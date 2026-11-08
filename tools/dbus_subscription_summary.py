#!/usr/bin/env python3
"""Read-only AddMatch/limit-error correlation from one process's strace files.

Only complete visible packets are decoded. Missing/error-free output does not
prove that the bus accepted every subscription. Inputs may contain private data;
keep both traces and generated results outside the public repository.
"""
import argparse
import ast
import bisect
import json
import re
import struct
from collections import defaultdict
from pathlib import Path

from dbus_ping_summary import headers


def analyze(paths):
    calls = defaultdict(list)
    errors = []
    incomplete = 0
    count = 0
    for path in paths:
        with Path(path).open(errors='replace') as handle:
            for line in handle:
                match = re.search(r'(\d\d):(\d\d):(\d\d\.\d+)\s+(sendmsg|recvmsg)\((\d+),', line)
                if not match or '= -1' in line:
                    continue
                hour, minute, second, direction, fd = match.groups()
                stamp = int(hour)*3600+int(minute)*60+float(second)
                try:
                    data = b''.join(ast.literal_eval('b'+s) for s in re.findall(r'iov_base=("(?:\\.|[^"\\])*")', line))
                    while len(data) >= 16 and data[0] in (108, 66):
                        endian = '<' if data[0] == 108 else '>'
                        size, serial, length = struct.unpack_from(endian+'III', data, 4)
                        start = (16+length+7)//8*8
                        if length > 1048576 or size > 1048576 or len(data) < start+size:
                            incomplete += 1
                            break
                        frame = data[:start+size]
                        kind, serial, fields = next(headers(frame))
                        body = frame[start:]
                        def string():
                            length = struct.unpack_from(endian+'I', body)[0]
                            if 4+length >= len(body) or body[4+length] != 0:
                                raise ValueError('Incomplete D-Bus string')
                            return body[4:4+length].decode(errors='replace')
                        if direction == 'sendmsg' and kind == 1 and fields.get(3) == 'AddMatch':
                            calls[int(fd), serial].append({'seconds': stamp, 'time': match[0].split()[0], 'rule': string()})
                            count += 1
                        elif direction == 'recvmsg' and kind == 3 and fields.get(4) == 'org.freedesktop.DBus.Error.LimitsExceeded':
                            errors.append({'seconds': stamp, 'fd': int(fd), 'reply_serial': fields.get(5), 'message': string()})
                        data = data[start+size:]
                except (ValueError, SyntaxError, IndexError, StopIteration, struct.error):
                    incomplete += 1
    for values in calls.values():
        values.sort(key=lambda item: item['seconds'])
    for error in errors:
        values = calls.get((error['fd'], error['reply_serial']), [])
        index = bisect.bisect_right([item['seconds'] for item in values], error['seconds'])-1
        error['add_match_call'] = values[index] if index >= 0 else None
    return {'scope': 'Complete visible packets, threads of one process, one day; FD reuse/split packets can limit correlation',
            'add_match_calls': count, 'decoded_limit_errors': len(errors),
            'incomplete_or_malformed_packets': incomplete, 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('traces', nargs='+', type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.traces), indent=2))


if __name__ == '__main__':
    main()
