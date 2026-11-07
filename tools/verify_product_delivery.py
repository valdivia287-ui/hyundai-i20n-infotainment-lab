#!/usr/bin/env python3
"""Offline checks for a completed private Windows product delivery run.
Requires separately obtained private evidence. Does not launch or control a VM.
"""
import argparse,hashlib,json,re
from pathlib import Path
from PIL import Image,ImageChops,ImageStat

def check(run):
 run=Path(run).resolve();result=json.loads((run/'product-delivery-result.json').read_text())
 assert result.get('ui_sequence_passed') is True and not result.get('error'),'UI sequence incomplete'
 names=['home-ready','menu','nmode','home-after-nmode','radio','home-after-radio','manual','home-after-manual','home-after-final-drag','awaiting-windows-stop']
 checkpoints=[s for s in result['steps'] if 'checkpoint' in s]
 assert [s['checkpoint'] for s in checkpoints]==names,'Incomplete or reordered checkpoints'
 hashes={}
 for step in checkpoints:
  if 'screenshot' not in step:continue
  name=step['screenshot'];assert Path(name).name==name and name.endswith('.png')
  file=run/name
  with Image.open(file) as im:
   assert im.size==(1280,800) and im.convert('RGB').getbbox(),'Empty/invalid screenshot'
   if 'reference' in step:
    reference=Path(step['reference'])
    if not reference.is_absolute():reference=run.parent.parent/reference
    with Image.open(reference) as ref:
     box=(0,100,1280,690);diff=ImageChops.difference(im.convert('RGB').crop(box),ref.convert('RGB').crop(box));r,g,b=diff.split();hist=ImageChops.lighter(ImageChops.lighter(r,g),b).histogram()
     assert sum(hist[9:])/sum(hist)<=.005 and sum(ImageStat.Stat(diff).mean)/3<=.5,'Frame mismatch: '+name
  hashes[name]=hashlib.sha256(file.read_bytes()).hexdigest()
 command=json.loads((run/'command.json').read_text());assert command[command.index('-nic')+1]=='none','Guest network enabled'
 options=json.loads((run/'replay-options.json').read_text());assert options['spanish_eu'] and options['car_type_code']==81 and options['high_performance_car'],'Wrong software identity'
 assert 'reboot: Power down' in (run/'console.log').read_text(errors='replace'),'No clean guest shutdown evidence'
 health=(run/'guest-logs/product-health.txt').read_text();identities={}
 for name,pid,birth in re.findall(r'name=(\S+) pid=(\d+) birth=(\d+)',health):identities.setdefault(name,set()).add((pid,birth))
 assert set(identities)=={'AppLauncher','ApplicationManager','AppHomeScreen','micommanager_userspace','weston'} and all(len(x)==1 for x in identities.values()),'Core identity changed/missing'
 weston=(run/'guest-logs/weston.log').read_text(errors='replace')
 readiness=(run/'guest-logs/home-initial-layout-ready.txt').read_text()
 ready_tick=int(re.search(r'CA_FRAME_PROBE tick=(\d+)',readiness).group(1))
 radio_records=re.findall(r'CA_SURFACE_OWNER tick=(\d+) id=\d+ pid=(\d+) comm=AppEURadio',weston)
 radio_pids={pid for tick,pid in radio_records if int(tick)>=ready_tick}
 assert len(radio_pids)==1,'Original Radio surface owner changed/missing after measured Home readiness'
 startup_radio_pids={pid for tick,pid in radio_records if int(tick)<ready_tick}
 life=json.loads((run/'windows-delivery.json').read_text());assert life['start_mode']=='desktop-shortcut' and life['native_stop_button'] and life['no_owned_orphans'],'Windows lifecycle incomplete'
 mouse=json.loads((run/'native-windows-pointer-validation.json').read_text());assert mouse['transport']=='Windows user32 -> Brave -> noVNC -> QEMU' and mouse['home1_match'] and mouse['home0_match'],'Native browser mouse not verified'
 return {'verified':True,'scope':'Recorded UI/reference pixels, native Windows input and clean-stop evidence; not all apps/hardware/stability','screenshots':hashes,'core_identities':{k:list(v)[0] for k,v in identities.items()},'radio_after_home_readiness':list(radio_pids),'radio_startup_pids':sorted(startup_radio_pids)}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('run',type=Path);a=p.parse_args();print(json.dumps(check(a.run),indent=2))
if __name__=='__main__':main()
