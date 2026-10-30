# Research status — 30 October 2026

**Experimental, isolated QEMU/Weston/Wayland IVI Hyundai i20 N infotainment laboratory.** **New milestone (30 October): original Home and ApplicationManager coexisted for 10 minutes** in a disposable guest using a separate SysV IPC namespace for the manager. Original Home navigation and its `appid=500` request are demonstrated in other completed runs. **No second original application has rendered or become interactive yet.** See [latest IPC/application trials](PROGRESS-2026-10-30-IPC-APPS.md), [earlier GL/WM report](PROGRESS-2026-10-30-GL-INTEGRATION.md) and [agent handoff](AI-HANDOFF.md).

> Evidence qualification: the findings below are based on progress logs and screenshots supplied by the owner; the underlying private VM, complete traces and diffs have not been independently inspected for this public report.

## Newest reported milestone — 30 October, 19:22 UTC status

- **Ten-minute simultaneous operation:** run `20261030T175729Z-3869-1` reportedly kept real `AppHomeScreen`, original `ApplicationManager` and Weston GL/OEM IVI WM alive at **5 and 10 minutes**. Captures show **1280 × 730** Home without Pixman assertion or watchdog failure. This was **not** a demonstrated 10-minute interactive-app test.
- **Watchdog mechanism narrowed:** Home's main thread was blocked in SysV `semtimedop` for Qt semaphore **`MICOMSTATUSMESSAGE`** while original ApplicationManager held the semaphore without the shared-memory state needed to release it. Stopping the manager released Home. The reported workaround runs the manager with **`unshare(CLONE_NEWIPC)=0`** in a separate IPC namespace; OEM shared-memory/IPC behavior remains **incomplete**.
- **Geometry corrected in experiment:** a laboratory IVI destination region for surface **1000** was adjusted to **0,0,1280,730**. The earlier small Home under GL is a **historical failure**, not the latest integrated outcome.
- **Home → ApplicationManager:** separate runs `20261030T174954Z-18971-1` and `20261030T182026Z-30876-1` demonstrated Home navigation, `appid=500` delivered to original manager, and manager return **255**. Replaying six Home registrations and a `registertouchkey` test did not enable launch.
- **Manager-initiated Home termination:** early manager startup ran D-Bus `Peer.Ping`; after `NoReply`, it ran `killall -5 AppHomeScreen`, confirmed as **SIGTRAP**. Blocking that signal led to `killall -9`; the guard was rejected. This is not an unexplained spontaneous Home crash.
- **Original AppSetup:** after remapping reference-viewer surface IDs **1001–1007 → 9001–9007**, AppSetup created original IVI surface **1001** while Home remained visible. **No buffer attached** and no Setup screen was rendered. A 360 s standalone Setup test (without manager) also produced no pixels; its D-Bus queries returned some missing-service errors, not a demonstrated single root cause.
- **AppStandbyClock:** run `20261030T192157Z-999-1` was **in progress as of the supplied 19:22 UTC report**. Its final result is **not known** from these files.
- Reference page-0→1 interactive Home run `20261030T020654Z-13522-1` remains preserved. Check the newest local tests before drawing updated conclusions.

**Read the [full sanitized evidence chronology](PROGRESS-2026-10-30-IPC-APPS.md).** The older sections below record historical troubleshooting snapshots, not the current blockers.

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

## Historical completed-run checkpoint: GL/WM integration (30 October, before IPC fix)

The owner supplied a read-only tracking package of completed tests, allowing more precise assessment than the earlier reports. See the [detailed sanitized progress report](PROGRESS-2026-10-30-GL-INTEGRATION.md).

- **Pixman + OEM WM:** an ARGB8888 `wl_shm` buffer of **1926 × 753** was attached immediately before Weston aborted at `composite_clipped: Assertion src_format failed`. The **actual failing Pixman image/surface has not been identified**. A Wayland SHM format value of 0 is **not** proof of an invalid Pixman format.
- **Early-background exclusion:** removing its execution did not prevent the assertion; it is not necessary to reproduce that specific failure.
- **Weston GL + Mesa softpipe 13.0.6:** Weston initialized EGL and avoided the Pixman assertion at that point. With OEM WM **but no `hmi-controller`**, Home showed black and then aborted by watchdog (**134**).
- **GL + OEM WM + `hmi-controller`:** original Home became visible **reduced to roughly 320 × 365 px in a 1280 × 800 output**, but was not usefully navigable and later aborted by watchdog (**134**). A repeat **without `strace`** had the same failure, ruling out strace as a necessary condition.
- **ApplicationManager:** original WM calls for VolumeOSD, AvOSD and NotificationManager were observed. These do **not** prove any secondary app launch.
- **Unresolved:** possible WM target **1920 × 720** vs guest output **1280 × 800** mismatch; ASTC texture errors preceding the watchdog without demonstrated causal connection; the main-thread stall has no independently verified root cause.
- Earlier interactive Home reference **remains preserved**. No verified application launch, return-to-Home interaction, ten-minute integrated stability or end-to-end Windows double-click test yet.

## Next work

- Read the **newest** completed `runs/` after the **19:22 UTC report**. In particular, inspect any results of the AppStandbyClock trial; do not assume it worked.
- Preserve **two different baselines**: original interactive Home, and ten-minute Home+manager co-existence with the manager in a separate IPC namespace.
- Investigate genuine ApplicationManager error **255**, original D-Bus services, failed `Peer.Ping` and manager-triggered SIGTRAP/SIGKILL as **unresolved OEM startup dependencies**; don't use synthetic answers to claim a working app.
- Continue original AppSetup / StandbyClock launch experiments. Surface creation alone does **not** constitute rendered or interactive app execution: require attach/commit, visual evidence, user input, and Home return.
- Maintain disposable overlays, avoid vehicle interaction or OEM asset publication. Later stages: repeatability, translations/ASTC gaps and Windows one-click launcher.

## Publication

No OEM firmware, binaries, QML, textures, maps, keys, VM disks, unredacted raw logs or vehicle data are distributed. Only independently authored or appropriately licensed code and sanitized evidence may be published. No vehicle flashing, physical CAN injection or testing on the car.
