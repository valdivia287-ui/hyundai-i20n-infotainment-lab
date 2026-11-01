#!/usr/bin/env python3
"""Build a SYNTHETIC offline UART fixture; does not open a device or socket.

Observed lab contract: reply 0x8201 has 36 payload bytes and XOR checksum.
The original MICOM/launcher logged Country=Korea for payload[4]=0, Europe
for payload[4]=5. Payload byte1=2 remains the existing diagnostic baseline.
This is not a captured vehicle response or a complete vehicle model.
"""
import argparse
import json
from functools import reduce
from operator import xor


def build_fixture(country_code, power_code=2):
    if country_code not in (0, 5):
        raise ValueError('Only the two observed laboratory country fixtures are supported')
    if power_code not in (0, 1, 2):
        raise ValueError("Unsupported laboratory power fixture")
    payload = bytearray(36)
    payload[1] = power_code
    payload[4] = country_code
    frame = bytes([0xAA, 0x82, 0x01, len(payload)]) + payload
    return frame + bytes([reduce(xor, frame, 0)])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--country-code', type=int, choices=(0, 5), required=True)
    parser.add_argument('--power-code', type=int, choices=(0, 1, 2), default=2)
    args = parser.parse_args()
    print(json.dumps({'synthetic': True, 'country_code': args.country_code, 'power_code': args.power_code,
                      'frame_hex': build_fixture(args.country_code, args.power_code).hex()}))


if __name__ == '__main__':
    main()
