"""Invented measurements only; no private traces or OEM content."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('clock_summary', Path(__file__).parents[1] / 'tools' / 'qt_animation_clock_summary.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ClockSummaryTests(unittest.TestCase):
    def test_detects_slow_interval_without_counting_resets(self):
        result = module.summarize([
            'HOME_ANIMATION_CLOCK qt_delta_ms=5 wall_delta_ms=1000',
            'HOME_ANIMATION_CLOCK qt_delta_ms=0 wall_delta_ms=0',
            'HOME_ANIMATION_CLOCK qt_delta_ms=-5 wall_delta_ms=1000',
            'HOME_ANIMATION_CLOCK qt_delta_ms=1000 wall_delta_ms=-5',
            'HOME_ANIMATION_CLOCK qt_delta_ms=200 wall_delta_ms=200',
            'HOME_ANIMATION_CLOCK qt_delta_ms=0 wall_delta_ms=2',
        ])
        self.assertEqual(result['invalid_or_reset'], 3)
        self.assertEqual(result['eligible_intervals'], 2)
        self.assertEqual(result['slow_intervals'], 1)
        self.assertEqual(result['worst_interval']['qt_to_wall_ratio'], .005)

    def test_empty_malformed_and_unrelated_lines(self):
        result = module.summarize(['unrelated secret: must not be emitted',
                                  'HOME_ANIMATION_CLOCK broken',
                                  'HOME_ANIMATION_WALLTIME_POLICY enabled=1'])
        self.assertEqual(result['policy_markers'], 1)
        self.assertEqual(result['invalid_or_reset'], 1)
        self.assertIsNone(result['worst_interval'])
        self.assertNotIn('secret', str(result))


if __name__ == '__main__':
    unittest.main()
