/* Own read-only Qt5.4 Media window observation. No setters, injected events or replies. */
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
static int observing(void) {
 static int enabled=-1;
 if(enabled>=0)return enabled;
 char exe[256];ssize_t n=readlink("/proc/self/exe",exe,sizeof(exe)-1);
 if(n<=0)return enabled=0;
 exe[n]=0;
 return enabled=!strcmp(exe,"/app/bin/AppMediaPlayer") && access("/mnt/ca-tools/MEDIA_WINDOW_OBSERVE",R_OK)==0;
}
static const char *class_name(const void *object) {
 typedef const void *(*meta_fn)(const void*);
 typedef const char *(*name_fn)(const void*);
 name_fn name=(name_fn)dlsym(RTLD_NEXT,"_ZNK11QMetaObject9classNameEv");
 if(!object||!name)return "unknown";
 const void *meta=((meta_fn)(*(void ***)object)[0])(object);
 return meta?name(meta):"unknown";
}
static int property_int(const void *object,const char *name) {
 typedef void (*property_fn)(void*,const void*,const char*);
 typedef int (*int_fn)(const void*,_Bool*);
 typedef void (*destroy_fn)(void*);
 property_fn get=(property_fn)dlsym(RTLD_NEXT,"_ZNK7QObject8propertyEPKc");
 int_fn convert=(int_fn)dlsym(RTLD_NEXT,"_ZNK8QVariant5toIntEPb");
 destroy_fn destroy=(destroy_fn)dlsym(RTLD_NEXT,"_ZN8QVariantD1Ev");
 if(!get||!convert||!destroy)return -1;
 union {long double align;unsigned char data[32];} value;
 get(&value,object,name);_Bool ok=0;int result=convert(&value,&ok);destroy(&value);
 return ok?result:-1;
}
static void observe(void *window,const char *phase,unsigned type) {
 static unsigned count;
 if(!observing()||!window||count++>=500)return;
 typedef _Bool (*bool_fn)(const void*);
 bool_fn visible=(bool_fn)dlsym(RTLD_NEXT,"_ZNK7QWindow9isVisibleEv");
 bool_fn exposed=(bool_fn)dlsym(RTLD_NEXT,"_ZNK7QWindow9isExposedEv");
 if(!visible||!exposed)return;
 struct timespec ts={0};clock_gettime(CLOCK_REALTIME,&ts);
 char line[512];int n=snprintf(line,sizeof(line),"MEDIA_WINDOW time=%ld.%09ld phase=%s event=%u object=%p class=%s width=%d height=%d visible=%d exposed=%d visibility=%d\n",(long)ts.tv_sec,ts.tv_nsec,phase,type,window,class_name(window),property_int(window,"width"),property_int(window,"height"),visible(window),exposed(window),property_int(window,"visibility"));
 if(n<=0||(size_t)n>=sizeof(line))return;
 int fd=open("/mnt/ca-output/media-window-observer.txt",O_CREAT|O_APPEND|O_WRONLY,0600);
 if(fd>=0){ssize_t written=write(fd,line,(size_t)n);(void)written;close(fd);}
}
void window_show(void *window) __asm__("_ZN7QWindow4showEv");
void window_show(void *window) {
 typedef void (*show_fn)(void*);static show_fn original;
 if(!original)original=(show_fn)dlsym(RTLD_NEXT,"_ZN7QWindow4showEv");
 if(!original)_exit(126);
 int saved=errno;observe(window,"before-show",0);errno=saved;original(window);saved=errno;observe(window,"after-show",0);errno=saved;
}
_Bool gui_notify(void *app,void *receiver,void *event) __asm__("_ZN15QGuiApplication6notifyEP7QObjectP6QEvent");
_Bool gui_notify(void *app,void *receiver,void *event) {
 typedef _Bool (*notify_fn)(void*,void*,void*);static notify_fn original;
 if(!original)original=(notify_fn)dlsym(RTLD_NEXT,"_ZN15QGuiApplication6notifyEP7QObjectP6QEvent");
 if(!original)_exit(126);
 int saved=errno;
 unsigned type=event?*(uint16_t*)((char*)event+16):0;
 int selected=observing()&&receiver&&(type==14||type==17||type==18||type==206)&&!strcmp(class_name(receiver),"QQuickView");
 if(selected)observe(receiver,"before-event",type);
 errno=saved;
 _Bool result=original(app,receiver,event);saved=errno;
 if(selected)observe(receiver,"after-event",type);
 errno=saved;return result;
}
