# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 29 October 2026 (after latest Codex credit cutoff)

See [detailed dated progress report](docs/PROGRESS-2026-10-29.md) and [handoff](docs/AI-HANDOFF.md) for the evidence and exact next steps.

- Original Hyundai `AppHomeScreen` runs in QEMU/Weston/Wayland IVI; Codex reported fullscreen Home remaining visible at 110 s and 170 s. A byte-identical original QML copy is used only in a disposable overlay.
- Original QML variant `E_VEHICLE_BC3 = 23`; test setting `vehicleVariant` from 5 to 23 caused a third page indicator. The original horizontal `ListView` is still **not demonstrably navigable**.
- Codex loaded OEM `ivi-input-controller.so` and compiled an independent `ivi_input` v1 seat-acceptance utility. `default` seat / Home IVI surface **0** acceptance was **confirmed on attempt 2** (`CA_IVI_INPUT_ACCEPTED`).
- The original client then received **`wl_pointer.enter`**, but lost focus on movement. No real page transition was demonstrated.
- The guest kernel recognized **`QEMU Virtio MultiTouch`** and captured a full swipe, **but the OEM client's `wl_touch` trace remained empty**. Codex identified a missing `BTN_TOUCH` injection event and experimented with virtual touch-display association and device order to preserve tablet mouse input.
- **UNRESOLVED AT CREDIT CUTOFF:** the newest reordered-device touchscreen test had started, but its final result is not known. The first action for a new agent is to **inspect the newest run evidence and any still-running QEMU process** before rerunning or changing anything.
- Outgoing D-Bus headers expose 47 distinct call types; active language from shared memory still fails despite available `.qm` files. RTX 3080 Ti/VirGL acceleration is proposed, **not proven**.

**Next task:** verify input end-to-end (`BTN_TOUCH`/guest kernel → Weston focus/seat → client `wl_touch` → original QML `ListView` index), **without inventing client events or changing original OEM binaries/QML**.

## Agent rules

1. First inventory actual local files, open running processes, scripts, logs, and `git status`. The **public repository contains documentation, not the private firmware or full VM**.
2. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
3. Work in a separate branch/worktree and **a new disposable QEMU overlay**; never let Codex and Claude control the same live guest/overlay.
4. Do not edit original Hyundai binaries, QML, images or rootfs. Preserve working SHA-checked snapshots and the validated software rendering path.
5. Public commits: author-owned code, synthetic fixtures, carefully redacted logs/metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, cryptographic secrets or private VM disks.
6. No physical car tests, installation/flashing, CAN injection, weakening host security or invented service responses.
7. Audit provenance of any upstream adaptation before publication, and document reproducible results and rollback.

## Immediate task

**Resume from the latest private run evidence**. Seat acceptance and the first `wl_pointer.enter` have already been reported. Inspect the interrupted VirtIO MultiTouch/`BTN_TOUCH`/device-order experiment first. Obtain verified `wl_touch` delivery and a real original `ListView` index transition before marking navigation functional. If no local lab access is available, prepare a reproducible synthetic test only and explicitly state what was not verified.
