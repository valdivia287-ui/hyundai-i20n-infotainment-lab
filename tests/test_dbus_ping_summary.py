"""D-Bus diagnostic tests with invented service names and messages only."""
import importlib.util
import struct
import tempfile
import unittest
from pathlib import Path

source = Path(__file__).resolve().parents[1] / 'tools/dbus_ping_summary.py'
spec = importlib.util.spec_from_file_location('ping_summary', source)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def message(kind, serial, fields):
    header = bytearray()
    for key, value in fields:
        header.extend(bytes((-len(header)) % 8))
        if isinstance(value, int):
            header.extend(bytes([key, 1, ord('u'), 0])+struct.pack('<I', value))
        else:
            value = value.encode()
            header.extend(bytes([key, 1, ord('s'), 0])+struct.pack('<I', len(value))+value+b'\0')
    result = bytes([ord('l'), kind, 0, 1])+struct.pack('<III', 0, serial, len(header))+header
    return result+bytes((-len(result)) % 8)


def trace_line(stamp, direction, fd, packet):
    escaped = ''.join('\\%03o' % byte for byte in packet)
    return f'101 {stamp} {direction}({fd}, {{iov_base="{escaped}"}}) = {len(packet)}\n'


class PingTests(unittest.TestCase):
    service = 'org.example.LabHome'

    def analyze(self, extra, reply_fd=8, truncated=False):
        request = message(1, 13, [(2, 'org.freedesktop.DBus.Peer'), (3, 'Ping'), (6, self.service)])
        reply = message(extra, 17, [(5, 13), (7, ':1.9')])
        text = trace_line('12:00:00.000000', 'sendmsg', 8, request)
        text += trace_line('12:00:00.012500', 'recvmsg', reply_fd, reply[:8] if truncated else reply)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'synthetic.txt'
            path.write_text(text)
            return module.summarize(path, self.service)

    def test_real_return_serial_and_latency(self):
        value = self.analyze(2)
        self.assertEqual((value['matched_returns'], value['max_ms']), (1, 12.5))
        self.assertEqual(value['replies'][0]['sender'], ':1.9')

    def test_error_is_not_success(self):
        value = self.analyze(3)
        self.assertEqual((value['matched_returns'], value['matched_errors']), (0, 1))

    def test_different_fd_cannot_match(self):
        self.assertEqual(self.analyze(2, reply_fd=9)['matched_returns'], 0)

    def test_incomplete_header_is_not_a_reply(self):
        value = self.analyze(2, truncated=True)
        self.assertEqual((value['matched_returns'], value['unmatched_not_proven_timeouts']), (0, 1))


if __name__ == '__main__':
    unittest.main()
