# Research status — 31 October 2026

**Experimental, isolated QEMU/Weston/Wayland IVI Hyundai i20 N infotainment laboratory.** Original Home is fullscreen and navigable. OEM ApplicationManager and AppStandbyClock can coexist with Home for **ten guest minutes** in a laboratory setup. **AppStandbyClock and AppEngineerMode have drawn limited genuine UI, but neither is stable/fully interactive**. Latest verified owner-reported private status: **31 October 2026, 11:34 UTC**. See [31 October OEM app trials](PROGRESS-2026-10-31-OEM-APPS.md), [earlier IPC milestones](PROGRESS-2026-10-30-IPC-APPS.md) and [agent handoff](AI-HANDOFF.md).

> Evidence qualification: the findings below are based on progress logs and screenshots supplied by the owner; the underlying private VM, complete traces and diffs have not been independently inspected for this public report.

## Newest reported milestone — 31 October, 11:34 UTC status

**Home/geometry:** a separate, reversible Weston 1.10 fullscreen HMI-controller module initialized **FULL_SCREEN** instead of the original Weston lab TILING state; this removed the earlier **320×365** tiling without `CA_FORCE_HOME_DESTINATION`. The OEM Home original QML again registered navigation. A threaded Qt scene-graph mode for Home prevented a previous overlap-related watchdog in controlled trials. Distinct baselines remain intact.

**Four-component stability:** private run `20261030T212548Z-18144-1` kept **Weston + original Home + original ApplicationManager + original AppStandbyClock** alive at guest uptime **619.73s**. Later run `20261031T102501Z-6447-1` repeated **619.96s**, Home heartbeat seq **112**, no watchdog on requested shutdown. The manager continues using a **separate SysV IPC namespace**; original OEM IPC is **not fully reproduced**.

**AppStandbyClock original interface:** real Clock `show_window_fg` call at app ID **14** returned `int32 1`; intermittent original **Confirm / Language** and `--:--` appeared, alternating with black. This is **partial real rendering**, not a usable clock. Earlier Standby/Valet successful manager foreground requests had rendered only white.

**Confirm diagnosis (latest):** while Confirm/Language was loaded, a private QML state probe showed **`enableBtn=0`, `enableTouch=false`**. The original QML disabled the MouseArea, explaining ignored pointer events. Setting `temporal=true` alone was insufficient. Static OEM inspection linked **reason 11** to `eUSER_INPUT_STANDBY_AGREE_ENABLE`; the run `20261031T112444Z-17824-1` measured **`enableBtn=1`** at 20 and 60s with reason 11 and temporal=true—but **`item1=false`, `item2=false`, `isDrawed=false`**. **Not proven:** simultaneous visible and enabled Confirm, or a successful QML click. Proposed next lab trial: **reason 10 to show, then reason 11 to enable**, preserving an isolated overlay.

**AppEngineerMode:** launching original **UserProfileManager** created `KEYSUPPORTCHINESE` shared memory, resolving a prior EngineerMode null-access dependency. In `20261031T091312Z-3435-1` the **original EngineerMode** registered with the manager as app ID **301**, created two IVI surfaces and displayed its **“Engineering Mode”** title fullscreen. Manager's **AppAlive** then timed out and initiated **AppKill()/SIGTRAP**. Without manager, the app's main thread remained in `poll` on its Wayland fd 9 after drawing; D-Bus is fd 17. Exact root cause is **not yet known**; only the title, not a complete engineering UI, was displayed.

**Interpretation:** These advances establish **a limited second original application rendering path**, but **neither interactive clock/EngineerMode nor Home→app→Home has been demonstrated**. No synthetic vehicle/D-Bus service or original AppLauncher was installed as a finished solution. Full details and caveats: [31 October evidence chronology](PROGRESS-2026-10-31-OEM-APPS.md).

## Earlier reported milestone — 30 October, 19:22 UTC status

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

**Historical note:** no secondary app had opened during these earlier runs. Subsequent 31 October experiments **did** render original content from Standby and EngineerMode, though neither became fully usable. See [the latest report](PROGRESS-2026-10-31-OEM-APPS.md).

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

- Inspect newer local runs **after the 11:34 UTC status**, if any, before treating the next trial as pending.
- Preserve separate references for Home page navigation, Home+manager stability, and **four-component 10-minute** guest stability. Do not let two agents edit/run the same guest/overlay.
- In Standby, test original **reason 10 → reason 11, temporal=true** in a fresh overlay; prove simultaneously visible **and** enabled Confirm, followed by genuine QML input, a stable screen and Home return. Investigate unexplained black intervals separately.
- In EngineerMode, isolate the **Wayland main-thread wait** and manager **AppAlive/NoReply → AppKill** interaction. A fullscreen title is **not** a functional settings/engineering app.
- Map original service/IPC dependencies before implementing any **minimal synthetic virtual vehicle service**; prioritize real OEM services already recovered, such as UserProfileManager. Do not fabricate D-Bus success.
- Target an interactive second original application and repeatable Home→app→Home, followed by Windows one-click launch. Never flash or interface with a physical vehicle.

## Publication

No OEM firmware, binaries, QML, textures, maps, keys, VM disks, unredacted raw logs or vehicle data are distributed. Only independently authored or appropriately licensed code and sanitized evidence may be published. No vehicle flashing, physical CAN injection or testing on the car.
