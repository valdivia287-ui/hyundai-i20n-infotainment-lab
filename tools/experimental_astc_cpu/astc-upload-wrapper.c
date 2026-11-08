/* Own opt-in CPU adaptation; leaves original compressed files intact.
 * Explicit per-application RAM markers; native EGL/GLES calls and errors retained.
 * Linked after the existing probe C source, whose native EGL resolver is reused. */
#include <stdlib.h>
#ifndef CA_ASTC_TARGET_EXE
#define CA_ASTC_TARGET_EXE "/app/bin/AppSetup"
#endif
#ifndef CA_ASTC_MARKER
#define CA_ASTC_MARKER "/run/ca-runtime/SETUP_ASTC_CPU_UPLOAD"
#endif
#ifndef CA_ASTC_HASH_LIBRARY
#define CA_ASTC_HASH_LIBRARY "/lib/libcrypto.so.1.0.2"
#endif
extern int ca_decode_astc_rgba(const unsigned char*,size_t,int,int,int,int,unsigned char*,size_t);
static int ca_astc_selected(void)
{
 char path[512];ssize_t n=readlink("/proc/self/exe",path,sizeof(path)-1);
 if(n<=0)return 0;path[n]=0;
 if(!strcmp(path,CA_ASTC_TARGET_EXE))return access(CA_ASTC_MARKER,R_OK)==0;
 if(!strcmp(path,"/app/bin/AppMediaPlayer"))return access("/run/ca-runtime/MEDIA_ASTC_CPU_UPLOAD",R_OK)==0;
 if(!strcmp(path,"/app/bin/BluetoothHMI"))return access("/run/ca-runtime/BT_ASTC_CPU_UPLOAD",R_OK)==0;
 return 0;
}
static void *ca_astc_native_gl(const char *name)
{
 typedef void *(*proc_fn)(const char*);
 proc_fn proc=(proc_fn)ca_original_egl_symbol("eglGetProcAddress");
 void *result=proc?proc(name):NULL;
 if(!result)result=dlsym(RTLD_NEXT,name);
 return result;
}
static void ca_astc_hash_hex(const unsigned char *digest,char text[65])
{
 const char *hex="0123456789abcdef";
 for(int i=0;i<32;i++){text[i*2]=hex[digest[i]>>4];text[i*2+1]=hex[digest[i]&15];}text[64]=0;
}
static void ca_astc_upload_log(int level,unsigned int format,int w,int h,int block,size_t size,const char *raw,const char *rgba,const char *renderer)
{
 int saved=errno;struct timespec ts={0};syscall(SYS_clock_gettime,CLOCK_REALTIME,&ts);
 char line[640];int n=snprintf(line,sizeof(line),"ASTC_CPU_UPLOAD realtime=%ld.%09ld pid=%ld level=%d format=0x%x dimensions=%dx%d block=%d source_bytes=%zu raw_sha256=%s rgba_sha256=%s native_rgba_upload_issued=1 no_error_cleared=1 renderer=%.80s\n",(long)ts.tv_sec,ts.tv_nsec,(long)getpid(),level,format,w,h,block,size,raw,rgba,renderer?renderer:"unknown");
 int fd=open("/mnt/ca-output/astc-cpu-upload.txt",O_WRONLY|O_APPEND|O_CREAT,0600);
 if(fd>=0){if(n>0&&(size_t)n<sizeof(line)){ssize_t written=write(fd,line,(size_t)n);(void)written;}close(fd);}errno=saved;
}
void glCompressedTexImage2D(unsigned int target,int level,unsigned int format,int w,int h,int border,int size,const void *data)
{
 typedef void (*compressed_fn)(unsigned int,int,unsigned int,int,int,int,int,const void*);
 compressed_fn original=(compressed_fn)ca_astc_native_gl("glCompressedTexImage2D");
 if(!original||original==glCompressedTexImage2D)_exit(126);
 int initial_errno=errno;
 int block=format==0x93b0?4:format==0x93b4?6:0;
 if(!ca_astc_selected()||!block||target!=0x0de1||level<0||level>31||border||w<1||h<1||w>4096||h>4096||size<=0||!data||(uintptr_t)data<4096)goto forward;
 size_t blocks_x=((size_t)w+block-1)/block,blocks_y=((size_t)h+block-1)/block;
 if(blocks_x*blocks_y*16!=(size_t)size)goto forward;
 typedef void *(*current_fn)(void);current_fn current=(current_fn)ca_original_egl_symbol("eglGetCurrentContext");
 if(!current||!current())goto forward;
 typedef const unsigned char *(*string_fn)(unsigned int);
 typedef void (*get_fn)(unsigned int,int*);typedef void (*store_fn)(unsigned int,int);
 typedef void (*image_fn)(unsigned int,int,int,int,int,int,unsigned int,unsigned int,const void*);
 string_fn get_string=(string_fn)ca_astc_native_gl("glGetString");get_fn get=(get_fn)ca_astc_native_gl("glGetIntegerv");store_fn store=(store_fn)ca_astc_native_gl("glPixelStorei");image_fn image=(image_fn)ca_astc_native_gl("glTexImage2D");
 if(!get_string||!get||!store||!image)goto forward;
 const char *version=(const char*)get_string(0x1f02);if(!version)goto forward;
 int es2=!strncmp(version,"OpenGL ES 2.",12),es3=!strncmp(version,"OpenGL ES 3.",12);
 if(!es2&&!es3){int major=0,minor=0;if(sscanf(version,"%d.%d",&major,&minor)!=2||major<2||major>4||(major==2&&minor<1))goto forward;}
 const char *extensions=es2?(const char*)get_string(0x1f03):"";
 int pbo=0,row=0,skip_rows=0,skip_pixels=0,alignment=0,max_size=0;
 if(!es2||(extensions&&(strstr(extensions,"GL_NV_pixel_buffer_object")||strstr(extensions,"GL_EXT_pixel_buffer_object"))))get(0x88ef,&pbo);
 if(!es2||(extensions&&strstr(extensions,"GL_EXT_unpack_subimage"))){get(0x0cf2,&row);get(0x0cf3,&skip_rows);get(0x0cf4,&skip_pixels);}
 get(0x0cf5,&alignment);get(0x0d33,&max_size);
 if(pbo||row||skip_rows||skip_pixels||!(alignment==1||alignment==2||alignment==4||alignment==8)||w>max_size||h>max_size)goto forward;
 typedef unsigned char *(*hash_fn)(const unsigned char*,size_t,unsigned char*);
 static void *crypto; if(!crypto)crypto=dlopen(CA_ASTC_HASH_LIBRARY,RTLD_LAZY|RTLD_NOLOAD);
 hash_fn hash=crypto?(hash_fn)dlsym(crypto,"SHA256"):NULL;if(!hash)goto forward;
 size_t bytes=(size_t)w*h*4;unsigned char *pixels=malloc(bytes);if(!pixels)goto forward;
 if(!ca_decode_astc_rgba(data,size,w,h,block,block,pixels,bytes)){free(pixels);goto forward;}
 unsigned char raw_digest[32],rgba_digest[32];char raw_hex[65],rgba_hex[65];
 if(!hash(data,size,raw_digest)||!hash(pixels,bytes,rgba_digest)){free(pixels);goto forward;}
 ca_astc_hash_hex(raw_digest,raw_hex);ca_astc_hash_hex(rgba_digest,rgba_hex);
 errno=initial_errno;if(alignment!=1)store(0x0cf5,1);
 image(target,level,0x1908,w,h,0,0x1908,0x1401,pixels);
 if(alignment!=1)store(0x0cf5,alignment);
 free(pixels);
 ca_astc_upload_log(level,format,w,h,block,size,raw_hex,rgba_hex,(const char*)get_string(0x1f01));return;
forward:
 errno=initial_errno;original(target,level,format,w,h,border,size,data);
}
void *eglGetProcAddress(const char *name)
{
 typedef void *(*fn)(const char*);fn original=(fn)ca_original_egl_symbol("eglGetProcAddress");
 if(!original)_exit(126);
 void *result=original(name);
 if(result&&name&&!strcmp(name,"glCompressedTexImage2D")&&ca_astc_selected())return (void*)glCompressedTexImage2D;
 return result;
}
