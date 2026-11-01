#!/usr/bin/env python3
"""Offline correlation of visible D-Bus headers in a caller's strace.

No device or bus access. Truncated/split headers are skipped, so counts are
lower bounds. An unmatched request does not itself establish a timeout.
"""
import argparse
import ast
import json
import re
import statistics
import struct
from pathlib import Path


def headers(data):
    while len(data) >= 16 and data[0] in (ord('l'), ord('B')):
        endian = '<' if data[0] == ord('l') else '>'
        body, serial, size = struct.unpack_from(endian+'III', data, 4)
        if size > 1048576 or len(data) < 16+size:
            return
        position, fields = 16, {}
        while position < 16+size:
            position = (position+7)//8*8
            if position >= 16+size:
                break
            key, length = data[position:position+2]
            signature = data[position+2:position+2+length]
            position += 3+length
            if signature in (b's', b'o', b'u'):
                position = (position+3)//4*4
                value = struct.unpack_from(endian+'I', data, position)[0]
                position += 4
                if signature == b'u':
                    fields[key] = value
                else:
                    if position+value >= 16+size:
                        return
                    fields[key] = data[position:position+value].decode(errors='replace')
                    position += value+1
            elif signature == b'g':
                length = data[position]
                position += 1
                fields[key] = data[position:position+length].decode(errors='replace')
                position += length+1
            else:
                return
        yield data[1], serial, fields
        total = (16+size+7)//8*8+body
        if total > len(data):
            return
        data = data[total:]


def summarize(path, service):
    pending, replies = {}, []
    requests = 0
    with path.open(errors='replace') as trace:
        for line in trace:
            match = re.search(r'\b(\d\d:\d\d:\d\d\.\d+)\s+(sendmsg|recvmsg)\((\d+),', line)
            if not match or re.search(r'= -1\b', line):
                continue
            timestamp, direction, fd = match.groups()
            hour, minute, second = timestamp.split(':')
            seconds = int(hour)*3600+int(minute)*60+float(second)
            try:
                data = b''.join(ast.literal_eval('b'+item) for item in re.findall(r'iov_base=("(?:\\.|[^"\\])*")', line))
                for kind, serial, fields in headers(data):
                    if direction == 'sendmsg' and kind == 1 and fields.get(2) == 'org.freedesktop.DBus.Peer' and fields.get(3) == 'Ping' and fields.get(6) == service:
                        pending[fd, serial] = seconds
                        requests += 1
                    elif direction == 'recvmsg' and kind in (2, 3):
                        started = pending.pop((fd, fields.get(5)), None)
                        if started is not None:
                            replies.append(dict(serial=fields[5], time=timestamp,
                                latency_ms=round((seconds-started) % 86400*1000, 3),
                                kind='return' if kind == 2 else 'error', sender=fields.get(7)))
            except (ValueError, SyntaxError, struct.error, IndexError):
                continue
    values = [item['latency_ms'] for item in replies if item['kind'] == 'return']
    return dict(visible_headers_only=True, service=service, requests=requests,
        matched_returns=len(values), matched_errors=len(replies)-len(values),
        unmatched_not_proven_timeouts=len(pending),
        median_ms=statistics.median(values) if values else None,
        max_ms=max(values) if values else None, replies=replies)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('trace', type=Path)
    parser.add_argument('--service', required=True)
    arguments = parser.parse_args()
    print(json.dumps(summarize(arguments.trace, arguments.service), indent=2))
