"""Invented D-Bus messages; no OEM captures or service names."""
import struct
import sys
import tempfile
import unittest
from pathlib import Path
from test_dbus_ping_summary import message, trace_line

source = Path(__file__).resolve().parents[1]/'tools'
sys.path.insert(0, str(source))
import dbus_subscription_summary as module


def packet(kind, serial, fields, value):
    data = bytearray(message(kind, serial, fields))
    body = value.encode()
    struct.pack_into('<I', data, 4, len(body)+5)
    return bytes(data)+struct.pack('<I', len(body))+body+b'\0'


class SubscriptionTests(unittest.TestCase):
    def result(self, lines):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)/'invented.txt'
            path.write_text(''.join(lines))
            return module.analyze([path])

    def test_matches_fd_and_reply_serial(self):
        call = packet(1, 13, [(3, 'AddMatch')], "type='signal',interface='org.example.Widget'")
        other = packet(1, 13, [(3, 'AddMatch')], 'other rule')
        error = packet(3, 90, [(4, 'org.freedesktop.DBus.Error.LimitsExceeded'), (5, 13)], 'invented match rules limit')
        value = self.result([trace_line('12:00:00.000000', 'sendmsg', 8, call), trace_line('12:00:00.000000', 'sendmsg', 9, other), trace_line('12:00:00.020000', 'recvmsg', 8, error)])
        self.assertEqual(value['add_match_calls'], 2)
        self.assertEqual(value['decoded_limit_errors'], 1)
        self.assertIn('org.example.Widget', value['errors'][0]['add_match_call']['rule'])

    def test_other_fd_is_unmatched(self):
        call = packet(1, 13, [(3, 'AddMatch')], 'invented rule')
        error = packet(3, 90, [(4, 'org.freedesktop.DBus.Error.LimitsExceeded'), (5, 13)], 'invented limit')
        value = self.result([trace_line('12:00:00.000000', 'sendmsg', 8, call), trace_line('12:00:00.020000', 'recvmsg', 9, error)])
        self.assertIsNone(value['errors'][0]['add_match_call'])

    def test_truncated_body_is_not_a_decoded_call(self):
        call = packet(1, 13, [(3, 'AddMatch')], 'invented rule')
        value = self.result([trace_line('12:00:00.000000', 'sendmsg', 8, call[:-3])])
        self.assertEqual(value['add_match_calls'], 0)
        self.assertEqual(value['incomplete_or_malformed_packets'], 1)

    def test_input_order_does_not_change_correlation(self):
        call = packet(1, 13, [(3, 'AddMatch')], 'earlier rule')
        error = packet(3, 90, [(4, 'org.freedesktop.DBus.Error.LimitsExceeded'), (5, 13)], 'invented limit')
        value = self.result([trace_line('12:00:00.020000', 'recvmsg', 8, error), trace_line('12:00:00.000000', 'sendmsg', 8, call)])
        self.assertEqual(value['errors'][0]['add_match_call']['rule'], 'earlier rule')
