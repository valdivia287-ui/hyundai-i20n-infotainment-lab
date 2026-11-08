/* Original lab code: resolve already-loaded EGL including RTLD_LOCAL plugins. */
#define _GNU_SOURCE
#include <dlfcn.h>
#include <errno.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/syscall.h>
#include <time.h>
#include <unistd.h>
static void *ca_original_egl_symbol(const char *name)
{
 static void *handle;
 if(!handle)handle=dlopen("libEGL.so.1",RTLD_LAZY|RTLD_NOLOAD);
 if(!handle)handle=dlopen("/usr/lib/libEGL.so.1.0.0",RTLD_LAZY|RTLD_NOLOAD);
 void *symbol=handle?dlsym(handle,name):NULL;
 if(!symbol)symbol=dlsym(RTLD_NEXT,name);
 return symbol;
}
