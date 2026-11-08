/* Own synthetic ABI test. No OEM application, asset, RPC or compositor. */
#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char**argv){
 if(argc!=3)return 2;void*h=dlopen(argv[1],RTLD_NOW|RTLD_LOCAL);if(!h){puts(dlerror());return 3;}
 if(!dlopen("/lib/x86_64-linux-gnu/libcrypto.so.3",RTLD_NOW|RTLD_GLOBAL))return 4;
 void(*reset)(void)=dlsym(h,"reset_fixture");void(*setcase)(int)=dlsym(h,"set_case");int(*check)(int)=dlsym(h,"check_fixture");
 typedef void(*compressed_fn)(unsigned,int,unsigned,int,int,int,int,const void*);typedef void*(*proc_fn)(const char*);
 proc_fn proc=dlsym(RTLD_DEFAULT,"eglGetProcAddress");compressed_fn direct=dlsym(RTLD_DEFAULT,"glCompressedTexImage2D");if(!proc||!direct)return 5;
 unsigned char astc[16]={0xfc,0xfd,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0,0,0,0,0xff,0xff};
 int selected=!strcmp(argv[2],"selected");compressed_fn fn=(compressed_fn)proc("glCompressedTexImage2D");reset();fn(0x0de1,2,0x93b0,3,2,0,16,astc);if(!check(selected?1:0)){puts("FAIL pixel/upload/alignment/forwarding");return 6;}
 reset();direct(0x0de1,2,0x93b0,3,2,0,15,astc);if(!check(0))return 7;
 reset();direct(0x0de1,2,0x93d0,3,2,0,16,astc);if(!check(0))return 8;
 if(selected){reset();setcase(1);direct(0x0de1,2,0x93b0,3,2,0,16,(void*)0x8000);if(!check(0))return 9;
 reset();setcase(2);direct(0x0de1,2,0x93b0,3,2,0,16,astc);if(!check(0))return 10;
 reset();setcase(3);direct(0x0de1,2,0x93b0,3,2,0,16,astc);if(!check(0))return 11;}
 printf("ASTC_HOST_CONTRACT_PASS selected=%d rgba_color=verified mip_level2_preserved=1 alignment8_restored=1 invalid_and_srgb_forwarded=1 pbo_context_row_guards=1 no_OEM=1\n",selected);return 0;
}
