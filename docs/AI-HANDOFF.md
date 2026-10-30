# AI agent handoff — Hyundai i20 N infotainment lab

**Snapshot: 30 October 2026 — initial input/navigation breakthrough with GPT-6 Sol Alto; subsequent application-launch investigation with GPT-6 Astra Medio.** This public note gives new agents a **precise, non-proprietary handoff**. It is **not** a replacement for private WSL run logs, exact scripts, overlays, and captured screens.

Read [status](STATUS.md), [latest GL/WM integration report](PROGRESS-2026-10-30-GL-INTEGRATION.md), [30 October timeline](PROGRESS-2026-10-30.md), [CLAUDE.md](../CLAUDE.md), [architecture](ARCHITECTURE.md) and [provenance](../PROVENANCE.md).

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

## Latest recovered completed runs — integrate from here

A later owner-supplied read-only tracking bundle documents the **actual post-ApplicationManager tests** and supersedes the earlier "start original manager next" step. Only completed-run summaries and filtered traces were reviewed; newer local trials may exist.

- Original ApplicationManager **did** run and briefly register on D-Bus; with OEM `ivi-window-manager.so`, it later issued original WM calls identifying VolumeOSD, AvOSD and NotificationManager. **These are requests, not working app windows**.
- **Pixman integration:** guest Home created an **ARGB8888 1926 × 753 SHM** buffer immediately before `composite_clipped: Assertion src_format failed`. The **faulting Pixman image remains unidentified**. `early-background` is not required to reproduce it.
- **GL/softpipe integration:** Weston EGL/GL initialized and avoided the Pixman assert, but Home was **black without `hmi-controller`**. With `hmi-controller`, Home was **reduced to ~320 × 365 px inside a 1280 × 800 frame**, then aborted by **watchdog (134)**. Turning off `strace` for Home **did not prevent** that abort.
- Recent runs: `20261030T141623Z-11549-1` (black Home), `20261030T151207Z-3791-1` (small Home/watchdog), `20261030T151528Z-18058-1` (same without strace). All were reportedly stopped, preserving the earlier interactive Home reference at `20261030T020654Z-13522-1`.
- Potential **1920 × 720 WM destination vs 1280 × 800 guest output** geometry mismatch is unproven; an **ASTC texture failure** also appears before watchdog but is not proven causal. Main-thread stack from privately retained Home core is not yet analyzed here.
- Guest script and supervisor gained an optional **`CA_HOME_NO_STRACE=1`** diagnostic, off by default; a repeat without strace still fails.
- Read [new detailed checkpoint](PROGRESS-2026-10-30-GL-INTEGRATION.md) and inspect any newer `runs/` **before** attempting changes. Public repository contains **none of the private tracking ZIP contents**, only this safe summary.

## Resume protocol

1. On the private PC, **inspect** latest `runs/` and `investigacion/` outputs, run manifests, launcher and source diffs, QEMU processes, guest state and overlays. The model may have written further outputs after the screenshot. Do **not** restart an old task based on this snapshot alone.
2. Preserve the **successful controller/configuration and page 0→1 evidence**. Distinguish actual source code of the OEM controller from the experimental COVESA-derived controller, and verify license provenance.
3. **Do not return to the superseded missing-appmanager diagnosis.** Inspect the latest GL/WM runs: attribute Pixman's failing image in an instrumented, separate lab Weston; investigate IVI/DRM geometry and Home's watchdog/main-thread backtrace independently. Use fresh overlays and compare against the already functional page-0→1 baseline before each step.
4. Run small, reversible tests in **new QEMU overlays** only. Do not let Claude and Codex drive the same live VM/overlay. Preserve working software rendering, perform clean shutdowns, and record logs/captures/hashes.
5. Build toward multiple original applications and services, rather than focusing on one icon or a single special feature. Never claim complete UI functionality until original target application launch and navigation are demonstrated.

## Starter instruction for another agent

> Continue the Hyundai i20 N Gen5W_L Linux/Qt QEMU lab from the **newest local completed run**, not a fresh setup. A known-good profile at `20261030T020654Z-13522-1` demonstrated original Home page 0→1 navigation. Original ApplicationManager already starts and makes real IVI WM requests, but combining it with Home is not stable. With Pixman and OEM WM, Weston hits `composite_clipped: Assertion src_format failed`; the exact Pixman image is unidentified. GL/Mesa softpipe avoids that assertion but Home is black without hmi-controller; with hmi-controller it draws ~320×365 within 1280×800 and then aborts via watchdog (134), also when strace is disabled (`20261030T151528Z-18058-1`). Inspect newer `runs/`, preserve the working baseline, isolate buffer/format and geometry factors, inspect the Home core main-thread stack in private, and only then retry genuine Home→other OEM application→Home flows. No fake D-Bus responses, original file modifications, car tests or proprietary publication.

## Safety and sharing

No physical-car tests, CAN/MICOM injections, firmware flashing, OEM asset publication, private disk publishing, credentials, or unreversed host security changes. Any public code must be original or license-audited with attribution. Report facts as **runtime observed**, **reported**, **static inspection** or **hypothesis**.
