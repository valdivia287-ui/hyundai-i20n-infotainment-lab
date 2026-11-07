#!/usr/bin/env python3
"""Offline supporting checks for the visually reviewed original fitted Voice Memo cycle.
No VM/input/OEM execution. Screen identity still requires separate visual review.
"""
import argparse,hashlib,json,re
from pathlib import Path
from PIL import Image,ImageChops
if not __debug__:raise SystemExit('Evidence checks require Python without -O')
p=argparse.ArgumentParser(description=__doc__);p.add_argument('run',type=Path);a=p.parse_args();r=a.run.resolve()
def txt(name):return (r/name).read_text(errors='replace')
def sha(name):return hashlib.sha256((r/name).read_bytes()).hexdigest()
result=json.loads(txt('app-audit-result.json'))
assert result['cycle_verified'] is True
for name,digest in result['sha256'].items():
 path=(r/name).resolve();assert path.is_relative_to(r) and path.is_file();assert sha(name)==digest
assert 'reboot: Power down' in txt('console.log') and not (r/'worker-error.log').exists()
assert 'AppKill' not in txt('guest-logs/app-launcher.txt')
command=json.loads(txt('command.json'));assert command[command.index('-nic')+1]=='none'
manager=txt('guest-logs/audit-manager.strace')
for marker in ['appid[117] reason[28]','requestShow AppId[APP_VOICE_MEMO][117]','ask_drawing_application ret[117]','handleBackKey eventId[3] appId[117] reason[1]','GoXXXBackDefault::calcHistory plan[1] AppId[11]']:assert marker in manager
assert 'OEM_LAYOUT_INTENT app=117 source=three_real_getters' in txt('guest-logs/oem-layout-intent-observer.txt')
layout=txt('guest-logs/weston.log');fit=re.search(r'CA_ACTIVE_MEDIA_GEOMETRY_FIT id=(\d+) manager_agreed=117 from=1920x720 to=1280x730 output=1280x800',layout);assert fit
sid=int(fit[1]);owner=re.search(r'CA_SURFACE_OWNER tick=\d+ id='+str(sid)+r' pid=(\d+) comm=AppMediaPlayer',layout);assert owner;pid=int(owner[1])
assert re.search(r'CA_FRAME_PROBE tick=\d+ id='+str(sid)+r' layer=102 visible=1 layer_visible=1 buffer=1920x720 dest=0,0,1280,730',layout)
assert 'class=QQuickView width=1920 height=720 visible=1 exposed=1' in txt('guest-logs/media-window-observer.txt')
trace=txt('guest-logs/audit-launcher-child.strace');assert re.search(r'open\("/app/share/AppMediaPlayer/res/languages/AppMediaPlayer_es_ES.qm".*\) = \d+',trace)
assert 'Screen_VoiceMemoRecorder.qml' in txt('guest-logs/audit-voice-memo-runtime.strace')
argv=txt('guest-logs/audit-voice-memo-'+str(pid)+'-argv.txt').splitlines();assert argv[0]=='/app/bin/AppMediaPlayer' and '-cv:5' in argv and '-l:7' in argv
health=txt('guest-logs/audit-voice-memo-process-health.txt');identities=set(re.findall(r'pid=(\d+) birth=(\d+)',health));assert len(identities)==1 and next(iter(identities))[0]==str(pid)
actions=[json.loads(l)['action'] for l in txt('operator-vnc-input.jsonl').splitlines()];assert actions==['drag-left','voice-memo','media-back','drag-right']
prefix='voice-art' if (r/'operator-voice-art-native-complete.png').is_file() else 'voice-fit'
frames=['audit-home-before-voice-memo.png','operator-'+prefix+'-native-complete.png','operator-'+prefix+'-native-home-return.png','operator-'+prefix+'-home0-after-return.png']
if prefix=='voice-art' and (r/'operator-voice-art-native-late.png').is_file():frames[1]='operator-voice-art-native-late.png'
ims=[]
for name in frames:
 with Image.open(r/name) as im:assert im.size==(1280,800);ims.append(im.convert('RGB'))
box=ImageChops.difference(ims[0],ims[-1]).getbbox();assert box is None or (610<=box[0]<=box[2]<=669 and 703<=box[1]<=box[3]<=712)
assert ImageChops.difference(ims[0],ims[1]).getbbox() is not None
exports=[json.loads(l) for l in txt('screenshot-export.jsonl').splitlines()]
for e in exports:assert sha(e['source'])==e['source_sha256']
resources=(r/'payload/MEMO_PNG_FALLBACK').is_file()
if resources:
 assert txt('guest-logs/memo-observed-source-integrity.txt').count(': OK')==70
 assert txt('guest-logs/memo-observed-output-integrity.txt').count(': OK')==35
 assert 'CA_MEMO_OBSERVED_PNG_READY count=35' in txt('guest-logs/memo-observed-setup.txt')
print(json.dumps(dict(result='Supporting original VoiceMemo117 fitted UI/Back/Home cycle checks passed; visual review mandatory',run=r.name,owner=dict(pid=pid,surface=sid),original_open=[304,117,28,1,0],original_back=[3,117,1,1,0],process_identity=sorted(identities),final_home_diff_bbox=box,exports=dict(total=len(exports),unavailable=sum(e['export_status']!='verified' for e in exports),all_local_hashes_match=True),decoded_extra_memo_resources=35 if resources else 0,captures={name:sha(name) for name in frames},limits=['Qtwindow observer active; timing influence not isolated','UI roundtrip only; no recording/playback/deletion/audio proof','OEM bootCarType fixture0/LX2; targetBC3N MY23 Spain/Europe not full vehicle emulation','No new ten-minute stability or full-system completion claim']),ensure_ascii=False,indent=2))
