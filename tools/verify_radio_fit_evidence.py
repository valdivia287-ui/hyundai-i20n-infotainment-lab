#!/usr/bin/env python3
"""Offline verification of the bounded Radio-fit/VNC experiment; no VM access.
Reads only the supplied completed run, prints JSON, and never modifies evidence.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from PIL import Image, ImageChops

if not __debug__:
    raise SystemExit("Run without Python -O: evidence assertions must remain enabled")

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('run',type=Path)
args=parser.parse_args();run=args.run.resolve()
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def text(name):return (run/name).read_text(errors='replace')
def compare(first,second,box=None):
    with Image.open(run/first) as src, Image.open(run/second) as ref:
        a=src.convert('RGB');b=ref.convert('RGB')
        assert a.size==b.size==(1280,800)
        if box:a=a.crop(box);b=b.crop(box)
        return ImageChops.difference(a,b).getbbox()
console=text('console.log');weston=text('guest-logs/weston.log')
assert 'reboot: Power down' in console,'Requires completed clean shutdown'
assert not (run/'worker-error.log').exists(),'Worker error requires separate classification'
assert 'segfault at' not in console
assert 'AppKill' not in text('guest-logs/app-launcher.txt')
env=json.loads(text('profile-env.json'));command=json.loads(text('command.json'))
assert env['CA_HMI_ACTIVE_RADIO_FIT']=='1' and env['CA_POST_CYCLE_STABILITY_SEC']=='0'
assert command[command.index('-nic')+1]=='none'
assert digest(run/'payload/hmi-controller-fullscreen.so')=='2f273fe437e6cb888847d513a1199966ec81a25aa843116c6a010fb6836f9b6d'
assert digest(run/'payload/qt-input-probe.so')=='64f7c8c601941df8abd651b2d478412efeb4ffd488f637585038a981cf009cb2'
fit=[line for line in weston.splitlines() if 'CA_ACTIVE_RADIO_GEOMETRY_FIT ' in line]
assert fit and all('source=0,0,1920,720 source_unchanged=1 opacity_unchanged=1 layer_unchanged=1' in line for line in fit)
assert 'CA_ACTIVE_HOME_GEOMETRY_FIT id=1000 from=1920x720 to=1280x730' in weston
postfit=weston[weston.index(fit[0]):]
radio_frames=[line for line in postfit.splitlines() if 'CA_FRAME_PROBE ' in line and 'id=1002 ' in line and re.search(r'\bvisible=1 ',line) and 'buffer=1920x720' in line]
assert radio_frames and all('dest=0,0,1280,730 ' in line for line in radio_frames)
roi=(0,100,1280,690)
checks={
 'vnc_page1_matches_reference_content':compare('operator-vnc-home1.png','home-return-layout-ready-before-input.png',roi) is None,
 'returned_home_matches_page1_content':compare('operator-vnc-home-return-50s.png','operator-vnc-home1.png',roi) is None,
 'final_vnc_page0_matches_full_baseline':compare('operator-vnc-home0-after-return.png','operator-baseline-home0.png') is None,
 'station_list_80s_image_equals_fm':compare('operator-vnc-station-list-80s.png','operator-vnc-radio-wait-100s.png') is None,
}
assert all(checks.values())
health={}
for line in text('guest-logs/interactive-health.txt').splitlines():
    fields=dict(part.split('=',1) for part in line.split() if '=' in part)
    name=fields['name'];item=health.setdefault(name,{'identities':set(),'samples':0,'rss_kib':[]})
    item['identities'].add((int(fields['pid']),int(fields['birth'])))
    item['samples']+=1;item['rss_kib'].append(int(fields['rss_kib']))
assert len(health)==6 and all(len(item['identities'])==1 and item['samples']>=7 for item in health.values())
for item in health.values():
    item['identities']=sorted(item['identities']);rss=item.pop('rss_kib')
    item.update(rss_min_kib=min(rss),rss_max_kib=max(rss),rss_final_minus_initial_kib=rss[-1]-rss[0])
exports=[json.loads(line) for line in text('screenshot-export.jsonl').splitlines()]
for item in exports:assert digest(run/item['source'])==item['source_sha256']
inputs=[json.loads(line) for line in text('operator-vnc-input.jsonl').splitlines()]
assert [item['action'] for item in inputs]==['drag-left','radio','station-list','home','drag-right']
intent=re.findall(r'^OEM_LAYOUT_INTENT app=(\d+) source=three_real_getters',text('guest-logs/oem-layout-intent-observer.txt'),re.M)
assert intent[-3:]==['11','77','11']
observations=[json.loads(line) for line in text('operator-observations.jsonl').splitlines()]
important=['console.log','command.json','profile-env.json','replay-options.json','radio-fit-reproduction.json','screenshot-export.jsonl','operator-vnc-input.jsonl','operator-observations.jsonl','guest-logs/weston.log','guest-logs/oem-layout-intent-observer.txt','guest-logs/interactive-health.txt','guest-logs/radio-qt-input-probe.txt','guest-logs/home-qt-input-probe.txt','guest-logs/app-launcher.txt']
important += [p.name for p in sorted(run.glob('operator-*.png')) if '-review' not in p.name]
result={'run':run.name,'result':'radio_fit_geometry_home_return_and_vnc_navigation_verified','scope':'One bounded pending Radio-fit trial; existing automated preparation then a VNC Radio roundtrip. No new stability or Qt/Spanish diagnostic. Not a complete emulator.', 'radio_fit_log':fit,'visible_radio_frames_after_fit':len(radio_frames),'pixel_checks':checks,'real_getter_intent_sequence':intent,'health':health,'exports':{'total':len(exports),'verified':sum(x['export_status']=='verified' for x in exports),'unavailable':sum(x['export_status']!='verified' for x in exports),'all_WSL_original_hashes_valid':True},'inputs':inputs,'observations':observations,'limitations':['Station List click reached original Qt and release seq3, but repeated-foreground Station List was not visually shown; snapshots equal FM.','Slow foreground presentation: first post-click screenshot still Home; later full Radio. No exact presentation latency inferred between samples.','No new ten-minute stability measurement; preserved earlier stability profile unchanged.','No RF/audio, navigation, native ASTC or guest GPU acceleration claims.'],'shutdown':'Explicit clean owned stop; reboot: Power down, guest logs recovered','sha256':{name:digest(run/name) for name in important}}
print(json.dumps(result,indent=2))
