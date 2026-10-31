# AI agent handoff — Hyundai i20 N infotainment lab

**Snapshot: 31 October 2026, 16:43 UTC — original Standby button interaction verified, hidden-Home frame-callback blocker isolated, OEM Home page 0→1→0 with manager, and unresolved return-state guard.** This public note gives new agents a **precise, non-proprietary handoff**. It is **not** a replacement for private WSL run logs, exact scripts, overlays, and captured screens.

Read [status](STATUS.md), [latest 31 October foreground/return report](PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md), [earlier 31 October secondary-app trials](PROGRESS-2026-10-31-OEM-APPS.md), [earlier IPC/application trials](PROGRESS-2026-10-30-IPC-APPS.md), [earlier GL/WM report](PROGRESS-2026-10-30-GL-INTEGRATION.md), [30 October timeline](PROGRESS-2026-10-30.md), [CLAUDE.md](../CLAUDE.md), [architecture](ARCHITECTURE.md) and [provenance](../PROVENANCE.md).

## Latest handoff — 31 October 2026, 16:43 UTC

**Read [the 16:43 UTC Home/Standby integration report](PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md) first.** The 11:34 UTC text below is retained as a historical checkpoint and its pending Confirm-click experiment **has been completed**.

- Original **Standby Confirm button genuinely processed a press, release and click** in run **`20261031T132500Z-6658-1`**: private visual probe **P=R=C=1**. An isolated private QML copy lowered the original focus `MouseArea` from z=1000 to z=-1 after enabling the button; this is a lab input workaround, not original firmware modification.
- The two real original D-Bus **`/clock.show_window_fg`** calls (**reason10/temporal false**, then **reason11/temporal true**) allow **Confirm/Language visible and enableBtn=1 simultaneously**, unlike older 11:34 runs. After the OEM click, app manager receives a real **`appid=2, reason=12`** request. It still rejects it, and **Home return is not demonstrated**.
- At foreground, the original manager and OEM IVI WM move **Home surface1000** to **layer4000** (not in compositor's active repaint list) while **Standby1001** is in **layer102**. A Home frame callback remains pending and Qt Quick can block. A separate experimental **`CA_HMI_FRAME_RESCUE=1`** lab Weston HMI module delivered missing callbacks in a bounded test, preventing Home watchdog.
- In a registered-Home run, the original manager recorded six unsuccessful **AppAlive** checks then **AppKill(Home)**; complete core run **`20261031T161129Z-13234-1`** proved manager-initiated **SIGTRAP 133**, with the callback arriving four seconds too late. **Do not misinterpret this as a spontaneous crash.**
- Changing only the original **Home Mesa renderer to llvmpipe** via `CA_HOME_LLVMPIPE=1`, while preserving softpipe for Weston and Standby, avoided manager `AppKill` in `20261031T162201Z-9612-1`. A different previous test of **Standby-only** llvmpipe did **not** fix Home watchdog.
- **Latest completed run `20261031T163512Z-9562-1`:** two QMP drags with original manager active produced **original Home page0→1→0**, then Standby came foreground and original **Confirm/Language** displayed with `btn=1`, `item2=true`, `drawn=true`. Home maintained heartbeat without watchdog/SIGTRAP until its programmed limit **exit124**. This does **not** mean Home was visually restored after Standby.
- **Outstanding specific blocker:** manager retains **`currentStandbyStatus[10]`**, rejecting the OEM **appid2/reason12** transition as not enabled. Direct **`Transition::request(322,11,0,1,0)`** reached `handleEvent` but **not `handleGoHomeKey`**, returned **255**. Asking manager **appid10/reason11** was also tried and normalized to reason10. **Neither is a solution.**
- Static metadata mentions **`com.lge.avn.appmanager.info.ask_standby_status`** as **reader** and **`standby_status`** as emitted signal. **The original integer status writer/event is unknown**. `set_request_standby_screen` lacks a status argument and must not be treated as a setter. `NotifyConfirmStatus(false)` appears to affect a distinct boolean property.
- Final supervisor `estado.json` reported `home_expired`, `home_validated=false`, `home_rendered=false` after **600s programmed timeout**; the actual run's original QML events and earlier screenshot show Home really rendered. The final flags still do not prove end-to-end return.
- **After that run, owner report said VM and supervisor were stopped.** If a newer agent has started since, check actual processes before running another QEMU. Two agents must never alter the same live guest or overlays.

**Immediate target:** Locate the original manager's Standby-state update path and prove a genuine **Home → Standby → Home** sequence with visible return, continued AppAlive/frame callbacks and stable graphics. Do not introduce synthetic success replies or conceal manager kills.

## Historical handoff — 31 October 2026, 11:34 UTC

**Read the [31 October detailed report](PROGRESS-2026-10-31-OEM-APPS.md) and the *newest local private runs* before modifying or launching anything.** The 30 October note below is preserved **as a historical stage**, not current status.

- Original **Home** navigates and runs at **1280×730**. Run `20261030T211509Z-11579-1` fixed the 320×365 display not by manually setting surface geometry, but through a **separate lab-built Weston 1.10 HMI-controller module initially selecting FULL_SCREEN instead of TILING**. Its public-source provenance must be audited before shipping source.
- Original Home + ApplicationManager performed page **0→1→0**, N Mode `appid=500` reached OEM manager, which returned **255**, and ran up to ten guest minutes (`20261030T201814Z-17465-1`). **Manager remains in a separate SysV IPC namespace**, not full shared OEM IPC.
- Original **Home + ApplicationManager + AppStandbyClock**, with Weston, were all active for **~620 s guest uptime** (`20261030T212548Z-18144-1`, `20261031T102501Z-6447-1`). Home's **threaded Qt scene graph** avoided the old overlay-related watchdog in bounded runs. This proves coexistence, **not an interactive app**.
- Original **AppStandbyClock** attached genuine Wayland buffers and began intermittently showing **“Confirm / Language”**, **`--:--`** or black. Original direct Clock D-Bus `show_window_fg` appid **14** replied `int32 1` in one run, but no usable clock or successful Home→Clock→Home.
- A **private QML-only diagnostic probe**, never publish, found **`enableBtn=0` / `enableTouch=false`** while “Confirm / Language” was loaded; mouse delivery alone cannot click a disabled OEM `MouseArea`. `temporal=true` alone did not enable it. Static OEM branch `eUSER_INPUT_STANDBY_AGREE_ENABLE` corresponded to original `reason=11`. Run **`20261031T112444Z-17824-1`** showed **`enableBtn=1`** at 20 and 60s with `reason=11, temporal=true`, **but the form loader was absent** (`item1=false, item2=false, isDrawed=false`). **Pending test:** `reason=10` to show the form, then `reason=11` to enable it, checking actual QML pointer action.
- Original **UserProfileManager** created shared memory **`KEYSUPPORTCHINESE`**, removing a missing dependency for **AppEngineerMode**. Run **`20261031T091312Z-3435-1`** rendered **“Engineering Mode” fullscreen**, made two IVI surfaces and registered app ID **301**. Manager's **AppAlive NoReply** led to intentional **AppKill()/SIGTRAP**. Without manager, the app's main thread stalled in `poll` on **Wayland fd 9** after rendering; D-Bus fd 17. Full engineering UI not functional.
- The original **AppLauncher** executable exists, but **was not launched**. It starts multiple applications and could conflict with the manually built lab.
- **No virtual vehicle simulation has been validated or integrated as a general fix.** Prioritize real OEM service startup before considering minimal, contract-verified synthetic services. Do not fabricate bus replies.
- Codex agents: separate worktrees and VM/overlay ownership; one must not alter another's live runtime.

**The next milestone remains: one original second application visible, enabled and interactive, with verified return to Home.** This is still pending.

## Historical handoff — 30 October 2026, status reported at 19:22 UTC

**The previous GL/WM failure and missing-appmanager-only diagnoses are historical. Do not resume from them.**

- **New ten-minute milestone:** run `20261030T175729Z-3869-1` reportedly showed **original Home at 1280 × 730 and OEM ApplicationManager running together** with Weston GL/OEM IVI WM at both five and ten minutes, without the earlier Pixman assertion or Home watchdog. This **does not** prove app switching, a fully interactive ten-minute session, or shared OEM IPC.
- The previously recurring Home watchdog was traced to a SysV Qt semaphore **`MICOMSTATUSMESSAGE`**, acquired by ApplicationManager while requisite shared-memory state was absent. A diagnostic **separate IPC namespace (`unshare(CLONE_NEWIPC)=0`) for ApplicationManager** bypasses this contention while maintaining real D-Bus/Wayland. This workaround needs future integration work.
- An experimental surface destination region for **IVI surface 1000** placed Home at **0,0,1280,730**. Keep both older **interactive Home** run `20261030T020654Z-13522-1` and new **ten-minute coexistence** run as different regression references.
- In other completed trials, real Home page navigation and an N Mode click delivered **`appid=500`** to the original manager, which returned **255** (no application window opened). Replaying Home registrations did not remove this error.
- Early manager startup issued D-Bus `Peer.Ping`; after `NoReply`, the **manager deliberately ran `killall -5 AppHomeScreen` (SIGTRAP)**. A signal-blocking experiment caused **SIGKILL** escalation and was discarded.
- Original **AppSetup** can now create IVI surface **1001** after remapping an auxiliary viewer's collisions **1001–1007 → 9001–9007**. AppSetup **has not attached a buffer** or produced a visible UI. Even without ApplicationManager, a 360-second test timed out after D-Bus polling with missing-service messages.
- The latest supplied status lists **AppStandbyClock** test `20261030T192157Z-999-1` **in progress**. Inspect newer local records for its outcome; do **not** claim that it succeeded or failed.
- Public documentation contains sanitized findings only. No new proprietary traces, guest binaries, image captures or VM overlays were committed.

[Full chronological summary and limitations](PROGRESS-2026-10-30-IPC-APPS.md).

## Environment

- Private Windows 11 Pro system: Ryzen 7 5800X, RTX 3080 Ti, 32 GiB RAM.
- WSL distribution **Ubuntu-24.04**, private lab path `/home/valdi/i20n-lab/codex-autonomo`.
- QEMU Linux guest using isolated disposable overlays; Weston/Wayland IVI, original OEM Qt 5.4.1 and `AppHomeScreen`. Current reliable software-rendered profile must be preserved.
- GitHub provides project documentation, **not** the private firmware/VM or source code of the OEM UI.

## Verified as reported in private Codex progress

- Original `AppHomeScreen` reached fullscreen UI; 110s/170s screenshots and surface/buffer traces were reportedly recorded. Prior disappearance came from a test timeout.
- Original QML enum `E_VEHICLE_BC3 = 23`. Setting the active vehicle variant to 23 in a disposable overlay affected Home's visible pages. Original QML and binaries are not changed in the base image.
- Earlier missing pointer/touch input was progressively traced to a missing IVI input module, seat-focus acceptance, timing and an overlaying reference Weston interface (surface IVI **2001**). Home is surface **0**.
- A lab-built `ivi_input` v1 tool accepted `default` seat for Home; the original client eventually received `wl_pointer.enter` and `wl_touch.down/motion/up` after removing the auxiliary reference interface and waiting for client readiness.
- The OEM input controller yielded implausibly small pointer coordinates. A **separate experimental COVESA-derived IVI input-controller build** corrected the coordinate path for a pointer drag. Do **not** overwrite OEM controller files in the base image, nor publish imported source before attribution/licensing audit.
- **Major new result:** a drag produced original QML `onMovingChanged: true`, `onFlickStarted`, `advancedModePageChange(1)` and a captured **second Home page**. This is a page 0 → 1 navigation demonstration, **not** complete UI interactivity or proven touch-driven page navigation.
- **Newest confirmed diagnostic in owner-shared report (Astra Medio):** Home processes the N Mode icon click and requests **`appid=500`**. The lab lacks a registered D-Bus service named **`com.lge.hyundai.avn.appmanager`**, preventing application launch. The original target app has **not** opened.
- **Pending original ApplicationManager test:** Codex prepared an option for launching the OEM ApplicationManager but **did not execute it** before its last report. It reported 8 passing tests, 281 verified hashes and a clean VM shutdown with logs/overlays preserved. Local state filenames named: `ESTADO-PROYECTO.md`, `investigacion/nmode-click-20261030.md`. These private files are not reproduced in GitHub.
- Separate unresolved work: D-Bus services (47 call types documented, including appmanager/MICOM requests), shared-memory locale selection, ASTC software rendering gaps, GPU acceleration (not verified).

## Earlier recovered completed runs — historical GL/WM debugging

A later owner-supplied read-only tracking bundle documents the **actual post-ApplicationManager tests** and supersedes the earlier "start original manager next" step. Only completed-run summaries and filtered traces were reviewed; newer local trials may exist.

- Original ApplicationManager **did** run and briefly register on D-Bus; with OEM `ivi-window-manager.so`, it later issued original WM calls identifying VolumeOSD, AvOSD and NotificationManager. **These are requests, not working app windows**.
- **Pixman integration:** guest Home created an **ARGB8888 1926 × 753 SHM** buffer immediately before `composite_clipped: Assertion src_format failed`. The **faulting Pixman image remains unidentified**. `early-background` is not required to reproduce it.
- **GL/softpipe integration:** Weston EGL/GL initialized and avoided the Pixman assert, but Home was **black without `hmi-controller`**. With `hmi-controller`, Home was **reduced to ~320 × 365 px inside a 1280 × 800 frame**, then aborted by **watchdog (134)**. Turning off `strace` for Home **did not prevent** that abort.
- Recent runs: `20261030T141623Z-11549-1` (black Home), `20261030T151207Z-3791-1` (small Home/watchdog), `20261030T151528Z-18058-1` (same without strace). All were reportedly stopped, preserving the earlier interactive Home reference at `20261030T020654Z-13522-1`.
- Potential **1920 × 720 WM destination vs 1280 × 800 guest output** geometry mismatch is unproven; an **ASTC texture failure** also appears before watchdog but is not proven causal. Main-thread stack from privately retained Home core is not yet analyzed here.
- Guest script and supervisor gained an optional **`CA_HOME_NO_STRACE=1`** diagnostic, off by default; a repeat without strace still fails.
- Read [new detailed checkpoint](PROGRESS-2026-10-30-GL-INTEGRATION.md) and inspect any newer `runs/` **before** attempting changes. Public repository contains **none of the private tracking ZIP contents**, only this safe summary.

## Resume protocol — current

1. Check the latest private `ESTADO-PROYECTO.md`, `INFORME-SEGUIMIENTO-20261031.md`, investigation notes, finished `runs/`, live processes and Git state. The public snapshot is only through **16:43 UTC**.
2. Preserve interactive Home, fullscreen Weston controller, four-component ten-minute baseline, **experimental frame-rescue** and **Home-only llvmpipe** runs as **distinct** overlays. Never claim full OEM IPC, since ApplicationManager still runs in a separate SysV IPC namespace.
3. **Do not repeat** reason10→reason11 just to test whether Confirm is clickable: authentic P=R=C=1 has already been observed. Instead trace the manager's *actual writer/trigger* of integer **`currentStandbyStatus`** and the expected original reason12 return transition.
4. Do not repeat rejected direct GoHome event **322** or manager Standby reason11 requests as fixes. Check original source of state, signals and handlers, with a new bounded **one-variable** test.
5. For every foreground and return trial, verify **original Home page interaction**, original Standby visible and enabled, genuine click, actual `Home` reappearance, Wayland callbacks (including when Home is hidden), manager AppAlive, and no watchdog or SIGTRAP. Distinguish a screen temporarily black from a crashed process.
6. Keep private QML changes, any COVESA-derived Weston modules, callback rescue and guest overlays **private**, and have a separate coding agent analyze without sharing live VM ownership. Prefer real OEM service behavior; simulate only demonstrated known contracts, never arbitrary success.

## Starter instruction for another agent

> Continue the Hyundai i20 N Gen5W_L offline QEMU lab **from newest local finished run**. Owner's last supplied report at **31 Oct 16:43 UTC** identifies run **`20261031T163512Z-9562-1`**: genuine OEM Home page 0→1→0 with original ApplicationManager, then foreground original Standby with **Confirm/Language loaded+enabled**; hidden Home stayed alive using separately built **experimental HMI frame callback rescue** and **Home-only Mesa llvmpipe** until planned timeout 124. Original Confirm's real pressed/released/btnClicked signals **P=R=C=1** were already established in `20261031T132500Z-6658-1`; click delivered **appid=2 reason=12** but manager rejected return because **currentStandbyStatus remains 10**. Direct event322 and manager appid10/reason11 requests have **already failed with 255** and must not be presented as the fix. Embedded original bus interface exposes **ask_standby_status** (reader), **standby_status** (signal); **the writer of manager's internal integer state is unknown**. Investigate the genuine OEM state update/transition path; require visual, interactive Home return, Wayland frame completion, successful AppAlive and no black-screen/watchdog regressions. Keep all OEM assets/bases immutable, do not share live VM between agents, do not fabricate service replies or access physical vehicle; first check if later runs supersede this report.

## Safety and sharing

No physical-car tests, CAN/MICOM injections, firmware flashing, OEM asset publication, private disk publishing, credentials, or unreversed host security changes. Any public code must be original or license-audited with attribution. Report facts as **runtime observed**, **reported**, **static inspection** or **hypothesis**.
