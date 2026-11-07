#!/usr/bin/env python3
"""Static offline inventory: original launcher initializers, never execute OEM code.
Writes private metadata only to the requested independent output directory.
"""
import argparse,hashlib,json,re,struct,subprocess
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('launcher',type=Path);p.add_argument('base',type=Path);p.add_argument('output',type=Path);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
b=a.launcher.read_bytes()
if b[:6]!=b'\x7fELF\x02\x01':raise SystemExit('Expected little-endian ELF64')
phoff=struct.unpack_from('<Q',b,32)[0];phents,phnum=struct.unpack_from('<HH',b,54)
segments=[struct.unpack_from('<IIQQQQQQ',b,phoff+i*phents) for i in range(phnum)]
def cstring(addr):
 for typ,flags,fo,va,_,fs,ms,al in segments:
  if typ==1 and va<=addr<va+fs:
   off=fo+addr-va;end=b.find(b'\0',off,off+500)
   if end<0:return ''
   try:return b[off:end].decode('ascii')
   except UnicodeDecodeError:return ''
 return ''
asm=subprocess.check_output(['objdump','-d','-C','--no-show-raw-insn',str(a.launcher)],text=True).splitlines()
entries={};last_string='';last_addr=''
for i,line in enumerate(asm):
 m=re.search(r'^\s*([0-9a-f]+):.*lea\s+.*%rsi\s+#\s*([0-9a-f]+)',line)
 if m:last_addr=m[1];last_string=cstring(int(m[2],16))
 m=re.search(r'movl\s+\$0x([0-9a-f]+),.*\(%rip\)',line)
 if not m or not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]{2,45}',last_string):continue
 name=last_string;app_id=int(m[1],16)
 if not 0<app_id<10000:continue
 for later in asm[i+1:i+14]:
  z=re.search(r'lea\s+.*%rsi\s+#\s*([0-9a-f]+)',later)
  if not z:continue
  exe=cstring(int(z[1],16))
  if exe.startswith(('/app/bin/','/navi/')) and Path(exe).name==name:
   key=(name,app_id,exe);entry=entries.setdefault(key,{'name':name,'app_id':app_id,'executable':exe,'initializer_addresses':[]})
   entry['initializer_addresses'].append(last_addr)
  break
safe={'AppHomeScreen','AppStandbyClock','AppEURadio','AppMediaPlayer','AppProjection','BluetoothHMI','AppAssistantWindow'}
hardware={'AppRadio','AppXMAudio','AppXMData','AppHDData','AppMobileTV','AppCamera','AppClimate','AppMirrorLink','AppCarLife','AppPHEV','AppFCEV','AppRSPA','AppVH','AppSDS','AppVR','AppNavi','TmsFgApp','TmsGuiApp','TmsVcrmApp'}
internal={'ApplicationManager','AppLauncher','AppOSDManager','AppDMClient'}
for entry in entries.values():
 name=entry['name'];entry.update(status='no probada',ivi_surface=None,missing_dependencies=[],requested_services=[],interaction='no comprobada',return_home='no comprobado',evidence=[],capture=None)
 if re.search(r'Test|Engineer|Diag|Update|Flash|Fumo|FUMO',name):entry.update(category='excluida',reason='Vehicle diagnostic, engineering or update path; never run')
 elif name=='AppGPS':entry.update(category='revisión necesaria',reason='Receiver-control behavior unknown; review before execution')
 elif name=='AppSetup':entry.update(category='revisión necesaria',reason='Can change persistent settings; review original handlers before execution')
 elif name in internal:entry.update(category='servicio interno',reason='Manager/background service; not a standalone user application')
 elif name in safe:entry.update(category='gráfica candidata offline',reason='Basic passive GUI only; no settings writes, pairing or hardware control authorized by this classification')
 elif name in hardware:entry.update(category='dependiente de hardware',reason='Requires application-specific contract and safety review before runtime')
 else:entry.update(category='revisión necesaria',reason='Unknown side effects; do not execute on name alone')
 if entry['category'] in ['excluida','servicio interno']:entry['status']='excluida'
listed=subprocess.check_output(['debugfs','-R','ls -p /app/bin',str(a.base)],stderr=subprocess.DEVNULL,text=True)
(a.output/'app-bin-list.txt').write_text(listed)
excluded=[]
for line in listed.splitlines():
 fields=line.split('/')
 if len(fields)>6 and re.search(r'updat|flash|diag|testagent|engineer|install|erase|fumo|scomo',fields[5],re.I):excluded.append({'name':fields[5],'reason':'Conservative exclusion: update/flashing/diagnostic/install/erase utility; not executed'})
result={'source_sha256':hashlib.sha256(b).hexdigest(),'method':'ELF64 PT_LOAD strings plus x86-64 initializer: name QString, adjacent immediate app ID, matching executable QString. Repeated tables deduplicated; initializer addresses retained. Static registration does not prove launch eligibility.','registered':sorted(entries.values(),key=lambda x:(x['app_id'],x['name'])),'excluded_utilities':excluded,'scope_limit':'Launcher tables only. Logical in-process Home app IDs, manager registrations, original QML and SQLite require separate correlation; no completeness claim yet.'}
(a.output/'launcher-inventory.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('Static launcher entries:',len(entries),'Excluded utilities:',len(excluded))
for entry in result['registered']:print(entry['app_id'],entry['name'],entry['category'])
