# AI agent handoff — Hyundai i20 N infotainment lab

**Snapshot: 30 October 2026 — initial input/navigation breakthrough with GPT-6 Sol Alto; subsequent application-launch investigation with GPT-6 Astra Medio.** This public note gives new agents a **precise, non-proprietary handoff**. It is **not** a replacement for private WSL run logs, exact scripts, overlays, and captured screens.

Read [status](STATUS.md), [latest IPC/application trials](PROGRESS-2026-10-30-IPC-APPS.md), [earlier GL/WM report](PROGRESS-2026-10-30-GL-INTEGRATION.md), [30 October timeline](PROGRESS-2026-10-30.md), [CLAUDE.md](../CLAUDE.md), [architecture](ARCHITECTURE.md) and [provenance](../PROVENANCE.md).

## Most recent handoff — 30 October 2026, status reported at 19:22 UTC

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

## Resume protocol

1. On the user's computer, inspect newest `runs/`, local `ESTADO-PROYECTO.md` and pending AppStandbyClock results. The state may have advanced after **19:22 UTC**; do not blindly replay this snapshot.
2. Preserve original OEM base images and two distinct successes: older page-0→1 **interactive Home** and newer **ten-minute Home + manager coexistence** using IPC isolation. Do not mistake the IPC bypass for restored OEM shared-memory integration.
3. Trace **original ApplicationManager return 255** and its `Peer.Ping` → manager-triggered SIGTRAP chain using real logs. Preserve service names and origin-specific D-Bus events; don't fabricate replies.
4. In separate overlays, continue original AppSetup and AppStandbyClock initialization; require **buffer attach/commit, visible pixels and user interaction** before claiming an app launch. Do not treat surface 1001 creation as a working Setup screen.
5. Work toward actual Home → second original app → Home behavior, then ten-minute **interactive stability** and a repeatable Windows launcher. Keep provenance and no-car/no-flash restrictions.

## Starter instruction for another agent

> Continue the Hyundai i20 N Gen5W_L lab **from the newest completed private run**, not from scratch. A prior profile at `20261030T020654Z-13522-1` genuinely navigated original Home. A later `20261030T175729Z-3869-1` demonstrated **original Home and ApplicationManager alive together for 10 minutes**, Home visible at **1280×730**, using a **separate SysV IPC namespace** for the manager to avoid a traced `MICOMSTATUSMESSAGE` semaphore deadlock. This is not full OEM IPC. Original Home can send `appid=500` to the manager, but the manager returns **255**, so no target app opens. AppSetup now creates surface 1001 after overlay-only reference viewer remapping, but **never attaches a buffer** in completed trials; removing ApplicationManager did not fix this. The final supplied note shows original AppStandbyClock test `20261030T192157Z-999-1` still underway. **First inspect newest runs**, then pursue real app launch, manager `Peer.Ping`/SIGTRAP behavior and required OEM services without fake replies. Preserve the two baselines, original OEM files, and isolated overlay operation; do not publish proprietary artifacts or test on a vehicle.

## Safety and sharing

No physical-car tests, CAN/MICOM injections, firmware flashing, OEM asset publication, private disk publishing, credentials, or unreversed host security changes. Any public code must be original or license-audited with attribution. Report facts as **runtime observed**, **reported**, **static inspection** or **hypothesis**.
