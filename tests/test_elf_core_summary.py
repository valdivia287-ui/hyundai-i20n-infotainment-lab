"""Synthetic cores only: verify rejection of incomplete diagnostic evidence."""
import importlib.util
from pathlib import Path
import struct
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('core_summary', Path(__file__).parents[1] / 'tools' / 'elf_core_summary.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def fixture(truncated=False, empty_mapping=False):
    notes = bytearray()
    for tid in (120, 121):
        payload = bytearray(336)
        struct.pack_into('<h', payload, 12, 3)
        struct.pack_into('<i', payload, 32, tid)
        notes.extend(struct.pack('<III', 5, 336, 1) + b'CORE\0\0\0\0' + payload)
    count = 3 if empty_mapping else 2
    note_offset = 64 + count * 56
    load_offset = note_offset + len(notes)
    header = b'\x7fELF\x02\x01\x01' + bytes(9)
    header += struct.pack('<HHIQQQIHHHHHH', 4, 62, 1, 0, 64, 0, 0, 64, 56, count, 0, 0, 0)
    ph = struct.pack('<IIQQQQQQ', 4, 0, note_offset, 0, 0, len(notes), len(notes), 4)
    ph += struct.pack('<IIQQQQQQ', 1, 6, load_offset, 0x1000, 0, 4096, 4096, 4096)
    if empty_mapping:
        ph += struct.pack('<IIQQQQQQ', 1, 5, load_offset + 999999, 0x2000, 0, 0, 4096, 4096)
    return header + ph + notes + bytes(16 if truncated else 4096)


class CoreEvidenceTests(unittest.TestCase):
    def inspect(self, content):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'core'
            path.write_bytes(content)
            return module.summarize(path)

    def test_two_threads_and_signal_in_complete_core(self):
        result = self.inspect(fixture())
        self.assertTrue(result['structurally_complete'])
        self.assertEqual(result['threads'], [{'tid': 120, 'signal': 3}, {'tid': 121, 'signal': 3}])

    def test_killed_dump_is_rejected_even_when_notes_are_intact(self):
        result = self.inspect(fixture(truncated=True))
        self.assertFalse(result['structurally_complete'])
        self.assertEqual(result['missing_segments'][0]['bytes_missing'], 4080)

    def test_zero_file_mapping_can_point_past_eof(self):
        self.assertTrue(self.inspect(fixture(empty_mapping=True))['structurally_complete'])

    def test_non_core_is_rejected(self):
        with self.assertRaises(ValueError):
            self.inspect(b'not a core')


if __name__ == '__main__':
    unittest.main()
