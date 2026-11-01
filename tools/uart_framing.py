"""Original lab framing helpers. No device access or captured vehicle data."""
from functools import reduce
from operator import xor


def frame(message_id, payload=b''):
    if not 0 <= message_id <= 0xffff or len(payload) > 255:
        raise ValueError('UART field out of range')
    data = bytes([0xaa, message_id >> 8, message_id & 255, len(payload)]) + bytes(payload)
    return data + bytes([reduce(xor, data, 0)])


class Decoder:
    def __init__(self):
        self.pending = bytearray()

    def feed(self, data):
        self.pending.extend(data)
        result = []
        while self.pending:
            if self.pending[0] != 0xaa:
                del self.pending[0]
                continue
            if len(self.pending) < 4:
                break
            size = self.pending[3] + 5
            if len(self.pending) < size:
                break
            candidate = bytes(self.pending[:size])
            if reduce(xor, candidate, 0):
                del self.pending[0]
                continue
            del self.pending[:size]
            result.append((int.from_bytes(candidate[1:3], 'big'), candidate[4:-1]))
        return result
