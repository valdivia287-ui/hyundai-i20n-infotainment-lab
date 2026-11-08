// Own bounded C ABI over pinned MIT upstream ASTC decoder; no OEM content.
#include <stddef.h>
#include <stdint.h>
#include "astc.h"
extern "C" __attribute__((visibility("default")))
int ca_decode_astc_rgba(const unsigned char *data,size_t size,int w,int h,int bx,int by,unsigned char *rgba,size_t rgba_size)
{
 if(!data||!rgba||w<1||h<1||w>4096||h>4096||!((bx==4&&by==4)||(bx==6&&by==6)))return 0;
 size_t bytes=(size_t)w*h*4;
 size_t blocks_x=((size_t)w+bx-1)/bx,blocks_y=((size_t)h+by-1)/by;
 size_t blocks=blocks_x*blocks_y*16;
 if(size!=blocks||rgba_size!=bytes)return 0;
 if(!decode_astc(data,w,h,bx,by,(uint32_t*)rgba))return 0;
 for(size_t i=0;i<bytes;i+=4){unsigned char b=rgba[i];rgba[i]=rgba[i+2];rgba[i+2]=b;}
 return 1;
}
