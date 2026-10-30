# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 30 October 2026 (Codex: GPT-6 Sol Alto, then GPT-6 Astra Medio)

**Latest [GL/WM integration checkpoint](docs/PROGRESS-2026-10-30-GL-INTEGRATION.md), [handoff](docs/AI-HANDOFF.md) and [progress report](docs/PROGRESS-2026-10-30.md) supersede older 29 October descriptions.** The private experiment is not automatically available from this public GitHub clone.

- Original Hyundai `AppHomeScreen` renders fullscreen in QEMU + Weston/IVI using original Qt/QML/resources in disposable overlays.
- BC3 variant **23** is reported identified. Home QML uses a horizontal `ListView`.
- The IVI seat/focus helper and touch flow can now deliver `wl_touch.down/motion/up` to the **original** client. A reference Weston UI with surface IVI **2001** had been intercepting input intended for OEM Home surface **0**.
- A separate **experimental** lab controller derived from public COVESA research corrected pointer coordinates. Code provenance/license must be checked before publication; original controller stays preserved.
- **First genuine navigation reported:** Home page **0 → 1** after a pointer drag, corroborated by original `onMovingChanged`, `onFlickStarted`, `advancedModePageChange(1)` logs and a captured second page. **Other application launch is not yet demonstrated.**
- **Newest diagnostic (GPT-6 Astra Medio):** the original Home processes the N Mode icon click and emits a request for **`appid=500`**. The required **`com.lge.hyundai.avn.appmanager`** D-Bus service is not present/registered in the isolated lab, so no target app opens.
- The option to launch the **original OEM ApplicationManager** is **prepared, not yet executed** in QEMU. Astra reported **8 passing tests**, **281 hashes verified** and a **clean VM shutdown**, preserving run logs and overlays. Refer to the private `ESTADO-PROYECTO.md` and `investigacion/nmode-click-20261030.md` checkpoint; never assume the public repo contains them.
- Codex then received **“Selected model is at capacity”**. The previous assistant's attribution to `Sol Ligero` was incorrect; the owner confirmed **GPT-6 Sol Alto** was the model used for this breakthrough.
- Other unresolved issues: incomplete translations/shared-memory language, missing D-Bus/appmanager/MICOM services, ASTC gaps, optional GPU acceleration.

**Newest private completed-run results (later 30 October checkpoint):** the manager **was already run**. It registered D-Bus and in OEM WM configurations made requests for VolumeOSD, AvOSD and NotificationManager. **Pixman + OEM WM** causes `composite_clipped: Assertion src_format failed` shortly after a 1926×753 ARGB8888 SHM attach; **the faulty Pixman image is still unknown**. **Weston GL/Mesa softpipe** avoids this assertion, but without `hmi-controller` Home appears black, and **with** `hmi-controller` it draws only about **320×365 in a 1280×800 output**, then fails the **Home watchdog (exit 134)**. Removing `strace` from the Home launch did not fix this (`20261030T151528Z-18058-1`). Early-background was shown unnecessary for the Pixman assertion. **The previously functional page-0→1 Home reference remains preserved.**

**Next experiment:** inspect newest local state and use the [integration report](docs/PROGRESS-2026-10-30-GL-INTEGRATION.md) as a factual checkpoint. Independently isolate the actual failing Pixman image, WM 1920×720 vs output 1280×800 geometry and the original Home main-thread watchdog (private core). Preserve baseline and only afterwards resume live app-launch tests. Neither a second original application nor ten-minute integrated stability has been demonstrated.

## Agent rules

1. First inventory actual local files, open running processes, scripts, logs, and `git status`. The **public repository contains documentation, not the private firmware or full VM**.
2. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
3. Work in a separate branch/worktree and **a new disposable QEMU overlay**; never let Codex and Claude control the same live guest/overlay.
4. Do not edit original Hyundai binaries, QML, images or rootfs. Preserve working SHA-checked snapshots and the validated software rendering path.
5. Public commits: author-owned code, synthetic fixtures, carefully redacted logs/metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, cryptographic secrets or private VM disks.
6. No physical car tests, installation/flashing, CAN injection, weakening host security or invented service responses.
7. Audit provenance of any upstream adaptation before publication, and document reproducible results and rollback.

## Immediate task

**Resume from newest private run, without rerunning the already completed original ApplicationManager startup**. Inspect latest `runs/`, check no concurrent agent/VM is active, identify the Pixman compositor image causing `src_format`, and isolate GL/WM/hmi-controller output geometry and Home watchdog in separate overlays. The latest documented experiments are `20261030T151207Z-3791-1` and `20261030T151528Z-18058-1` (small original Home + watchdog); check newer runs before assuming these remain current. Keep the earlier functional Home navigation baseline and all OEM bases unchanged; no fabricated services, proprietary publication or real vehicle interaction.
