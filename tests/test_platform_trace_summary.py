import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).parents[1] / "tools/platform_trace_summary.py"
spec = importlib.util.spec_from_file_location("platform_trace_summary", TOOL)
summary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(summary)


def dbus_message(message_type, serial, fields):
    def pad(buffer, boundary):
        buffer.extend(b"\0" * (-len(buffer) % boundary))

    encoded_fields = bytearray()
    for key, value in fields:
        pad(encoded_fields, 8)
        field = bytearray((key, 1, ord("s" if isinstance(value, str) else "u"), 0))
        if isinstance(value, str):
            raw = value.encode()
            field.extend(len(raw).to_bytes(4, "little"))
            field.extend(raw + b"\0")
        else:
            field.extend(value.to_bytes(4, "little"))
        encoded_fields.extend(field)
    header = bytearray(b"l" + bytes((message_type, 0, 1)))
    header.extend((0).to_bytes(4, "little"))
    header.extend(serial.to_bytes(4, "little"))
    header.extend(len(encoded_fields).to_bytes(4, "little"))
    header.extend(encoded_fields)
    return bytes(header)


class PlatformTraceSummaryTests(unittest.TestCase):
    def test_wayland_uses_strace_clock_when_debug_clock_jumps(self):
        trace = (
            '00:00:01.001000 write(2, "[900000.000] -> wl_surface@3.frame(new id wl_callback@8)\\n", 63) = 63\n'
            '00:00:01.002000 write(2, "[5.000] -> wl_surface@3.commit()\\n", 37) = 37\n'
            '00:00:01.018000 write(2, "[700000.000] <- wl_callback@8.done(700000)\\n", 42) = 42\n')
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "client.trace"
            path.write_text(trace)
            result = summary.summarize_client_wayland(path, "synthetic")
        self.assertEqual(result["surfaces"]["3"]["commit_to_frame_done"]["p50_ms"], 16)

    def test_dbus_pairs_across_thread_files_in_time_order(self):
        call = dbus_message(1, 51, [(2, "org.freedesktop.DBus.Peer"),
                                    (3, "Ping"), (6, "example.service")])
        reply = dbus_message(2, 92, [(5, 51)])
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            # Reply filename sorts first; timestamps define event order.
            (folder / "a-reply").write_text(
                '00:00:10.025000 sendmsg(18, {msg_iov=[{iov_base="' +
                ''.join(f'\\x{byte:02x}' for byte in reply) + '"}]}) = 32\n')
            (folder / "z-call").write_text(
                '00:00:10.000000 recvmsg(18, {msg_iov=[{iov_base="' +
                ''.join(f'\\x{byte:02x}' for byte in call) + '"}]}) = 80\n')
            result = summary.summarize_client_dbus(
                [folder / "a-reply", folder / "z-call"], "synthetic")
        ping = result["by_method"]["Peer.Ping"]
        self.assertEqual(ping["successful"]["n"], 1)
        self.assertEqual(ping["successful"]["p50_ms"], 25)

    def test_cpu_percent_uses_percent_units_and_count(self):
        rows = [
            {"kind": "sample", "uptime_ms": 1000, "pid": 10, "tid": 10,
             "birth_ticks": 1, "utime_ticks": 0, "stime_ticks": 0,
             "ticks_per_second": 100, "renderer": "llvmpipe"},
            {"kind": "sample", "uptime_ms": 2000, "pid": 10, "tid": 10,
             "birth_ticks": 1, "utime_ticks": 50, "stime_ticks": 0,
             "ticks_per_second": 100, "renderer": "llvmpipe"}]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "cpu.jsonl"
            path.write_text("".join(json.dumps(row) + "\n" for row in rows))
            result = summary.summarize_platform_cpu(path)
        stats = result["by_renderer"]["llvmpipe"]
        self.assertEqual(stats["n"], 1)
        self.assertEqual(stats["p50_percent"], 50)


if __name__ == "__main__":
    unittest.main()
