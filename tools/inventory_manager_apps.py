#!/usr/bin/env python3
"""Read-only manager table inventory from separately supplied original ELF/disassembly.
Recognizes reviewed QString assignments plus adjacent ID/flags; never executes OEM code.
Output metadata remains private. Labels are logical app IDs, not executable launch entries.
"""
import argparse,hashlib,json,re,struct
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('elf',type=Path);p.add_argument('disassembly',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
b=a.elf.read_bytes();assert b[:6]==b'\x7fELF\x02\x01'
if hashlib.sha256(b).hexdigest()!='5d71539f61a3982b8aac6132a2de14c083fa9ac129792bae750a526ebd771cbc':raise SystemExit('Unreviewed manager build: verify constructor address/layout before adapting this parser')
po=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54)
segments=[struct.unpack_from('<IIQQQQQQ',b,po+i*es) for i in range(n)]
def string(addr):
 for t,f,o,v,_,size,mem,align in segments:
  if t==1 and v<=addr<v+size:
   start=o+addr-v;end=b.find(b'\0',start,start+160)
   if end<0:return ''
   try:return b[start:end].decode('ascii')
   except UnicodeDecodeError:return ''
 return ''
strings={};ints={};rsi=None;rdi=None;recent=0
for line in a.disassembly.open():
 m=re.match(r'\s*([0-9a-f]+):\s',line)
 if not m:continue
 addr=int(m[1],16);recent+=1
 z=re.search(r'lea\s+.*%rsi\s+#\s*([0-9a-f]+)',line)
 if z:rsi=(string(int(z[1],16)),recent,addr)
 z=re.search(r'lea\s+.*%rdi\s+#\s*([0-9a-f]+)',line)
 if z:rdi=(int(z[1],16),recent)
 z=re.search(r'movl\s+\$0x([0-9a-f]+),.*\(%rip\).*#\s*([0-9a-f]+)',line)
 if z:ints[int(z[2],16)]=int(z[1],16)
 if re.search(r'call\s+178160\b',line) and rsi and rdi and recent-rsi[1]<14 and recent-rdi[1]<14:
  strings[rdi[0]]=(rsi[0],rsi[2]);rsi=rdi=None
rows={}
for dest,(name,addr) in strings.items():
 label=strings.get(dest+8,('',0))[0];app_id=ints.get(dest+16)
 if not label.startswith('APP_') or not name or not app_id or app_id>10000:continue
 key=(app_id,label,name);row=rows.setdefault(key,dict(app_id=app_id,label=label,provider_name=name,flags_raw=ints.get(dest+20),mask_raw=ints.get(dest+24),initializer_addresses=[]));row['initializer_addresses'].append(hex(addr))
result=dict(source_sha256=hashlib.sha256(b).hexdigest(),method='Original manager static constructor: provider QString at row+0, APP label QString at+8, immediate logical ID at+16; raw fields+20/+24 retained without invented semantics. Repeated tables deduplicated.',limits='Static metadata, not runtime registration, executable presence, safety or completeness proof. Launcher parser pattern produced zero rows for this different layout; no inference of absent apps.',rows=sorted(rows.values(),key=lambda x:(x['app_id'],x['label'],x['provider_name'])))
a.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');print('Manager logical entries:',len(rows))
for row in result['rows']:print(row['app_id'],row['label'],row['provider_name'])
