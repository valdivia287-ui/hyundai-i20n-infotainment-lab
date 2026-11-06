#!/usr/bin/env python3
"""Summarize original lab probe measurements; never emit raw trace lines.

The probe logs some immediately preceding driver intervals, not every interval.
These samples therefore cannot establish total animation time or causality.
"""
import argparse
import json
import re
from pathlib import Path


def summarize(lines):
    result = {'policy_markers': 0, 'clock_samples': 0, 'invalid_or_reset': 0,
              'eligible_intervals': 0, 'slow_intervals': 0, 'worst_interval': None,
              'limits': 'Sampled adjacent-call deltas only; not a continuous timeline or a causal diagnosis.'}
    for line in lines:
        if line.startswith('HOME_ANIMATION_WALLTIME_POLICY '):
            result['policy_markers'] += 1
        if not line.startswith('HOME_ANIMATION_CLOCK '):
            continue
        result['clock_samples'] += 1
        fields = dict(re.findall(r'(qt_delta_ms|wall_delta_ms)=(-?\d+)\b', line))
        try:
            qt_ms, wall_ms = int(fields['qt_delta_ms']), int(fields['wall_delta_ms'])
        except (KeyError, ValueError):
            result['invalid_or_reset'] += 1
            continue
        if wall_ms <= 0 or qt_ms < 0:
            result['invalid_or_reset'] += 1
            continue
        # Short intervals amplify quantization. Inspect only gaps >=100 ms.
        if wall_ms < 100:
            continue
        result['eligible_intervals'] += 1
        ratio = qt_ms / wall_ms
        if ratio < .5:
            result['slow_intervals'] += 1
        worst = result['worst_interval']
        if worst is None or ratio < worst['qt_to_wall_ratio']:
            result['worst_interval'] = {'qt_delta_ms': qt_ms, 'wall_delta_ms': wall_ms,
                                        'qt_to_wall_ratio': ratio}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('trace', type=Path, help='Private lab probe log to read; no raw lines are printed')
    args = parser.parse_args()
    with args.trace.open(encoding='utf-8', errors='replace') as stream:
        print(json.dumps(summarize(stream), indent=2))


if __name__ == '__main__':
    main()
