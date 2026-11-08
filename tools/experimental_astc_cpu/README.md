# Experimental CPU ASTC upload adapter

Original lab code for the original Qt applications. It decodes requested ASTC LDR 4×4/6×6 blocks on the CPU and issues native RGBA texture uploads. Hyundai resources, QML, application binaries and the OEM LZ4 loader remain outside this tool. This is CPU decoding, not OEM ASTC rendering or GPU acceleration.

The integrated private AppSetup probe rendered the original Latin-keyboard previews and returned to Home. Its first uploaded resource matched an independent Windows decode by compressed-source and RGBA hashes. All 126 private resource fixtures matched the pinned decoder pixel for pixel on Linux. The standalone library here shares that decoder/upload code and has synthetic host contract tests; integration into an original application environment remains a separate step. Media support has a separate opt-in marker and is under investigation. The BluetoothHMI opt-in restored the original phone illustration in a live native-provider reexec test; its original-source and RGBA hashes matched the pinned decoder. Cold-boot Bluetooth integration is a separate pending check.

## Build

Requirements: x86-64 Linux for the x86-64 guest, Python 3.12+, GCC/G++, readelf. No global installation is performed.

```sh
python3 tools/experimental_astc_cpu/build.py --self-test
```

The build downloads the pinned MIT [texture2ddecoder 1.0.6 source distribution](https://pypi.org/project/texture2ddecoder/1.0.6/) and verifies SHA-256 before extracting selected source files into the ignored `build/` directory. An existing archive can be supplied with `--source-archive`. Build provenance is recorded locally. Synthetic fixtures contain no Hyundai content and never run in QEMU.

## Runtime scope

The library requires an independently prepared original runtime and its already loaded EGL/GLES/OpenSSL libraries. Default selection requires `/app/bin/AppSetup` plus `/run/ca-runtime/SETUP_ASTC_CPU_UPLOAD`, original AppMediaPlayer plus the separate `MEDIA_ASTC_CPU_UPLOAD` marker, or original `/app/bin/BluetoothHMI` plus `BT_ASTC_CPU_UPLOAD`. Other processes and unsupported uploads are forwarded. No marker is installed by the build.

Supported contexts are GLES 2/3 or desktop GL 2.1+. sRGB ASTC, other block sizes, PBO data, nondefault unpack rows/skips, invalid sizes and absent contexts retain the original upload path. RGBA upload alignment is restored. The adapter does not consume or clear GL errors; an issued upload alone does not prove visible UI. Native source/RGBA SHA-256 and renderer observations belong in private logs. Four empty recovered source payloads remain excluded; no pixels are fabricated.

The software lab remains offline and uses disposable overlays. Never inject this library into a vehicle or an accepted profile without separate validation.

## Provenance

The wrapper and C ABI are original lab code. The unmodified decoder comes from [K0lb3/texture2ddecoder](https://github.com/K0lb3/texture2ddecoder), which credits [Ishotihadus/mikunyan ASTC](https://github.com/Ishotihadus/mikunyan) and [FP16](https://github.com/Maratyszcza/FP16). MIT notices are retained here and in the fetched headers. Endianness-header attribution is retained in the source distribution. Decoder code is not claimed as original lab work.
