#!/usr/bin/env python3
"""Offline summaries for process-scoped Wayland/D-Bus and renderer CPU traces.

Input traces must already exist. This tool does not attach to processes or
contact a guest; callback IDs are correlated only within the supplied client.
"""
import argparse
import ast
import importlib.util
import json
import math
import re
import struct
from collections import defaultdict
from pathlib import Path

_dbus_spec = importlib.util.spec_from_file_location(
    "public_dbus_ping_summary", Path(__file__).with_name("dbus_ping_summary.py"))
dbus_parser = importlib.util.module_from_spec(_dbus_spec)
_dbus_spec.loader.exec_module(dbus_parser)


def percentiles(values, unit="ms"):
    values = sorted(float(value) for value in values)
    suffix = "percent" if unit == "percent" else "ms"
    if not values:
        return {"n": 0, f"p50_{suffix}": None, f"p95_{suffix}": None,
                f"max_{suffix}": None}

    def quantile(p):
        rank = (len(values) - 1) * p
        lo, hi = math.floor(rank), math.ceil(rank)
        return values[lo] + (values[hi] - values[lo]) * (rank - lo)

    return {"n": len(values), f"p50_{suffix}": round(quantile(.5), 3),
            f"p95_{suffix}": round(quantile(.95), 3),
            f"max_{suffix}": round(max(values), 3)}


def _wayland_client_messages(paths):
    """Recover complete WAYLAND_DEBUG lines and their outer strace times."""
    messages = []
    write_re = re.compile(r'^\s*(?:(\d+)\s+)?(\d\d):(\d\d):(\d\d\.\d+)\s+write\(2,\s*("(?:\\.|[^"\\])*")')
    for source in paths:
        fragments = bytearray()
        fragment_stamp = None
        with Path(source).open(errors="replace") as trace:
            for line in trace:
                match = write_re.search(line)
                if not match:
                    continue
                try:
                    _, hour, minute, second, payload = match.groups()
                    if not fragments:
                        fragment_stamp = int(hour) * 3600 + int(minute) * 60 + float(second)
                    fragments.extend(ast.literal_eval("b" + payload))
                except (ValueError, SyntaxError):
                    continue
                while b"\n" in fragments:
                    raw, _, rest = fragments.partition(b"\n")
                    fragments = bytearray(rest)
                    decoded = raw.decode(errors="replace")
                    if re.search(r"\[\d+\.\d+\].*wl_(?:surface|callback)@", decoded):
                        messages.append((fragment_stamp, decoded))
                    fragment_stamp = None if not fragments else fragment_stamp
    return messages


def summarize_client_wayland(paths, client):
    """Correlate callbacks inside one process-scoped strace capture."""
    if isinstance(paths, (str, Path)):
        paths = [paths]
    frame_re = re.compile(r"wl_surface@(\d+)\.frame\(new id wl_callback@(\d+)\)")
    commit_re = re.compile(r"wl_surface@(\d+)\.commit\(")
    attach_re = re.compile(r"wl_surface@(\d+)\.attach\(wl_buffer@(\d+)")
    done_re = re.compile(r"wl_callback@(\d+)\.done\(")
    destroy_re = re.compile(r"wl_callback@(\d+)\.destroy\(")
    live, waiting, buffers = {}, defaultdict(list), {}
    latencies, pending_max = defaultdict(list), defaultdict(int)
    records = 0
    for stamp, message in sorted(_wayland_client_messages(paths), key=lambda row: row[0]):
        if match := attach_re.search(message):
            surface, buffer = match.groups()
            buffers[surface] = buffer
        if match := frame_re.search(message):
            surface, callback = match.groups()
            live[callback] = {"surface": surface, "commit_ms": None,
                              "buffer": buffers.get(surface)}
            waiting[surface].append(callback)
            pending_max[surface] = max(pending_max[surface], sum(
                value["surface"] == surface for value in live.values()))
            records += 1
        if match := commit_re.search(message):
            (surface,) = match.groups()
            for callback in waiting.pop(surface, []):
                if callback in live and live[callback]["commit_ms"] is None:
                    live[callback]["commit_ms"] = stamp * 1000
                    live[callback]["buffer"] = buffers.get(surface)
            records += 1
        if match := done_re.search(message):
            (callback,) = match.groups()
            item = live.pop(callback, None)
            if item and item["commit_ms"] is not None:
                elapsed = stamp * 1000 - item["commit_ms"]
                if elapsed >= 0:
                    latencies[item["surface"]].append((elapsed, item.get("buffer")))
            records += 1
        if match := destroy_re.search(message):
            (callback,) = match.groups()
            item = live.pop(callback, None)
            if item:
                waiting[item["surface"]] = [c for c in waiting[item["surface"]]
                                               if c != callback]
    surfaces = {}
    surface_ids = set(latencies) | {item["surface"] for item in live.values()}
    for surface in sorted(surface_ids, key=int):
        values = latencies[surface]
        surfaces[surface] = {
            "commit_to_frame_done": percentiles([value for value, _ in values]),
            "callbacks_pending_at_trace_end": sum(
                item["surface"] == surface for item in live.values()),
            "callbacks_pending_max": pending_max[surface],
            "buffers_seen": sorted({buffer for _, buffer in values if buffer}, key=int),
        }
    return {"available": bool(records), "client_identity": client,
            "identity_scope": "object IDs are correlated only within this process capture",
            "surfaces": surfaces, "callbacks_pending_at_trace_end": len(live),
            "protocol_records": records}


def summarize_platform_cpu(path):
    """Summarize sampled per-thread renderer CPU as percent of one guest core."""
    path = Path(path)
    if not path.is_file():
        return {"available": False, "reason": "CPU sample log absent"}
    samples = [json.loads(line) for line in path.read_text(errors="replace").splitlines()
               if line.strip()]
    samples = [item for item in samples if item.get("kind") == "sample"]
    samples.sort(key=lambda item: (item["uptime_ms"], item["pid"], item["tid"]))
    previous, by_process = {}, defaultdict(float)
    for item in samples:
        key = (item["pid"], item["tid"], item.get("birth_ticks"))
        old = previous.get(key)
        previous[key] = item
        if not old or old.get("renderer") != item.get("renderer"):
            continue
        dt = item["uptime_ms"] - old["uptime_ms"]
        ticks = item["utime_ticks"] + item["stime_ticks"] - old["utime_ticks"] - old["stime_ticks"]
        hz = float(item.get("ticks_per_second", 100))
        if dt > 0 and ticks >= 0 and hz > 0:
            ident = (item["renderer"], item["pid"], item.get("birth_ticks"), item["uptime_ms"])
            by_process[ident] += ticks / hz / (dt / 1000) * 100
    by_window, grouped = defaultdict(float), defaultdict(list)
    for (renderer, _pid, _birth, uptime), usage in by_process.items():
        by_window[renderer, uptime] += usage
    for (renderer, _uptime), usage in by_window.items():
        grouped[renderer].append(usage)
    return {"available": bool(grouped), "unit": "percent of one guest CPU core",
            "by_renderer": {name: percentiles(values, unit="percent")
                            for name, values in sorted(grouped.items())},
            "raw_samples": len(samples)}


def summarize_client_dbus(paths, client):
    """Pair visible method calls and replies across strace -ff TID files."""
    if isinstance(paths, (str, Path)):
        paths = [paths]
    line_re = re.compile(r"\b(\d\d):(\d\d):(\d\d\.\d+)\s+(sendmsg|recvmsg)\((\d+),")
    events, pending, results, seen = [], {"in": {}, "out": {}}, defaultdict(list), defaultdict(int)
    for source in paths:
        with Path(source).open(errors="replace") as trace:
            for line_number, line in enumerate(trace):
                match = line_re.search(line)
                if not match or re.search(r"= -1\b", line):
                    continue
                hour, minute, second, direction, fd = match.groups()
                now = int(hour) * 3600 + int(minute) * 60 + float(second)
                try:
                    data = b"".join(ast.literal_eval("b" + item) for item in
                                    re.findall(r'iov_base=("(?:\\.|[^"\\])*")', line))
                    for kind, serial, fields in dbus_parser.headers(data):
                        events.append((now, str(source), line_number, direction, fd,
                                       kind, serial, fields))
                except (ValueError, SyntaxError, struct.error, IndexError):
                    continue
    for now, _source, _line, direction, fd, kind, serial, fields in sorted(events):
        member, interface = fields.get(3), fields.get(2)
        if kind == 1 and member:
            category = ("Peer.Ping" if interface == "org.freedesktop.DBus.Peer" and member == "Ping"
                        else "AppAlive" if re.search(r"app.?alive", member, re.I) else None)
            if category:
                side = "out" if direction == "sendmsg" else "in"
                pending[side][(fd, serial)] = (now, category)
                seen[category] += 1
        elif kind in (2, 3):
            # recvmsg replies close outgoing calls; sendmsg replies close calls
            # handled by this process.
            side = "out" if direction == "recvmsg" else "in"
            start = pending[side].pop((fd, fields.get(5)), None)
            if start:
                begin, category = start
                results[category].append(((now - begin) % 86400 * 1000,
                                          "return" if kind == 2 else "error"))
    methods = {}
    for name in ("Peer.Ping", "AppAlive"):
        replies = results[name]
        methods[name] = {"observed_calls": seen[name],
                         "successful": percentiles([ms for ms, kind in replies if kind == "return"]),
                         "errors": sum(kind == "error" for _, kind in replies),
                         "unmatched_not_proven_timeouts": max(0, seen[name] - len(replies))}
    return {"available": any(seen.values()), "client_identity": client,
            "by_method": methods,
            "reason": None if any(seen.values()) else "no matching method headers"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wayland", type=Path, nargs="*", default=[])
    parser.add_argument("--dbus", type=Path, nargs="*", default=[])
    parser.add_argument("--cpu", type=Path)
    parser.add_argument("--client", default="unnamed-process")
    args = parser.parse_args()
    result = {"wayland": summarize_client_wayland(args.wayland, args.client)
              if args.wayland else None,
              "dbus": summarize_client_dbus(args.dbus, args.client) if args.dbus else None,
              "renderer_cpu": summarize_platform_cpu(args.cpu) if args.cpu else None}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
