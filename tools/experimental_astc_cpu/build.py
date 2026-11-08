#!/usr/bin/env python3
"""Build an opt-in CPU ASTC upload adapter; no firmware or global installation."""
import argparse,hashlib,json,os,subprocess,tarfile,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parent
URL='https://files.pythonhosted.org/packages/d8/25/603483a6c5f0fcd694732cbb079c83a026aa4ff153278a1f400c2bdf65e7/texture2ddecoder-1.0.6.tar.gz'
DIGEST='88f04d8951018ac13b8dacd07e57e8adad4a6f1cfe5509646e8a1020346a81ca'
FILES=['astc.cpp','astc.h','color.h','endianness.h','fp16.h','fp16/fp16.h','fp16/bitcasts.h']
def run(args,**kwargs):subprocess.run(list(map(str,args)),check=True,**kwargs)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-archive',type=Path);p.add_argument('--self-test',action='store_true');a=p.parse_args()
 work=ROOT/'build';work.mkdir(exist_ok=True)
 data=a.source_archive.read_bytes() if a.source_archive else urllib.request.urlopen(URL,timeout=30).read()
 if hashlib.sha256(data).hexdigest()!=DIGEST:raise SystemExit('Source archive SHA-256 mismatch')
 archive=work/'texture2ddecoder-1.0.6.tar.gz';archive.write_bytes(data)
 source=work/'upstream';source.mkdir(exist_ok=True);checks={}
 with tarfile.open(archive) as package:
  for name in FILES+['LICENSE','README.md']:
   member='texture2ddecoder-1.0.6/'+('src/Texture2DDecoder/' if name in FILES else '')+name
   item=package.getmember(member)
   if not item.isfile():raise SystemExit('Unexpected source member type')
   content=package.extractfile(item).read();target=source/name;target.parent.mkdir(parents=True,exist_ok=True)
   if target.exists() and target.read_bytes()!=content:raise SystemExit('Existing upstream source differs: '+name)
   target.write_bytes(content);checks[name]=hashlib.sha256(content).hexdigest()
 combined=work/'adapter.c';combined.write_bytes((ROOT/'native-egl-resolver.c').read_bytes()+(ROOT/'astc-upload-wrapper.c').read_bytes())
 flags=['-O2','-fPIC','-fno-stack-protector','-fno-exceptions','-fno-rtti','-fvisibility=hidden','-I'+str(source)]
 objects=[]
 for path in [source/'astc.cpp',ROOT/'decode-astc-rgba.cpp']:
  obj=work/(path.stem+'.o');run(['g++',*flags,'-c',path,'-o',obj]);objects.append(obj)
 def link(output,extra=()):
  run(['gcc','-O2','-fPIC','-fno-stack-protector','-shared','-nostdlib',*extra,combined,*objects,'-o',output])
  dynamic=subprocess.check_output(['readelf','-d',output],text=True)
  if 'NEEDED' in dynamic:raise SystemExit('Unexpected host runtime dependency')
 output=work/'astc-cpu-upload.so';link(output)
 report={'source_url':URL,'source_archive_sha256':DIGEST,'unmodified_sources':checks,'own_sources':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in ['native-egl-resolver.c','astc-upload-wrapper.c','decode-astc-rgba.cpp']},'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'scope':'Standalone experimental adapter; firmware/runtime must be obtained independently'}
 if a.self_test:
  check=work/'check';mock=work/'libFakeEGL.so';selected=work/'selected';selected.touch()
  run(['gcc','-shared','-fPIC','-Wl,-soname,libEGL.so.1',ROOT/'fixtures/fake_egl.c','-o',mock])
  run(['gcc',ROOT/'fixtures/check.c','-ldl','-o',check])
  test=work/'astc-cpu-upload-test.so'
  link(test,['-DCA_ASTC_TARGET_EXE="'+str(check)+'"','-DCA_ASTC_MARKER="'+str(selected)+'"','-DCA_ASTC_HASH_LIBRARY="/lib/x86_64-linux-gnu/libcrypto.so.3"'])
  for library,mode in [(test,'selected'),(output,'unselected')]:
   env=os.environ.copy();env['LD_PRELOAD']=str(library);run([check,mock,mode],env=env)
  report['host_synthetic_contract_tests']='passed; no OEM application, image or bus used'
 (work/'build-provenance.json').write_text(json.dumps(report,indent=2)+'\n');print(output)
if __name__=='__main__':main()
