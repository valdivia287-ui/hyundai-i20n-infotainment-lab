/* Synthetic host-only EGL/GLES contract fixture; never shipped into QEMU. */
#include <string.h>
#include <stdint.h>
static int compressed,images,alignment=8,last_level,pbo,context=1,row_length;
static unsigned last_format;static const void *last_data;static unsigned char pixels[128];
void reset_fixture(void){compressed=images=0;alignment=8;last_level=-1;last_format=0;last_data=0;pbo=0;context=1;row_length=0;}
void set_case(int value){if(value==1)pbo=3;else if(value==2)context=0;else if(value==3)row_length=7;}
int check_fixture(int mode){if(mode==1)return images==1&&compressed==0&&alignment==8&&last_level==2&&pixels[0]==255&&pixels[1]==0&&pixels[2]==0&&pixels[3]==255&&pixels[20]==255&&pixels[23]==255;return compressed==1&&images==0&&alignment==8;}
unsigned eglMakeCurrent(void*d,void*w,void*r,void*c){return 27;}
unsigned eglSwapInterval(void*d,int i){return 31+i;}
void *eglGetCurrentContext(void){return context?(void*)1:0;}
static void native_compressed(unsigned t,int l,unsigned f,int w,int h,int b,int n,const void*d){compressed++;last_format=f;last_data=d;last_level=l;}
static void native_image(unsigned t,int l,int f,int w,int h,int b,unsigned fmt,unsigned type,const void*d){images++;last_level=l;if(w*h*4<=128)memcpy(pixels,d,w*h*4);}
static const unsigned char *native_string(unsigned token){return (const unsigned char*)(token==0x1f02?"OpenGL ES 3.0 host contract fixture":token==0x1f01?"Synthetic host fixture":"");}
static void native_get(unsigned token,int*v){*v=token==0x0cf5?alignment:token==0x0d33?4096:token==0x88ef?pbo:token==0x0cf2?row_length:0;}
static void native_store(unsigned token,int v){if(token==0x0cf5)alignment=v;}
void *eglGetProcAddress(const char*n){if(!strcmp(n,"glCompressedTexImage2D"))return native_compressed;if(!strcmp(n,"glTexImage2D"))return native_image;if(!strcmp(n,"glGetString"))return native_string;if(!strcmp(n,"glGetIntegerv"))return native_get;if(!strcmp(n,"glPixelStorei"))return native_store;return 0;}
