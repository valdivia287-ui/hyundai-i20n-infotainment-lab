# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 30 October 2026 (Codex: GPT-6 Sol Alto, then GPT-6 Astra Medio)

**Latest [handoff](docs/AI-HANDOFF.md) and [progress report](docs/PROGRESS-2026-10-30.md) supersede older 29 October descriptions.** The private experiment is not automatically available from this public GitHub clone.

- Original Hyundai `AppHomeScreen` renders fullscreen in QEMU + Weston/IVI using original Qt/QML/resources in disposable overlays.
- BC3 variant **23** is reported identified. Home QML uses a horizontal `ListView`.
- The IVI seat/focus helper and touch flow can now deliver `wl_touch.down/motion/up` to the **original** client. A reference Weston UI with surface IVI **2001** had been intercepting input intended for OEM Home surface **0**.
- A separate **experimental** lab controller derived from public COVESA research corrected pointer coordinates. Code provenance/license must be checked before publication; original controller stays preserved.
- **First genuine navigation reported:** Home page **0 → 1** after a pointer drag, corroborated by original `onMovingChanged`, `onFlickStarted`, `advancedModePageChange(1)` logs and a captured second page. **Other application launch is not yet demonstrated.**
- **Newest diagnostic (GPT-6 Astra Medio):** the original Home processes the N Mode icon click and emits a request for **`appid=500`**. The required **`com.lge.hyundai.avn.appmanager`** D-Bus service is not present/registered in the isolated lab, so no target app opens.
- The option to launch the **original OEM ApplicationManager** is **prepared, not yet executed** in QEMU. Astra reported **8 passing tests**, **281 hashes verified** and a **clean VM shutdown**, preserving run logs and overlays. Refer to the private `ESTADO-PROYECTO.md` and `investigacion/nmode-click-20261030.md` checkpoint; never assume the public repo contains them.
- Codex then received **“Selected model is at capacity”**. The previous assistant's attribution to `Sol Ligero` was incorrect; the owner confirmed **GPT-6 Sol Alto** was the model used for this breakthrough.
- Other unresolved issues: incomplete translations/shared-memory language, missing D-Bus/appmanager/MICOM services, ASTC gaps, optional GPU acceleration.

**Next experiment:** inspect newest private run/logs and the already-prepared original ApplicationManager launch option. In a fresh disposable QEMU overlay, test **real OEM ApplicationManager startup and `com.lge.hyundai.avn.appmanager` D-Bus registration**, then retry `appid=500` and trace any further missing dependencies. The overall goal is all original applications, not solely N Mode. Do not redo already solved Home navigation without a reproducibility reason.

## Agent rules

1. First inventory actual local files, open running processes, scripts, logs, and `git status`. The **public repository contains documentation, not the private firmware or full VM**.
2. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
3. Work in a separate branch/worktree and **a new disposable QEMU overlay**; never let Codex and Claude control the same live guest/overlay.
4. Do not edit original Hyundai binaries, QML, images or rootfs. Preserve working SHA-checked snapshots and the validated software rendering path.
5. Public commits: author-owned code, synthetic fixtures, carefully redacted logs/metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, cryptographic secrets or private VM disks.
6. No physical car tests, installation/flashing, CAN injection, weakening host security or invented service responses.
7. Audit provenance of any upstream adaptation before publication, and document reproducible results and rollback.

## Immediate task

**Resume from the latest private run evidence**, not from the now-superseded touch/input blockage. `wl_touch` delivery and original Home page 0→1 navigation have been reported. The blocker has been narrowed to the **missing `com.lge.hyundai.avn.appmanager` service after an `appid=500` Home request**. First inspect the prepared ApplicationManager launcher and the latest private evidence, then test running the original ApplicationManager in a clean overlay; trace its registration and real downstream behavior. Maintain separate VM overlays, stable software rendering and source/provenance attribution. If no local lab access is available, prepare a reproducible synthetic test only and explicitly state what was not verified.
