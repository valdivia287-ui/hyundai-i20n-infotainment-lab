#!/usr/bin/env python3
"""Build a SYNTHETIC offline UART fixture; does not open a device or socket.

Observed lab contract: reply 0x8201 has 36 payload bytes and XOR checksum.
The original MICOM/launcher logged Country=Korea for payload[4]=0, Europe
for payload[4]=5. Payload byte1=2 remains the existing diagnostic baseline.
This is not a captured vehicle response or a complete vehicle model.
Optional software selection: CarType23=BC3,81=BC3N25MY; language7=Spanish(EU).
The reviewed HighPerformanceCar boot option is separate from CarType.
"""
import argparse
import json
from functools import reduce
from operator import xor


def build_fixture(country_code, power_code=2, *, language_code=0,
                  car_type_code=0, high_performance_car=False):
    if country_code not in (0, 5):
        raise ValueError('Only the two observed laboratory country fixtures are supported')
    if power_code not in (0, 1, 2):
        raise ValueError("Unsupported laboratory power fixture")
    if language_code not in (0, 7) or car_type_code not in (0, 23, 81):
        raise ValueError('Unreviewed software-profile fixture')
    if high_performance_car and car_type_code != 81:
        raise ValueError('HighPerformanceCar is reviewed only with explicit CarType81')
    payload = bytearray(36)
    payload[1] = power_code
    payload[3] = car_type_code
    payload[4] = country_code
    payload[26] = language_code
    # Original parser: big-endian options word, bit3 in the last byte.
    if high_performance_car:
        payload[33] = 8
    frame = bytes([0xAA, 0x82, 0x01, len(payload)]) + payload
    return frame + bytes([reduce(xor, frame, 0)])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--country-code', type=int, choices=(0, 5), required=True)
    parser.add_argument('--power-code', type=int, choices=(0, 1, 2), default=2)
    parser.add_argument('--language-code', type=int, choices=(0, 7), default=0)
    parser.add_argument('--car-type-code', type=int, choices=(0, 23, 81), default=0)
    parser.add_argument('--high-performance-car', action='store_true')
    args = parser.parse_args()
    if args.high_performance_car and args.car_type_code != 81:
        parser.error('HighPerformanceCar requires explicit --car-type-code 81')
    print(json.dumps({'synthetic': True, 'country_code': args.country_code, 'power_code': args.power_code,
                      'language_code': args.language_code, 'car_type_code': args.car_type_code,
                      'high_performance_car': args.high_performance_car,
                      'frame_hex': build_fixture(args.country_code, args.power_code,
                          language_code=args.language_code, car_type_code=args.car_type_code,
                          high_performance_car=args.high_performance_car).hex()}))


if __name__ == '__main__':
    main()
