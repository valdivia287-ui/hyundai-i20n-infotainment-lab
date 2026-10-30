# Research status — 30 October 2026

**Experimental, isolated QEMU/Weston/Wayland IVI Hyundai i20 N infotainment laboratory.** The original Home interface has now **navigated from page 0 to 1** in a private test reported by Codex running **GPT-6 Sol Alto**. The overall OEM multimedia is **not yet complete**, and other applications have not been proven to launch. See the [latest integrated GL/WM checkpoint](PROGRESS-2026-10-30-GL-INTEGRATION.md), [30 October progress](PROGRESS-2026-10-30.md) and [AI handoff](AI-HANDOFF.md).

> Evidence qualification: the findings below are based on progress logs and screenshots supplied by the owner; the underlying private VM, complete traces and diffs have not been independently inspected for this public report.

## Working foundation

- Original Hyundai `AppHomeScreen` and Qt 5.4.1 run in a disposable Linux/QEMU guest with Weston/Wayland IVI. Original OEM QML and recovered assets were loaded in guest overlays, leaving the base firmware untouched.
- AppHomeScreen rendered a partial genuine UI, later fullscreen; Codex reported stable screenshots at **110s** and **170s**, with **929,959 pixels** differing from the Weston reference. An earlier disappearing Home panel was explained by a **125-second test timeout**.
- Vehicle variant **BC3 = 23** was measured in original QML. A controlled overlay test changed active value from 5 to 23, added a third Home page indicator and saved the value in SQLite. This did not itself establish page navigation.
- Original application created SQLite tables (`MenuHome`: 3 rows; `CustomLayoutFront`: 25). Outgoing D-Bus header analysis identified **47 distinct calls**, including 12 appmanager registrations and 104 requests for unavailable MICOM; those are attempted calls, **not successful responses**.
- Localization remains incomplete: an English `.qm` file was found, but reading active language through shared memory failed. Some translation keys appear untranslated.

## 30 October: input and navigation breakthrough

1. The original `ivi-input-controller.so` was loaded in an isolated guest, and a lab utility confirmed `ivi_input` seat `default` acceptance for Home surface ID **0** on a retry.
2. Weston was initially directing touch toward a **reference interface surface IVI 2001** (`wl_surface@42`), not Home. Terminating only the auxiliary reference UI within a disposable guest removed that input blocker; simply hiding it had not sufficed.
3. After waiting for Home to be ready, the original client trace recorded **`wl_touch.down`, motions and `up`**. This was real delivery to the OEM client, not just the Linux kernel. The touch event by itself did not change the QML page index.
4. A pointer drag reached Home but original input-controller coordinates appeared unexpectedly small. Codex compared the original controller with a separate, **experimental, lab-built IVI controller based on public COVESA sources** and reported corrected pointer motion from approximately x=1430 to x=422. Provenance/licensing of any borrowed code needs an audit before publication.
5. The original QML then reported **`onMovingChanged: true`**, **`onFlickStarted`** and **`advancedModePageChange(1)`**; a captured frame reportedly showed **Home page 1**. These three pieces of evidence support an actual **page 0→1 navigation event** using the original Home application.
6. A subsequent click on an application icon reached the Home surface, but the screen stayed on Home. **Later, Codex running GPT-6 Astra Medio traced the N Mode icon press into the original Home application and reported an application-launch request with `appid=500`.** The lab's D-Bus service **`com.lge.hyundai.avn.appmanager` is missing/not registered**, so that target application does not open. This establishes a concrete app-manager launch blocker, **not** a working N Mode implementation.
7. Codex's selected model subsequently displayed **“Selected model is at capacity”**. This is a capacity limitation and does not establish that user credits were exhausted.

## Astra follow-up checkpoint (30 October)

- In a reported **1 min 57 s** Codex run under **GPT-6 Astra Medio**, the program identified the `appid=500` → missing appmanager-service dependency.
- Codex reported **8 passing checks, 281 verified hashes**, clean VM shutdown, preserved disposable overlays and logs.
- The option to try the **original Hyundai ApplicationManager** was prepared at this stage; **three subsequent QEMU experiments have now run it**, as described below.
- Local private files named in the Codex report: `ESTADO-PROYECTO.md` and `investigacion/nmode-click-20261030.md`; only their names and the report text are available to this public snapshot.

## Latest: real ApplicationManager and OEM IVI window manager trials

The owner has now provided Codex's detailed 30 October notes for **three new disposable-overlay executions**, each stopped normally with logs retained:

- **Manager startup:** the actual OEM ApplicationManager connects to Wayland, but exits during initialization.
- **D-Bus registration and failure:** the session bus registers, then loses **`com.lge.hyundai.avn.appmanager`**; recorded `SIGSEGV / SEGV_MAPERR` at null address after enumerating Wayland globals. Its own error handler attempted `addr2line` and exited with code 1. This was **not** a test timeout; no precise cause/instruction is yet established.
- **OEM window manager experiment:** adding `ivi-window-manager.so` in a **temporary** Weston module configuration starts `early-background`, then Weston aborts in `pixman-renderer.c:277` at `composite_clipped: Assertion src_format failed` (DRM-backend stack).
- The binary's references to `ivi_info_requester` / `ivi_window_manager` are useful leads for compositor protocol compatibility, **not proven explanations** for the null access. Likewise, MICOM/shared-memory/persistence warnings are not yet shown to cause it.
- Lab-only changes reported in `guest/guest-session.sh`, `host/worker.py`; **`CA_IVI_ORIGINAL_WM=1` defaults to off**, preserving the known working Home path.

**No original secondary app has opened yet.** First isolate the Pixman offending buffer/client and inspect the precise manager fault. See [30 October progress](PROGRESS-2026-10-30.md) for run IDs and bounded testing sequence.

## Newest completed-run checkpoint: GL/WM integration (30 October, later runs)

The owner supplied a read-only tracking package of completed tests, allowing more precise assessment than the earlier reports. See the [detailed sanitized progress report](PROGRESS-2026-10-30-GL-INTEGRATION.md).

- **Pixman + OEM WM:** an ARGB8888 `wl_shm` buffer of **1926 × 753** was attached immediately before Weston aborted at `composite_clipped: Assertion src_format failed`. The **actual failing Pixman image/surface has not been identified**. A Wayland SHM format value of 0 is **not** proof of an invalid Pixman format.
- **Early-background exclusion:** removing its execution did not prevent the assertion; it is not necessary to reproduce that specific failure.
- **Weston GL + Mesa softpipe 13.0.6:** Weston initialized EGL and avoided the Pixman assertion at that point. With OEM WM **but no `hmi-controller`**, Home showed black and then aborted by watchdog (**134**).
- **GL + OEM WM + `hmi-controller`:** original Home became visible **reduced to roughly 320 × 365 px in a 1280 × 800 output**, but was not usefully navigable and later aborted by watchdog (**134**). A repeat **without `strace`** had the same failure, ruling out strace as a necessary condition.
- **ApplicationManager:** original WM calls for VolumeOSD, AvOSD and NotificationManager were observed. These do **not** prove any secondary app launch.
- **Unresolved:** possible WM target **1920 × 720** vs guest output **1280 × 800** mismatch; ASTC texture errors preceding the watchdog without demonstrated causal connection; the main-thread stall has no independently verified root cause.
- Earlier interactive Home reference **remains preserved**. No verified application launch, return-to-Home interaction, ten-minute integrated stability or end-to-end Windows double-click test yet.

## Next work

- Inspect the latest private `runs/` logs, screenshots and patch diffs before new experiments; preserve the working software renderer and successful input/controller overlay.
- **Do not rerun manager startup as if untested.** It now registers the bus name briefly and crashes. Identify the fault after Wayland globals enumeration and determine why the original `ivi-window-manager.so` trial triggers Pixman's `src_format` assertion; isolate `early-background` and buffer formats in fresh overlays. No speculative MICOM fixes or fabricated service replies.
- Characterize input-controller coordinate conversion and license provenance; prove the page transition is repeatable in a new disposable overlay.
- Continue original service orchestration, additional apps, localization and remaining ASTC graphics. Research RTX 3080 Ti/VirGL only in a separate optional setup.
- Aim for a **complete interactive OEM multimedia laboratory**, not one particular application.

## Publication

No OEM firmware, binaries, QML, textures, maps, keys, VM disks, unredacted raw logs or vehicle data are distributed. Only independently authored or appropriately licensed code and sanitized evidence may be published. No vehicle flashing, physical CAN injection or testing on the car.
