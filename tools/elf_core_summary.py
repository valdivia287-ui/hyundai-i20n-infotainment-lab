#!/usr/bin/env python3
"""Validate private Linux x86-64 kernel cores before trusting a backtrace.

Reads metadata only. Does not recover missing bytes, execute the inferior,
load debugger scripts, or contact a symbol service. A structurally complete
file still needs matching executable/shared libraries for useful debugging.
"""
import argparse
import json
from pathlib import Path
import struct


def summarize(path):
    path = Path(path)
    size = path.stat().st_size
    with path.open('rb') as stream:
        header = stream.read(64)
        if len(header) != 64 or header[:7] != b'\x7fELF\x02\x01\x01':
            raise ValueError('Expected a little-endian ELF64 file')
        fields = struct.unpack_from('<HHIQQQIHHHHHH', header, 16)
        kind, machine = fields[:2]
        offset, entry_size, count = fields[4], fields[8], fields[9]
        if kind != 4 or machine != 62:
            raise ValueError('Expected an x86-64 ET_CORE file')
        if entry_size != 56 or not 1 <= count <= 8192:
            raise ValueError('Unsupported program header table')
        if offset + count * entry_size > size:
            raise ValueError('Truncated program header table')
        stream.seek(offset)
        segments = [struct.unpack('<IIQQQQQQ', stream.read(56)) for _ in range(count)]
        missing = []
        threads = []
        invalid_notes = []
        end = offset + count * entry_size
        for index, segment in enumerate(segments):
            kind, _, start, _, _, length, _, _ = segment
            if not length:
                continue  # File-free mappings may legitimately point beyond EOF.
            end = max(end, start + length)
            if start + length > size:
                missing.append({'segment': index, 'bytes_missing': start + length - size})
                continue
            if kind != 4:
                continue
            if length > 16 * 1024**2:
                invalid_notes.append({'segment': index, 'reason': 'note segment exceeds bounded parser limit'})
                continue
            stream.seek(start)
            notes = stream.read(length)
            pos = 0
            while pos < len(notes):
                if len(notes) - pos < 12:
                    if any(notes[pos:]):
                        invalid_notes.append({'segment': index, 'reason': 'truncated note header'})
                    break
                name_len, data_len, note_kind = struct.unpack_from('<III', notes, pos)
                pos += 12
                data_start = pos + ((name_len + 3) & ~3)
                next_pos = data_start + ((data_len + 3) & ~3)
                if next_pos > len(notes):
                    invalid_notes.append({'segment': index, 'reason': 'truncated note payload'})
                    break
                name = notes[pos:pos + name_len].rstrip(b'\0')
                if name == b'CORE' and note_kind == 1:
                    if data_len != 336:
                        invalid_notes.append({'segment': index, 'reason': 'unexpected x86-64 PRSTATUS size'})
                    else:
                        threads.append({'tid': struct.unpack_from('<i', notes, data_start + 32)[0],
                                        'signal': struct.unpack_from('<h', notes, data_start + 12)[0]})
                pos = next_pos
    return {'file_bytes': size, 'declared_file_end': end,
            'program_headers': count, 'missing_segments': missing,
            'invalid_notes': invalid_notes, 'threads': threads,
            'structurally_complete': not missing and not invalid_notes and bool(threads)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('core', type=Path)
    args = parser.parse_args()
    try:
        result = summarize(args.core)
    except (ValueError, OSError) as exc:
        parser.exit(2, str(exc) + '\n')
    print(json.dumps(result, indent=2))
    return 0 if result['structurally_complete'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
