# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 29 October 2026

- Original Hyundai `AppHomeScreen` runs in a disposable QEMU / Weston Wayland IVI environment and, per latest Codex results, stays visible in fullscreen snapshots at **110 s and 170 s**. Original QML was copied unchanged into an overlay.
- OEM vehicle variant **`E_VEHICLE_BC3` is 23**. A controlled trial changed `vehicleVariant` from 5 to 23 and produced a third page indicator. **N Mode has not been demonstrated**.
- The local QML contains a **horizontal `ListView`** for widgets and menu pages. Gestures do not yet reach the QML.
- Weston originally logged **`No ivi-input-module set`**. The original **`ivi-input-controller.so`** has since been verified and loaded, yet AppHomeScreen still receives **no `wl_pointer.enter` or motion**.
- **Next experiment:** inspect the actual local protocol and implement a tiny independent `ivi_input` v1 seat-acceptance client for the **`default` seat / Home IVI surface 0**, checking compositor acknowledgement and real client-side pointer events. The acceptance tool is not proven yet.
- A D-Bus header parser reports 47 distinct calls, 12 appmanager registrations and 104 `AskCANMMCANMicomReq` requests. Language determination from shared memory fails despite an English `.qm` file. Neither those services nor localization is solved.
- Graceful teardown via `TERM` and `CA_HOME_DONE 143` retains logs/SQLite evidence. Stable software-rendering setup must not be replaced by speculative GPU work.

See [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) for the detailed evidence ledger and first task.

## Agent rules

1. First inventory actual local files, open running processes, scripts, logs, and `git status`. The **public repository contains documentation, not the private firmware or full VM**.
2. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
3. Work in a separate branch/worktree and **a new disposable QEMU overlay**; never let Codex and Claude control the same live guest/overlay.
4. Do not edit original Hyundai binaries, QML, images or rootfs. Preserve working SHA-checked snapshots and the validated software rendering path.
5. Public commits: author-owned code, synthetic fixtures, carefully redacted logs/metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, cryptographic secrets or private VM disks.
6. No physical car tests, installation/flashing, CAN injection, weakening host security or invented service responses.
7. Audit provenance of any upstream adaptation before publication, and document reproducible results and rollback.

## Immediate task

**Resume exactly from the latest private status when available**. Validate the `ivi_input` seat-to-surface association and obtain `wl_pointer` events in the original AppHomeScreen, then prove a real `ListView` index transition. If no local lab access is available, prepare a reproducible synthetic test only and explicitly state what was not verified.
