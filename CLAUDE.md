# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 31 October 2026 (last owner report 11:34 UTC)

**Prioritize [docs/PROGRESS-2026-10-31-OEM-APPS.md](docs/PROGRESS-2026-10-31-OEM-APPS.md), [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) over historical Pixman/small-Home reports.** The public repository is documentation, not the owner's private VM. Inspect newer local `runs/`, investigation notes and running agents before assuming this is current.

### Baselines to preserve

- **Interactive OEM Home:** `20261030T020654Z-13522-1` original page 0→1, and `20261030T201814Z-17465-1` page 0→1→0 with original ApplicationManager; appid 500 reached manager but returned **255**.
- **Fullscreen geometry solution:** `20261030T211509Z-11579-1` used separately compiled Weston 1.10 HMI controller with initial **FULL_SCREEN** layout instead of **TILING** (source of former 320×365). No manual FORCE_HOME_DESTINATION required. This is experimental, not a Hyundai OEM module.
- **Four-component stability:** `20261030T212548Z-18144-1` and `20261031T102501Z-6447-1` show Weston + **OEM Home, OEM ApplicationManager and OEM AppStandbyClock** running together for **~620 seconds guest uptime**. A **threaded Home Qt scene-graph** prevented the prior overlap watchdog in these bounded profiles. Manager still uses a **separate SysV IPC namespace** around MICOMSTATUSMESSAGE; shared OEM IPC has **not** been restored.
- **Second application original pixels:** AppStandbyClock attaches its actual Wayland buffer and intermittently displays **Confirm / Language** and `--:--`, but alternates with black. Direct original Clock D-Bus `show_window_fg` appid **14** has replied `int32 1`; this **does not make it interactive**.
- **Confirm state root clue:** loaded form had `enableBtn=0` and `enableTouch=false`, explaining why Wayland pointer events did not activate QML MouseArea. `temporal=true` did not change this. Static original reason **11** corresponds to **eUSER_INPUT_STANDBY_AGREE_ENABLE**. In `20261031T112444Z-17824-1` reason 11 / temporal true yielded `enableBtn=1` at 20/60s **but no loaded form** (`item1=false, item2=false, isDrawed=false`). Next isolated trial: original **reason 10** to load form then **reason 11** to enable, observing QML click, display and heartbeat.
- **EngineerMode original:** running OEM **UserProfileManager** satisfied missing shared-memory state `KEYSUPPORTCHINESE`. Run `20261031T091312Z-3435-1` showed original **Engineering Mode** fullscreen title, two IVI surfaces and manager appid **301**. It then suffered a **Wayland fd 9 wait** on its main thread; original manager health-check `AppAlive` timed out, resulting in AppKill/SIGTRAP. Full UI **not usable**; do not conflate process registered, surface created and an interactive menu.
- **Future virtual vehicle services:** explore real OEM service dependencies first; no working synthetic D-Bus/CAN/GPS/MICOM simulator has yet been established by these reports. Do not return arbitrary success, or contact a physical vehicle.
- OEM **AppLauncher** executable was located but **not used** due to possible duplicate multi-app startup in manually constructed guest.

**Current target:** ONE stable additional original app showing genuine pixels, accepting input and returning to Home. Preserve original firmware, do not publish proprietary QML, converted images, private screenshots, sensitive logs or VM disks.

## Agent rules

1. First inventory actual local files, open running processes, scripts, logs, and `git status`. The **public repository contains documentation, not the private firmware or full VM**.
2. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
3. Work in a separate branch/worktree and **a new disposable QEMU overlay**; never let Codex and Claude control the same live guest/overlay.
4. Do not edit original Hyundai binaries, QML, images or rootfs. Preserve working SHA-checked snapshots and the validated software rendering path.
5. Public commits: author-owned code, synthetic fixtures, carefully redacted logs/metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, cryptographic secrets or private VM disks.
6. No physical car tests, installation/flashing, CAN injection, weakening host security or invented service responses.
7. Audit provenance of any upstream adaptation before publication, and document reproducible results and rollback.

## Immediate task

1. Inspect latest private run manifests and `investigacion/standby-clock-20261031.md` / `investigacion/engineer-20261031.md`; the latest known published cutoff is **11:34 UTC on 31 October**.
2. Preserve functional interactive/fullscreen and four-process-ten-minute baselines. Use isolated overlays and no competing VM controllers from another agent.
3. Trial **Clock reason 10 followed by reason 11/temporal=true**, measuring live QML `enableBtn`, `enableTouch`, Loader presence, real click and any stable OEM transition. Only claim a usable app after visible UI + interaction.
4. Investigate EngineerMode's Wayland fd 9 main-thread wait and original AppAlive policy independently; do not merely suppress the termination. If service virtualization is warranted, derive minimal authentic contracts from captured calls, preferring already recovered original OEM services.
5. No firmware base modification, unlicensed source publishing, vehicle/CAN testing, passwords, proprietary screenshots or raw logs in the public repo.
