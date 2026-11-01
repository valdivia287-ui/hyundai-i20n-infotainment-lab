"""Original arbitrary synthetic vectors; no captured vehicle packets."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from uart_framing import Decoder, frame


class FramingTests(unittest.TestCase):
    def test_synthetic_vector(self):
        self.assertEqual(frame(0x1234, b'\x01'), bytes.fromhex('aa123401018c'))

    def test_fragmented_and_coalesced_input(self):
        decoder = Decoder()
        self.assertEqual(decoder.feed(bytes.fromhex('aa12')), [])
        self.assertEqual(decoder.feed(bytes.fromhex('3401018caa123401018c')),
                         [(0x1234, b'\x01'), (0x1234, b'\x01')])

    def test_bad_checksum_resynchronization(self):
        self.assertEqual(Decoder().feed(bytes.fromhex('aa123401018daa123401018c')),
                         [(0x1234, b'\x01')])

    def test_invalid_fields(self):
        for message_id, payload in ((-1, b''), (65536, b''), (1, bytes(256))):
            with self.assertRaises(ValueError):
                frame(message_id, payload)


if __name__ == '__main__':
    unittest.main()
