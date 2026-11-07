#!/usr/bin/env python3
"""Read-only checks for a completed private native BC3N25MY N Mode audit.

Requires original private run evidence and Pillow. Hashes and protocol checks
do not replace visual review or prove complete vehicle/audio functionality.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from PIL import Image, ImageChops


def verify(run):
    result = json.loads((run / 'app-audit-result.json').read_text())
    assert result['cycle_verified'] and result['native_home_icon_verified']
    assert result['car_type_code'] == 81 and result['high_performance_car']
    assert result['capability_adapter'] is False and result['argv_adapter_used'] is False
    assert result['sha256']
    for name, expected in result['sha256'].items():
        path = (run / name).resolve()
        assert path.is_relative_to(run.resolve())
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, name
    argv = (run / 'guest-logs/audit-before-AppHomeScreen-argv.txt').read_text().splitlines()
    assert argv[0] == '/app/bin/AppHomeScreen'
    assert all(arg in argv for arg in ('-vv:81', '-pf:1', '-nm:2', '-cv:5', '-l:7'))
    maps = (run / 'guest-logs/audit-before-AppHomeScreen-maps.txt').read_text()
    env = (run / 'guest-logs/audit-before-AppHomeScreen-env.txt').read_text()
    for adapter in ('nmode-hmi-capability.so', 'nmode-argv.so'):
        assert adapter not in maps and adapter not in env
    for marker in ('NMODE_HMI_CAPABILITY', 'NMODE_OEM_ARGV'):
        assert not (run / 'payload' / marker).exists()
    options = json.loads((run / 'replay-options.json').read_text())
    assert options['car_type_code'] == 81 and options['high_performance_car'] and options['spanish_eu']
    launch = (run / 'guest-logs/app-launcher.txt').read_text(errors='replace')
    assert 'HighPerformanceCar[1]' in launch and 'Spanish(EU)' in launch
    frames = re.findall(r'request_id=0x0201[^\n]*frame_hex=([0-9a-f]+)', (run / 'synthetic-uart-reply.txt').read_text())
    assert frames
    for item in frames:
        frame = bytes.fromhex(item)
        assert len(frame) == 41 and frame[:4] == bytes.fromhex('aa820124')
        checksum = 0
        for value in frame:
            checksum ^= value
        assert checksum == 0
        payload = frame[4:-1]
        assert (payload[1], payload[3], payload[4], payload[26], payload[33]) == (0, 81, 5, 7, 8)
    manager = (run / 'guest-logs/audit-manager.strace').read_text(errors='replace')
    pid = result['process']['pid']
    assert f'Transition::request[{pid}] id[304] appid[500] reason[5185]' in manager
    assert 'requestShow AppId[APP_N_MODE][500]' in manager
    assert len(re.findall(fr'Transition::request\[{pid}\] id\[304\] appid\[11\] reason\[30\]', manager)) >= 2
    assert 'Application::AppKill()' not in manager
    identities = {}
    for line in (run / 'guest-logs/interactive-health.txt').read_text().splitlines():
        fields = dict(part.split('=', 1) for part in line.split() if '=' in part)
        identities.setdefault(fields['name'], set()).add((int(fields['pid']), int(fields['birth'])))
    assert set(identities) == {'AppLauncher', 'ApplicationManager', 'AppHomeScreen', 'micommanager_userspace', 'weston'}
    assert all(len(values) == 1 for values in identities.values())
    assert next(iter(identities['AppHomeScreen'])) == (pid, result['process']['birth'])
    weston = (run / 'guest-logs/weston.log').read_text(errors='replace')
    assert re.search(fr'CA_SURFACE_OWNER[^\n]*id={result["process"]["surface"]} pid={pid} comm=AppHomeScreen', weston)
    command = json.loads((run / 'command.json').read_text())
    assert command[command.index('-nic') + 1] == 'none'
    exports = [json.loads(line) for line in (run / 'screenshot-export.jsonl').read_text().splitlines()]
    assert len(exports) == result['exports_verified'] and all(x['export_status'] == 'verified' for x in exports)
    for item in exports:
        source = (run / item['source']).resolve()
        assert source.is_relative_to(run.resolve())
        assert hashlib.sha256(source.read_bytes()).hexdigest() == item['source_sha256']
    first = Image.open(run / 'audit-home-before-nmode.png').convert('RGB')
    final = Image.open(run / 'operator-bc3n25-nativecap-home0-final.png').convert('RGB')
    assert first.size == final.size == (1280, 800)
    box = ImageChops.difference(first, final).getbbox()
    assert box is None or (box[0] >= 610 and box[1] >= 703 and box[2] <= 669 and box[3] <= 712)
    assert (list(box) if box else None) == result['final_home_diff_bbox']
    assert 'Power down' in (run / 'console.log').read_text(errors='replace')
    return {'checks_passed': True, 'native_icon_origin_pid': pid,
            'exports_verified': len(exports), 'final_home_diff_bbox': box,
            'scope': 'Partial N Mode UI cycle; original images require human review; artwork/audio/sensors/stability limits remain'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.run), indent=2))


if __name__ == '__main__':
    main()
