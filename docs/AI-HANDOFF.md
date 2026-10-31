# AI agent handoff — Hyundai i20 N infotainment lab

**Snapshot: 31 October 2026, 11:34 UTC — additional original Standby/Clock and EngineerMode rendering and original OEM service investigations.** This public note gives new agents a **precise, non-proprietary handoff**. It is **not** a replacement for private WSL run logs, exact scripts, overlays, and captured screens.

Read [status](STATUS.md), [latest 31 October secondary-app trials](PROGRESS-2026-10-31-OEM-APPS.md), [earlier IPC/application trials](PROGRESS-2026-10-30-IPC-APPS.md), [earlier GL/WM report](PROGRESS-2026-10-30-GL-INTEGRATION.md), [30 October timeline](PROGRESS-2026-10-30.md), [CLAUDE.md](../CLAUDE.md), [architecture](ARCHITECTURE.md) and [provenance](../PROVENANCE.md).

## Latest handoff — 31 October 2026, 11:34 UTC

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

1. Check the actual private `ESTADO-PROYECTO.md`, latest **completed** `runs/`, `investigacion/standby-clock-20261031.md`, `investigacion/engineer-20261031.md`, active processes and Git state. The **11:34 UTC** public snapshot may now be stale.
2. Preserve interactive Home, fullscreen-HMI-controller and four-component ten-minute coexistence as distinct, verified run references; preserve all original OEM binaries and firmware bases.
3. **Clock next:** reason **10** show form → reason **11** enable; require simultaneous loader presence and **enableBtn=1**, actual QML click, stable pixels, and valid Home return. Intermittent black screens remain an independent defect.
4. **Engineer next:** inspect Wayland FD 9 main-thread wait, AppAlive responsiveness and actual pointer focus; do not silence AppKill merely to claim process stability.
5. Map dependencies and run existing OEM services such as UserProfileManager before proposing a fake. A future virtual-vehicle service must be limited to an evidenced contract, with isolated synthetic state and accurate unsupported responses.
6. Use new disposable overlays, keep two Codex agents from shared runtime modifications, publish only sanitized descriptions or licensing-audited original code. No physical vehicle, flash, raw asset uploads or unapproved screenshots.

## Starter instruction for another agent

> Continue the private Hyundai i20 N Gen5W_L QEMU laboratory **from the newest actual local run**, not from a fresh installation. As of owner status **31 October 2026, 11:34 UTC**, original Home is navigable/fullscreen with a separate public-source Weston controller, and OEM Home + ApplicationManager + AppStandbyClock have coexisted for ~620 seconds of guest uptime. Original Clock `show_window_fg` rendered intermittent **Confirm / Language** and `--:--`, but was not usable. A private QML probe showed loaded form with `enableBtn=0`; changing `reason=10` to **11** showed `enableBtn=1` but no loaded form. **Investigate the ordered reason 10 then 11 transition in a fresh overlay.** Original EngineerMode reached fullscreen title after original UserProfileManager supplied `KEYSUPPORTCHINESE`; its main thread later waited on Wayland and AppAlive checks failed. Investigate that wait separately. Keep OEM bases unchanged, isolate the manager's SysV IPC workaround, avoid fake D-Bus replies and physical devices, and require genuine interaction/Home return before claiming second-app success. **Always inspect newer local results first.**

## Safety and sharing

No physical-car tests, CAN/MICOM injections, firmware flashing, OEM asset publication, private disk publishing, credentials, or unreversed host security changes. Any public code must be original or license-audited with attribution. Report facts as **runtime observed**, **reported**, **static inspection** or **hypothesis**.
