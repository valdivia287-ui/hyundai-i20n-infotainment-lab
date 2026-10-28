# Hyundai i20 N Infotainment Lab — AI agent context

This is a **public, clean repository** for independent offline research. Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md), [docs/STATUS.md](docs/STATUS.md), [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md) first.

## What is known
- An isolated private QEMU lab has rendered a minimal QML scene with original Qt 5.4.1 on Weston/IVI.
- Later tests with original `AppHomeScreen` rendered a small dark-blue application panel with `STR_HOME_RADIO` and `MEDIA OFF`; visual proof is partial, not a complete usable Hyundai HMI.
- The prior SocketCAN kernel dependency was resolved in the isolated guest (no actual CAN device or traffic).
- Original image paths were exposed in disposable overlays, and a lab-only graphics compatibility experiment was used. Missing localization and D-Bus contracts remain.
- Reports of IVI fullscreen `switch_mode(2)` exist, but review specific captured frames independently.

## Working agreements
1. Before changes, inventory the available files and check which evidence is actually present. Never assume the private lab is included in the GitHub clone.
2. Publish only original code, synthetic fixtures, redacted metadata and documented findings. Never commit OEM firmware, recovered executables/libraries, OEM QML, assets, maps, keys, raw memory dumps or vehicle data.
3. Separate **runtime-proven**, **reported but not independently inspected**, **static analysis** and **hypothesis**.
4. Use feature branches, small commits, tests, and reproducible scripts. When multiple agents are active, use independent worktrees and *never run two controllers against one live QEMU instance/overlay*.
5. Treat all physical-vehicle interaction, firmware flashing, hardware CAN operations and changes to host security as out of scope.
6. Preserve attribution to third-party research; check exact source and license before importing code.
7. In the private lab use copy-on-write overlays and verify hashes; do not overwrite original images or earlier successful runs.
8. Prefer the next smallest independent test over broad changes. Never claim a complete HMI based on a process starting or a surface committing.

## First useful tasks
- Audit synthetic-testable IVI layer visibility and fullscreen control.
- Characterize ASTC/software GL using original synthetic textures.
- Isolate the translation and private D-Bus dependency contracts.
- Package legal-to-share tools with a new clean checkout (not from a private `runs/` directory).

See [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) for the actual handoff checklist and starter task.
