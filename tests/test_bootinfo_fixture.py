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

    def test_original_launcher_spanish_bc3n25_boot_vector(self):
        expected = bytes.fromhex('aa8201240000005105000000000000000000000000000000000000000000070000000000000000005e')
        self.assertEqual(fixture.build_fixture(5, 0, language_code=7, car_type_code=81), expected)

    def test_high_performance_option_is_independent_of_model(self):
        base = fixture.build_fixture(5, 0, language_code=7, car_type_code=81)
        selected = fixture.build_fixture(5, 0, language_code=7, car_type_code=81,
                                         high_performance_car=True)
        self.assertEqual([i for i, (a, b) in enumerate(zip(base, selected)) if a != b], [37, 40])
        self.assertEqual((int.from_bytes(selected[34:38], 'big') >> 3) & 1, 1)
        self.assertEqual(selected[-1], 0x56)
        self.assertEqual(selected[7], 81)

    def test_unreviewed_model_option_combination_rejected(self):
        for car_type in (0, 23):
            with self.subTest(car_type=car_type), self.assertRaises(ValueError):
                fixture.build_fixture(5, car_type_code=car_type, high_performance_car=True)


if __name__ == '__main__':
    unittest.main()
