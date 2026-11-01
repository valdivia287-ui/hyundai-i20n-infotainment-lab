import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('fixture', Path(__file__).parents[1] / 'tools/bootinfo_fixture.py')
fixture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixture)


class BootInfoFixtureTests(unittest.TestCase):
    def test_recorded_synthetic_europe_vector(self):
        expected = bytes.fromhex('aa8201240002000005000000000000000000000000000000000000000000000000000000000000000a')
        self.assertEqual(fixture.build_fixture(5), expected)

    def test_only_country_and_checksum_differ_from_control(self):
        control, europe = fixture.build_fixture(0), fixture.build_fixture(5)
        self.assertEqual([i for i, (a, b) in enumerate(zip(control, europe)) if a != b], [8, 40])
        self.assertEqual(control[-1], 0x0f)

    def test_observed_europe_operating_power_fixture(self):
        expected = bytes.fromhex('aa82012400000000050000000000000000000000000000000000000000000000000000000000000008')
        self.assertEqual(fixture.build_fixture(5, 0), expected)

    def test_unsupported_value_rejected(self):
        with self.assertRaises(ValueError):
            fixture.build_fixture(256)


if __name__ == '__main__':
    unittest.main()
