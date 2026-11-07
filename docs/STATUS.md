Latest checkpoint, 7 November 2026: [original Spanish UI and presentation limits](PROGRESS-2026-11-07-SPANISH-PRESENTATION.md). Original Home and Radio Spanish catalog opens and translated UI are verified. A clean-overlay causal Radio→Home cycle and real post-return page change completed with retained PIDs and aligned complete frames. An intermediate partial Home frame remains unresolved; post-cycle ten-minute stability is not yet validated. The monitor's unchanged-pointer/no-event bug was corrected and a new bounded trial is running. Windows consolidation remains pending; no OEM assets are published.

> **Earlier checkpoint — 6 November 2026, before the input-delivery guard:** 60 decoded original textures restore Radio artwork; Home can recover aligned and genuinely change pages afterward. **That return followed Radio watchdog death, not a proven Home-button action.** Manager NoReply/alive6/kill is traced. Original Home Spanish text and successful Home/Radio Spanish catalog opens are verified; visual Spanish Radio and a stable interactive cycle remain pending. Read [the current evidence and limits](PROGRESS-2026-11-06-RADIO-TEXTURES-SPANISH.md) first.

> **Earlier 6 November checkpoint:** original Confirm → Home → European Radio77 → manager-acknowledged Home return is observed, but post-return alignment/input remain unreliable. New read-only IVI/ListView probes measured an animation-clock discrepancy. A separate Home-only native Qt timer-mode trial produced an aligned intermediate return image, then lost content after the next gesture; it is not a validated fix. Spanish translated UI, repeated cycles and ten-minute stability remain pending. Read [the current evidence and next validation](PROGRESS-2026-11-06-HOME-ALIGNMENT.md) before historical entries below.

> **Earlier 1 November checkpoint:** a targeted, hash-checked laboratory extension of the original transition rollback deadline **10→45s** allowed the real Radio → Home acknowledgment and IVI foreground notification to finish with manager11/11. A separate viewport correction then showed the complete Home icon page after return. Post-return page navigation, persistent Radio content/audio and a stable repeated loop remain unverified. Spanish(EU) startup selection is verified separately. See [current Radio/return evidence](PROGRESS-2026-11-01-HOME-TO-EURADIO.md).

> Earlier checkpoint (14:44 UTC), blocker traced: original Home Peer.Ping returns NoReply; ApplicationManager reaches alive-count6 and orders AppKill (`20261101T143925Z-replay-bb73e0-1`). Diagnose Home delivery/main-thread state next. Original Radio FM rendering is observed; combined stability, interaction and return remain pending.

> Earlier Radio startup checkpoint: original AppEURadio77 launched, registered and displayed its FM interface. Station-list interaction, audio/tuner behavior, Home-driven launch and combined Home stability remain unverified. The prior Confirm detector confused Radio for Confirm in one run; that run is not a Confirm success. See [Radio report](PROGRESS-2026-11-01-RADIO-FILTERING.md).

> Later runtime finding: AppEURadio77 launched and registered in the European synthetic-input trial, but crashed/restarted; OSD/Home also restarted and Confirm was unavailable with the inherited power16 fixture. Stable interactive Radio remains pending.

> Runtime update: a one-byte synthetic UART boot-info change (country0→5) through original MICOM made original AppLauncher report Europe and admit AppEURadio77 in group4 (`20261101T140338Z-23977-1`). Independent Radio UI/audio remains unverified; see the linked report below.

> Update, 1 November 2026: [Radio filtering evidence and modular simulation scope](PROGRESS-2026-11-01-RADIO-FILTERING.md). Original Home requests logical Radio70; static launcher entry identifies AppEURadio77. AppEURadio was omitted from both group3 and group4; populating group3 with accepted AppOSDManager22 did not admit Radio in group4. Next: map the OEM startup eligibility input from bounded MICOM/AppLauncher traffic. Confirm→Home benchmark and its experimental timing/foreground limitations remain in force. Radio/GNSS/modem/navigation functionality is not yet established.

# Earlier research checkpoint — 1 November 2026, 10:19 UTC

**Experimental, isolated QEMU/Weston/Wayland IVI Hyundai i20 N infotainment laboratory.** **Latest milestone, 1 November 2026 10:19 UTC:** original Standby **Confirm** click triggers a *single genuine OEM* return request to original ApplicationManager; original Home comes back and responds to a real drag with its complete second page. This is proven in a **bounded, modified-timing laboratory profile** with a reversible **Standby timer 10→45 s** patch and experimental Weston foreground repair, **not** in unmodified OEM timing. Original AppLauncher runs a reduced list of manager, Home and Standby with controlled environment and launcher-timeout adjustments. Original Home's **Settings submenu** opens and returns to Home in separate runs; a real Radio **appid70/reason32** request was traced, but **AppEURadio did not start**. Earlier MICOM UART test produced manager **power_status=16**; do not conflate it with later launcher runs. **No complete, stable, stock-timing emulator or independently launched Radio yet.** Latest private report: **10:19 UTC**. See [latest 1 November Confirm/AppLauncher/Radio report](PROGRESS-2026-11-01-HOME-CONFIRM-LAUNCHER-RADIO.md), [earlier MICOM/power report](PROGRESS-2026-11-01-MICOM-POWER-STATE.md), and [AI handoff](AI-HANDOFF.md).

> Evidence qualification: the findings below are based on progress logs and screenshots supplied by the owner; the underlying private VM, complete traces and diffs have not been independently inspected for this public report.

## Latest reported milestone — 1 November, 10:19 UTC status

**AppLauncher original is integrated in a reduced original-app profile:** earlier `20261101T025038Z-30966-1` GDB analysis demonstrated that the observed original Home SIGSEGV was secondary to a **Wayland protocol failure** caused by duplicate `QT_WAYLAND_SHELL_INTEGRATION=ivi:ivi` selection. Removing the redundant inherited parent setting gave an original Home application with exactly one IVI integration and no earlier crash (`20261101T032004Z-1523-1`). A **separate reversible 10 s→120 s extension of selected launcher timers** permitted Standby to register in the original AppLauncher-managed flow (`20261101T034232Z-26717-1`); original preloading signal and AppManager response were observed, but a preload signal produced at timeout alone does **not** establish app health.

**Standby auto-return distinguished from real button action:** original Standby can issue the original return request **`(304,2,12,1,0)`** without any click through **QTimer::timerEvent → original clock callback → gotoHomeScreen** (`20261101T091352Z-1495-1`). Thus several earlier visible Standby→Home outcomes were **automatically timed**, not caused by Confirm. In `20261101T095204Z-16827-1` a narrow lab-only timer extension **10000→45000 ms** enabled one actual Confirm click to emit the **first and only** real OEM return request while no timer-based request occurred; manager changed to **standby12 and drawn Home11**. The original Standby QML and OEM binaries were not modified.

**First trace-supported Confirm → navigable Home:** `20261101T095842Z-17749-1` reproduced the real one-click original Confirm handler and only original D-Bus request. An initial +55s Home frame remained visually partial; a later **real Wayland pointer drag** restored an image of the complete **original Home second page**, with original app icons. Original manager reported **standby12/drawn Home11** and original processes remained alive in the bounded test. This is a functional milestone **under experimental timing and Weston Home surface-foreground repair**, not proof of immediate, fully faithful or long-term stable graphics.

**Settings round trip independently demonstrated:** in earlier integrated *auto-return* profiles `20261101T052217Z-19198-1` and `20261101T053427Z-13124-1`, the **original Settings submenu of Home** displayed Sound, Phone connection, Profile, Theme/Layout, Display, Button and General. A genuine back click restored the original Home page1 icons. This was **internal QML navigation**, not an independently launched `AppSetup` application; it was **not separately repeated in the later Confirm-causal timer run**.

**Radio icon is responsive but Radio is not running:** `20261101T101301Z-27925-1` traced original `homeListSendToApp itemID=4` and original D-Bus manager request **`(304,70,32,1,0)`**. Original Home received 255 but this return code **is not sufficient by itself** to classify the call. At +20/+40s manager still reported standby12/drawn Home11 and **no `AppEURadio` process**. The reduced private AppLauncher configuration only lists manager, Home and Standby: whether an original Radio registration or on-demand launch dependency explains the result **remains a hypothesis**.

[Detailed 1 November Confirm/AppLauncher/Settings/Radio report](PROGRESS-2026-11-01-HOME-CONFIRM-LAUNCHER-RADIO.md). All tested overlays and previous Home baselines were reported preserved; QEMU was stopped after the latest Radio trial.

## Previous reported milestone — 1 November, 01:58 UTC status

**Power-state gating narrowed (static OEM inspection):** original ApplicationManager's `set_request_standby_screen` returned **`Logic OFF`** and `ask_standby_status` stayed **10→10** in `20261101T012316Z-4751-1` while the manager held `power_status=1`. Static inspection indicated the branch emitting Standby state **11** needs manager power property **16**. This is a **precondition finding**, not proof that power 16 alone enables a screen return.

**Original MICOM service starts:** in `20261101T013557Z-29220-1`, original MICOM failed terminal ioctls `TCGETS/TCSETS` on `/dev/ttyS1` with `EIO`; launching original DLT alone was insufficient. In `20261101T013715Z-19560-1`, a second QEMU UART with **null backend** allowed original MICOM to register **`com.lge.car.micom`** on the system D-Bus in a bounded 60s experiment. This proves the initialization dependency, not actual car-protocol support.

**Real end-to-end OEM software response from synthetic UART input:** direct `NotifyMonitorPowerEvent(16)` reached manager but kept `power_status=1` (`20261101T014824Z-15950-1`). In `20261101T015448Z-28405-1`, **one synthetic serial response** to original MICOM `AskSysBootinfo` yielded **original MICOM D-Bus response**, accepted by original manager (`reply is VALID`), which changed **`power_status=1→16`**; original status getter returned **16** and Home was visibly fullscreen at 110s. The serial reply identifier **0x8201** and power byte **2** came from original OEM binary inspection; all remaining payload fields were **zero-filled synthetic test data**, **not captured from any vehicle**.

**Pending at cutoff:** isolated run `20261101T015819Z-13437-1` was **in progress**, combining MICOM+DLT with the established original Home+manager+Standby profile. Its first objective is to test whether the authentic `set_request_standby_screen` call now changes internal **`currentStandbyStatus` 10→11** when **`power_status=16`**. **No outcome, Confirm→Home return, or complete graphical stability is yet documented for this run.**

[Complete sanitized 1 November chronology](PROGRESS-2026-11-01-MICOM-POWER-STATE.md).

## Previous reported milestone — 31 October, 16:43 UTC status

**Real second-application button interaction:** in `20261031T132500Z-6658-1`, original AppStandbyClock displayed loaded+enabled **Confirm** and a controlled button interaction produced **P=1, R=1, C=1** (original pressed, released, btnClicked). The resulting original `appid=2, reason=12` transition request reached ApplicationManager, but was rejected, first because the manager did not regard Standby as the drawing app, and later for its *internal Standby state*. This **supersedes** the prior 11:34 note saying click never succeeded.

**Hidden Home render callback blocker identified:** after original manager foregrounds Standby1001, Home1000 moves to IVI layer **4000**, and its view is **excluded from repaint** despite visible flags. An outstanding `wl_surface.frame` can lack `wl_callback.done`, leaving original Home waiting in Qt Quick; watchdog **134** or manager **AppAlive failure → AppKill/SIGTRAP 133** can follow. In original Home core `20261031T161129Z-13234-1`, manager's six unsuccessful AppAlive probes and deliberate kill were recorded; a frame callback arrived **after** the kill.

**Two lab-only remedies, bounded evidence:** a reversible HMI frame-callback rescue produced callbacks for hidden Home and restored its heartbeat in `20261031T150154Z-12177-1` (stopped at planned 124). Changing **only Home** to Mesa **llvmpipe** in `20261031T162201Z-9612-1` prevented manager's AppKill during the Standby foreground trial, despite intermittent failed AppAlive probes. This is **not** evidence that full OEM frame scheduling/IPC is restored or that black Standby intervals are fixed.

**Original Home navigation with manager:** in latest run **`20261031T163512Z-9562-1`**, two QMP drags caused genuine **`advancedModePageChange(1)`** followed by **`advancedModePageChange(0)`** while manager was running. Original Standby later became foreground; private probe showed **Confirm/Language**, **`btn=1`**, **`item2=true`**, **`drawn=true`**. Original Home continued heartbeats through the timed end **124**, **without SIGTRAP or watchdog**. QEMU later shut down via ACPI; no VM reportedly remained active.

**Return remains unachieved:** direct `Transition::request(322,11,0,1,0)` only reached `handleEvent`, returned **255**, did **not** trigger `handleGoHomeKey`. Another original request `appid=2, reason=12` was rejected with **`currentStandbyStatus[10]` / `StandbyStatus is not enabled[10]`**. Asking manager for **appid=10, reason=11** was also tested and did **not** change its state. Embedded interface metadata contains original **`ask_standby_status`** (reader) and **`standby_status`** (signal), but **the OEM writer/updater of the manager's integer state is unknown**. Do not invent a setter or claim functional return.

**Supervisor caveat:** final `estado.json` for the last run says **home_expired**, 600-second limit, `home_validated=false` and `home_rendered=false`. These are **final-state flags**, not a contradiction of original Home logs and mid-run screenshot; equally, there is no verified visible Home return after Standby.

[Full sanitized 16:43 UTC chronology](PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md).

## Historical milestone — 31 October, 11:34 UTC status

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

- First inspect any **newer private runs after 10:19 UTC 1 November**, current state, agent worktrees and QEMU ownership. Keep one active guest operator.
- Preserve the **new Confirm-driven navigable Home reference `20261101T095842Z-17749-1`**, clearly labelled **timer-extended + experimental compositor-repaired**; retain older baseline `20261030T020654Z-13522-1` and original 31 Oct foreground investigations.
- Prioritize tracing **real `appid=70/reason=32` Radio** registration and whether reduced original AppLauncher config needs original **AppEURadio** in the app list/on-demand path. In one isolated new overlay, verify registration, PID, request, manager drawing status, Wayland IVI surface, actual buffers, screenshot and AppAlive before declaring Radio opened.
- Separately characterize QEMU timing and recover **original Standby 10s timer semantics** without permanently modifying OEM executables or attributing automatic return to user click; distinguish real original `QTimer` request from actual Confirm handler stack.
- Stabilize slow/partial renders and ASTC resources with separately reversible lab graphics experiments. Do not equate `standby_status=12`, a D-Bus return **255**, an initial retained screenshot or an AppLauncher preload-complete signal with successful UI/navigation.
- Keep all synthetic UART MICOM results as a **separate experiment** unless a later run explicitly merges the configurations. Preserve original sources, no physical car/CAN/flashing, no published OEM assets, raw traces, packet bytes or unapproved screenshots.

## Publication

No OEM firmware, binaries, QML, textures, maps, keys, VM disks, unredacted raw logs or vehicle data are distributed. Only independently authored or appropriately licensed code and sanitized evidence may be published. No vehicle flashing, physical CAN injection or testing on the car.
