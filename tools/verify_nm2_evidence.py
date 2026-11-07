#!/usr/bin/env python3
"""Verify supporting evidence of the reviewed nm2/pf0 original UI reference offline.
Requires manual screen review; never starts a VM or executes OEM code.
"""
import argparse,hashlib,json,re
from pathlib import Path
from PIL import Image,ImageChops
if not __debug__:raise SystemExit('Evidence assertions require Python without -O')
p=argparse.ArgumentParser(description=__doc__);p.add_argument('run',type=Path);a=p.parse_args();r=a.run.resolve()
def txt(f):return (r/f).read_text(errors='replace')
def sha(f):return hashlib.sha256((r/f).read_bytes()).hexdigest()
assert 'reboot: Power down' in txt('console.log')
assert not (r/'worker-error.log').exists()
assert 'AppKill' not in txt('guest-logs/app-launcher.txt') and 'segfault at' not in txt('console.log')
argv=txt('guest-logs/audit-before-AppHomeScreen-argv.txt').splitlines()
for arg in ['-nm:2','-pf:0','-cv:5','-l:7']:assert arg in argv
for property in ['drawing_application','appmanager_application']:assert re.search(r'int32 500\s*$',txt('guest-logs/audit-after-'+property+'.txt'))
assert re.search(r'int32 1\s*$',txt('guest-logs/audit-after-application500-status.txt'))
assert 'Main_Screen_N_Mode_Track.qml' in txt('guest-logs/audit-nmode.strace')
assert 'id[304] appid[500] reason[5185]' in txt('guest-logs/audit-manager.strace')
assert 'requestShow AppId[APP_N_MODE][500]' in txt('guest-logs/audit-manager.strace')
assert 'success=1 original_MICOM_unchanged=1 sensors_unchanged=1' in txt('guest-logs/nmode-hmi-capability.txt')
assert 'source=0,0,1920,720 dest=0,0,1280,730' in txt('guest-logs/home-initial-layout-ready.txt')
owner=txt('guest-logs/home-initial-layout-owner.txt');assert 'comm=AppHomeScreen' in owner
sid=int(re.search(r'id=(\d+)',owner)[1]);pid=int(re.search(r'pid=(\d+)',owner)[1])
assert txt('guest-logs/nmode-observed-source-integrity.txt').count(': OK')==42
assert txt('guest-logs/nmode-observed-output-integrity.txt').count(': OK')==21
restored=(r/'payload/NMODE_NM2_PNG').is_file()
if restored:
 assert txt('guest-logs/nmode-nm2-verified-source-integrity.txt').count(': OK')==132
 assert txt('guest-logs/nmode-nm2-verified-output-integrity.txt').count(': OK')==66
 assert 'count=66' in txt('guest-logs/nmode-nm2-verified-setup.txt')
events=[json.loads(l) for l in txt('operator-vnc-input.jsonl').splitlines()]
actions=[e['action'] for e in events]
assert actions in (['nmode-next-page','home','drag-right'],['nmode-next-page','home','drag-right','drag-right'])
# A premature drag during the native Home transition is retained, never counted as proof.
confirmed='operator-nmode-nm2-home-return-confirmed.png'
if len(actions)==4:
 assert (r/confirmed).is_file()
 observations=[json.loads(l) for l in txt('operator-observations.jsonl').splitlines()]
 observed=next(e['utc'] for e in observations if e['screenshot']==confirmed)
 assert events[-2]['utc'] < observed < events[-1]['utc']

frames=['audit-home-before-nmode.png','operator-nmode-nm2-original-dashboard.png','operator-nmode-nm2-page2-after-drag.png','operator-nmode-nm2-home-return-intermediate.png','operator-nmode-nm2-home0-after-return.png']
if (r/confirmed).is_file():frames[3]=confirmed
if (r/'operator-nmode-nm2-home0-confirmed.png').is_file():frames[4]='operator-nmode-nm2-home0-confirmed.png'
images=[]
for name in frames:
 with Image.open(r/name) as im:assert im.size==(1280,800);images.append(im.convert('RGB'))
assert ImageChops.difference(images[1],images[2]).getbbox() is not None
box=ImageChops.difference(images[0],images[-1]).getbbox();assert box is None or (610<=box[0]<=box[2]<=669 and 703<=box[1]<=box[3]<=712)
intent=txt('guest-logs/oem-layout-intent-observer.txt');assert len(re.findall(r'^OEM_LAYOUT_INTENT app=11 ',intent,re.M))>=2
health={}
for line in txt('guest-logs/interactive-health.txt').splitlines():
 d=dict(x.split('=',1) for x in line.split() if '=' in x);h=health.setdefault(d['name'],dict(identities=set(),rss=[],samples=0));h['identities'].add((int(d['pid']),int(d['birth'])));h['rss'].append(int(d['rss_kib']));h['samples']+=1
assert len(health)==5 and all(len(x['identities'])==1 for x in health.values())
for h in health.values():
 h['identities']=sorted(h['identities']);v=h.pop('rss');h.update(rss_min_kib=min(v),rss_max_kib=max(v),rss_final_minus_initial_kib=v[-1]-v[0])
command=json.loads(txt('command.json'));assert command[command.index('-nic')+1]=='none'
exports=[json.loads(l) for l in txt('screenshot-export.jsonl').splitlines()]
for x in exports:assert sha(x['source'])==x['source_sha256']
files=frames+['console.log','command.json','profile-env.json','replay-options.json','operator-vnc-input.jsonl','operator-observations.jsonl','guest-logs/audit-manager.strace','guest-logs/audit-nmode.strace','guest-logs/home-startup.strace','guest-logs/micom-home-startup.strace','guest-logs/audit-before-AppHomeScreen-argv.txt','guest-logs/audit-before-AppHomeScreen-env.txt','guest-logs/audit-before-AppHomeScreen-maps.txt','guest-logs/home-initial-layout-ready.txt','guest-logs/home-initial-layout-owner.txt','guest-logs/interactive-health.txt','guest-logs/oem-layout-intent-observer.txt']
if restored:files+=['guest-logs/nmode-nm2-verified-source-integrity.txt','guest-logs/nmode-nm2-verified-output-integrity.txt','guest-logs/nmode-nm2-verified-setup.txt']
print(json.dumps(dict(result='Original NMode500 nm2/pf0 two-page UI and native Home return verified, partial artwork/hardware',run=r.name,owner=dict(surface=sid,pid=pid,executable='/app/bin/AppHomeScreen'),request=[304,500,5185,1,0],argv=argv,manual_screen_review='Spanish original Track dashboard page1, native VNC horizontal page2, native Home control to full menu and further native Home page0 drag',final_home_diff_bbox=box,health=health,limits=['MY23 owner target; nm2/pf0 corresponds to OEM BC3 row, not full physical car identity','Original boot fixture CarType still0/LX2; existing frontendBC3 override and local nModeVariantFlg adaptation explicit','No new CAN/MICOM/D-Bus replies or sensor values; actual original calls/shared memory traced',('66 nm2-specific original textures restored plus21baseline; one empty base source pair excluded, not native ASTC' if restored else '21 legacy decoded original textures installed; nm2-specific graphics still lack fallback, not native ASTC'),'No new ten-minute stability/audio/vehicle/GPU proof'],exports=dict(total=len(exports),unavailable=sum(x['export_status']!='verified' for x in exports),all_local_hashes_match=True),decoded_nm2_resources=dict(installed=66 if restored else 0,verified_base_sources=132 if restored else 0,one_empty_base_pair_excluded=restored),captures=frames,shutdown='Owned clean stop, Power down',sha256={f:sha(f) for f in files}),indent=2,ensure_ascii=False))
