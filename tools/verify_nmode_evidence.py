#!/usr/bin/env python3
"""Offline check of the original integrated N Mode500 cycle; no VM access.
Screen identity is reviewed visually; this tool checks its supporting evidence.
"""
import argparse,hashlib,json,re
from pathlib import Path
from PIL import Image,ImageChops
if not __debug__:raise SystemExit('Run without -O; evidence checks require assertions')
p=argparse.ArgumentParser(description=__doc__);p.add_argument('run',type=Path);a=p.parse_args();r=a.run.resolve()
def txt(n):return (r/n).read_text(errors='replace')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert 'reboot: Power down' in txt('console.log')
assert not (r/'worker-error.log').exists()
assert 'AppKill' not in txt('guest-logs/app-launcher.txt') and 'segfault at' not in txt('console.log')
assert 'int32 1' in txt('guest-logs/audit-before-application500-status.txt')
assert 'int32 500' in txt('guest-logs/audit-after-drawing_application.txt')
assert 'int32 500' in txt('guest-logs/audit-after-appmanager_application.txt')
assert 'id[304] appid[500] reason[5185]' in txt('guest-logs/manager-return.strace')
assert 'requestShow AppId[APP_N_MODE][500]' in txt('guest-logs/manager-return.strace')
trace=txt('guest-logs/audit-nmode.strace')
assert 'NMode/Main_Screen.qml' in trace and 'NMode/Main_Screen_N_Mode.qml' in trace
assert 'original_model_property=0_to1 success=1' in txt('guest-logs/nmode-hmi-capability.txt')
assert '/app/bin/AppHomeScreen: OK' in txt('guest-logs/nmode-home-source-integrity.txt')
assert txt('guest-logs/nmode-observed-source-integrity.txt').count(': OK')==42
assert txt('guest-logs/nmode-observed-output-integrity.txt').count(': OK')==21
assert 'FAILED' not in txt('guest-logs/nmode-observed-source-integrity.txt')
assert not (r/'payload/LAUNCHER_PRELOAD_RADIO').exists()
command=json.loads(txt('command.json'));assert command[command.index('-nic')+1]=='none'
frames=['audit-home-before-nmode.png','operator-nmode-rendered-overview.png','operator-nmode-rendered-gauges.png','operator-nmode-speed-readonly.png','operator-nmode-rendered-native-home-return.png','operator-nmode-rendered-home-page0.png']
for name in frames:
 with Image.open(r/name) as im:assert im.size==(1280,800)
with Image.open(r/frames[-1]) as last,Image.open(r/frames[0]) as first:
 box=ImageChops.difference(last.convert('RGB'),first.convert('RGB')).getbbox()
 assert box is None or (610<=box[0]<=box[2]<=669 and 703<=box[1]<=box[3]<=712)
inputs=[json.loads(line) for line in txt('operator-vnc-input.jsonl').splitlines()]
assert [i['action'] for i in inputs]==['nmode-gauges','nmode-speed','home','drag-right']
intent=txt('guest-logs/oem-layout-intent-observer.txt')
assert len(re.findall(r'^OEM_LAYOUT_INTENT app=11 ',intent,re.M))>=2
assert 'checked=500' in intent or 'drawn=500' in intent
health={}
for line in txt('guest-logs/interactive-health.txt').splitlines():
 d=dict(x.split('=',1) for x in line.split() if '=' in x);h=health.setdefault(d['name'],{'identities':set(),'samples':0,'rss':[]})
 h['identities'].add((int(d['pid']),int(d['birth'])));h['samples']+=1;h['rss'].append(int(d['rss_kib']))
assert len(health)==5 and all(len(h['identities'])==1 for h in health.values())
for h in health.values():
 h['identities']=sorted(h['identities']);v=h.pop('rss');h.update(rss_min_kib=min(v),rss_max_kib=max(v),rss_final_minus_initial_kib=v[-1]-v[0])
exports=[json.loads(line) for line in txt('screenshot-export.jsonl').splitlines()]
for e in exports:assert sha(r/e['source'])==e['source_sha256']
files=frames+['console.log','profile-env.json','command.json','replay-options.json','operator-vnc-input.jsonl','operator-observations.jsonl','guest-logs/audit-before-AppHomeScreen-argv.txt','guest-logs/audit-before-AppHomeScreen-env.txt','guest-logs/audit-before-AppHomeScreen-maps.txt','guest-logs/audit-before-shm.txt','guest-logs/audit-before-sysvipc-shm.txt','guest-logs/audit-nmode.strace','guest-logs/manager-return.strace','guest-logs/nmode-hmi-capability.txt','guest-logs/nmode-observed-source-integrity.txt','guest-logs/nmode-observed-output-integrity.txt','guest-logs/oem-layout-intent-observer.txt','guest-logs/interactive-health.txt','guest-logs/weston.log']
result={'result':'original_integrated_N_Mode500_cycle_verified_with_limits','run':r.name,'native_request':[304,500,5185,1,0],'logical_id':500,'executable':'/app/bin/AppHomeScreen','process_creation':'OEM AppLauncher starts Home; integrated model provides NMode, no separate NMode executable','surface':'IVI1000, original AppHomeScreen owner,1920x720 buffer ->1280x730 destination','screen_review':'Original Spanish N Mode overview with restored main artwork; original Medidores/FuerzaG and Velocidad views selected by VNC. Raw images saved; identity manually reviewed.','return':'Native Home control, original real getters11 and aligned Home, then further VNC page1->0. No lab recovery request or process restart used for this return.','home_page0_diff_bbox':box,'local_adaptations':['Explicit local nModeVariantFlg configuration through original writable Qt property; OEM MICOM/CAN/D-Bus replies and sensors unchanged','Existing BC3 QML override and software/timing/IPC laboratory adaptations preserved; no N Mode QML edited','21 observed original textures decoded to PNG;42 immutable source hashes,21 output hashes and RGBA PNG roundtrip verified; not native ASTC rendering'],'limits':['nm0 integrated/legacy UI. Exact BC3N/nm2 variant remains unverified; guiVariant field must not be confused with nm','Nine additional detail textures were requested and are not included in this21-asset fallback','No physical sensor values; displays remain zero/unavailable. /dev/shm missing in current guest','Constructor hardware requests are not fully captured by this post-initialization trace','No new ten-minute stability claim; no RF/audio/navigation/guestGPU proof'],'argv':txt('guest-logs/audit-before-AppHomeScreen-argv.txt').splitlines(),'health':health,'captures':frames,'exports':{'total':len(exports),'verified':sum(e['export_status']=='verified' for e in exports),'unavailable':sum(e['export_status']!='verified' for e in exports),'all_WSL_hashes_match':True},'shutdown':'Explicit owned stop, Power down, logs recovered','sha256':{name:sha(r/name) for name in files}}
print(json.dumps(result,indent=2,ensure_ascii=False))
