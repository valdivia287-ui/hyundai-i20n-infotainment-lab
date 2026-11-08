# Hyundai i20 N Infotainment Lab — CLAUDE.md

Current state: [docs/STATUS.md](docs/STATUS.md). How to resume: [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md). Availability: [docs/APPLICATIONS-INTEGRATED.md](docs/APPLICATIONS-INTEGRATED.md). The pre-8-November version of this file is in [docs/history/CLAUDE-to-2026-11-08.md](docs/history/CLAUDE-to-2026-11-08.md) and is historical only.

## Agent rules

1. First inventory actual local files, running processes (QEMU and its owner), newest private runs and `git status`. This public repository contains documentation and author-owned tools, **not** the private firmware or VM.
2. Respect the owner pause recorded in the private `estado.json`; do not start or stop a VM without an explicit owner instruction.
3. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
4. Work in a separate branch and a **new disposable QEMU overlay**; never share a live guest or overlay with another agent. One active guest at a time.
5. Do not edit original Hyundai binaries, QML, images or rootfs, the accepted Windows product or its manifest. Do not re-run settled work without a concrete regression.
6. Public commits: author-owned code, synthetic fixtures, redacted metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, PINs or VM disks.
7. No physical car tests, flashing, CAN injection, weakening host security or invented service responses.
8. Audit provenance of any upstream adaptation before publication; document reproducible results and rollback.
9. When status changes, update `docs/STATUS.md` in place (and move superseded text to `docs/history/`) instead of stacking new banners on top of README/CLAUDE/AGENTS/ROADMAP.
