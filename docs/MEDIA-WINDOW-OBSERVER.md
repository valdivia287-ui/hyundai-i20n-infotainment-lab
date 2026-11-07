# Read-only MediaPlayer Qt window observer

`tools/media_window_observer.c` is original laboratory diagnostic code for the reviewed x86-64 Qt5.4.1 userspace. It contains no Qt/Hyundai implementation, private capture or resources. It interposes original `QWindow::show()` and `QGuiApplication::notify()`, forwards to the original methods, preserves their result and errno, and logs selected window geometry/visibility/exposure observations. It calls getters, never setters, and supplies no hardware, D-Bus or application-state replies.

```sh
cc -Wall -Wextra -Werror -O2 -fPIC -shared -nostdlib tools/media_window_observer.c -o /tmp/media-window-observer.so
readelf -V /tmp/media-window-observer.so
```

The reviewed build has no symbol-version requirements introduced by host startup objects. Runtime libc and Qt symbols must still match the original guest; this is not a generic Qt6 or cross-architecture tool. QEvent layout and QObject vtable assumptions are specific to the reviewed Qt5.4 ABI. Unknown builds require separate review.

Compilation does not start firmware or install anything. Integrate only through the existing private original-launcher workflow, in a new offline disposable overlay, preserving other preloads. Observation requires exact executable `/app/bin/AppMediaPlayer` and the explicit lab marker `/mnt/ca-tools/MEDIA_WINDOW_OBSERVE`. The existing `/mnt/ca-output` directory receives at most500 observation lines. No data is sent outside the guest. Other original Qt processes are forwarded without collecting their window state.

The private successful UI trial combined this source with an existing lab capability module whose behavior on Home was held constant. The observer is published separately; it is not a replacement HMI, MediaPlayer service or turnkey emulator. Its extra getter calls and logging can change timing. One original Voice Memo UI round trip appeared under instrumentation after earlier trials lacked a buffer; that correlation is **not an established causal fix or reproducibility claim**. Keep uninstrumented controls and original evidence private.
