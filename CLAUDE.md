# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 1 November 2026, 01:58 UTC

**Highest-priority report:** [Original MICOM and ApplicationManager power state](docs/PROGRESS-2026-11-01-MICOM-POWER-STATE.md). **Check newer local owner-private runs first**, particularly **`20261101T015819Z-13437-1`** (still in progress at snapshot cutoff).

- **Original hardware-dependent service started:** `20261101T013715Z-19560-1` showed that adding a second QEMU UART **with null backend** eliminated original MICOM's `TCGETS/TCSETS` `EIO` and permitted the original `com.lge.car.micom` service to register on **system D-Bus**; MICOM did not contact a real car.
- **Authentic OEM MICOM→manager data path reproduced from one *synthetic* hardware event:** in **`20261101T015448Z-28405-1`**, a lab-generated UART response to original **`AskSysBootinfo`** made the OEM MICOM send a genuine D-Bus reply; original ApplicationManager logged **`reply is VALID`**, moved **`power_status=1→16`**, and its getter returned 16. The UART response ID **0x8201** and power byte **2** were derived from original binary inspection, while **all remaining response fields are synthetic zeros**. No physical vehicle messages were captured or sent. Do not mistake one packet for a complete MICOM protocol emulator.
- **Condition found, Standby transition unproven:** manager `set_request_standby_screen` stayed at **`ask_standby_status=10`** and logged **`Logic OFF`** while power was **1** in `20261101T012316Z-4751-1`. Original manager static analysis indicates the code branch that sends state **11** requires power **16**. **No proof yet** that the combined run changed status from **10 to 11** or returned Home.
- **Active integration at cutoff:** `20261101T015819Z-13437-1` joined original Home, ApplicationManager, Standby, MICOM and DLT with the controlled UART response. Its **first** test gate is `power_status=16` at method-call time, followed by **`set_request_standby_screen` / `ask_standby_status`** before/after and result **10 or 11**. Only after a confirmed 11, run a separate genuine Confirm→Home test.
- **Earlier working baselines** remain valid: original Home 0→1→0 with manager, original Standby Confirm button emits actual P=R=C=1, and Home stays alive when hidden under experimental Weston frame-rescue with Home-only Mesa llvmpipe. **Original Home return is still not demonstrated**; manager SysV IPC namespace remains isolated. No proprietary binaries or assets in public repository.

**Agent priority:** preserve authentic OEM call chain and one-variable tests. Do not fall back to direct `NotifyMonitorPowerEvent(16)`, event322 or manager appid10/reason11 as proven fixes—they were specifically unsuccessful. Distinguish original OEM outputs from synthetic UART hardware inputs; no real vehicle, no CAN traffic, no firmware flash, no raw response packet publication.

## Previous checkpoint — 31 October 2026, 16:43 UTC

**Read the latest [Home/Standby foreground integration](docs/PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md), [handoff](docs/AI-HANDOFF.md) and [status](docs/STATUS.md).** Older 11:34 UTC notes predate **verified OEM Confirm clicks** and the registered-Home survival improvement.

### Working references and observations

- Original Home navigates **0→1→0 with original ApplicationManager** in `20261031T163512Z-9562-1`, and renders at **1280×730** using experimental Weston FULL_SCREEN HMI controller.
- Original **Standby Confirm** displays, loads and becomes enabled via original Clock calls **reason10/temporal=false → reason11/temporal=true**. Original OEM **button pressed/released/btnClicked** registered **P=R=C=1** in `20261031T132500Z-6658-1`, with an opt-in private QML focus-area z-order adjustment. This is a genuine click, **not a successful app return**.
- Original manager receives a **Standby Confirm → appid2/reason12** transition but rejects it, still reporting **currentStandbyStatus[10] / StandbyStatus is not enabled[10]**. Earlier direct **GoHome event 322** only reached `handleEvent` and returned **255** without `handleGoHomeKey`; manager request **appid10/reason11** was normalized back to 10. **Do not rerun these as solutions.**
- Hidden Home surface **1000** is relocated to layer **4000** and excluded from Weston's active repaint list when Standby **1001** becomes foreground on **102**. Its outstanding Wayland frame callback may remain pending, stalling original Qt Quick. `20261031T161129Z-13234-1` captured a complete core and **deliberate ApplicationManager AppAlive-failure → AppKill(SIGTRAP 133)** before Home's callback arrived.
- Optional **`CA_HMI_FRAME_RESCUE=1`** in a separate, experimental Weston HMI controller delivers callbacks to hidden Home, allowing heartbeat in `20261031T150154Z-12177-1`; it is not an OEM-proven correctness fix. Optional **`CA_HOME_LLVMPIPE=1`** uses llvmpipe **for Home only** (not Standby/Weston) and prevented manager kill through the foreground tests `20261031T162201Z-9612-1` and `20261031T163512Z-9562-1`. Neither fixes persistent Standby black intervals or manager state.
- Last run `20261031T163512Z-9562-1` displayed **Confirm/Language, btn=1, item2=true, drawn=true**, while Home continued heartbeat, no SIGTRAP or watchdog. **Exit 124** is its planned execution cutoff; final supervisor `home_rendered=false` is not proof Home never rendered, but **neither is return to Home established**.
- Earlier **ten-minute** multiprocess original OEM stability references remain preserved. Manager's separate SysV IPC namespace workaround for `MICOMSTATUSMESSAGE` is still active. The original firmware/Qt/Hyundai binaries are untouched; original EngineerMode can display a title but is not functional.
- Original manager's embedded metadata declares **`com.lge.avn.appmanager.info.ask_standby_status`** (reader) and **`standby_status`** (output signal). **The authentic update path for the manager's integer standby state is still unidentified**. Do not fabricate a setter or interpret `NotifyConfirmStatus(false)` as proven writer of this integer.

**Target:** One complete and repeatable **Home → original Standby → Home** journey, actual visible/interactive Home return, no unacknowledged callbacks, missed AppAlive, watchdog, SIGTRAP, or persistent black screens. No unproved synthetic D-Bus responses, physical CAN, OEM firmware uploads, new unapproved screenshots, or simultaneous editing of a live VM by multiple agents.

## Agent rules

1. First inventory actual local files, open running processes, scripts, logs, and `git status`. The **public repository contains documentation, not the private firmware or full VM**.
2. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
3. Work in a separate branch/worktree and **a new disposable QEMU overlay**; never let Codex and Claude control the same live guest/overlay.
4. Do not edit original Hyundai binaries, QML, images or rootfs. Preserve working SHA-checked snapshots and the validated software rendering path.
5. Public commits: author-owned code, synthetic fixtures, carefully redacted logs/metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, cryptographic secrets or private VM disks.
6. No physical car tests, installation/flashing, CAN injection, weakening host security or invented service responses.
7. Audit provenance of any upstream adaptation before publication, and document reproducible results and rollback.

## Immediate task

1. Check latest private completed runs, particularly **`20261101T015819Z-13437-1`**, and inspect active QEMU/agent ownership before launching experiments. Snapshot latest owner report: **01:58 UTC 1 November**.
2. In the validated MICOM+DLT+original Home+manager+Standby environment, verify the original **manager power=16 at test time**, call original `set_request_standby_screen`, and compare **original `ask_standby_status` 10 versus 11**. Log original call/reply/state; **do not assume 11**.
3. If 10 persists, inspect original code's other guards and boot dependencies. If state becomes 11, separately test original Confirm click and **actual visible interactive Home return**, verifying manager layers, callbacks, AppAlive and no crash/black-screen regression.
4. Preserve all old baselines, one QEMU controller, disposable overlays and independent agents/worktrees. The synthetic serial reply, manager IPC isolation, Weston callback rescue, Home-only llvmpipe and private QML focus adjustment remain experimental. No hardware vehicle testing, OEM asset or packet publication, generic always-success D-Bus stand-ins or secret leakage.
