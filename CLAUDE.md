# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 31 October 2026, 16:43 UTC

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

1. On the owner's machine, **inspect newest private runs and current processes first**; these public notes end at **31 October 2026, 16:43 UTC** and may now be stale.
2. Keep original page-navigation, fullscreen, ten-minute multiprocess and the 16:43 callback-rescue/Home-only-llvmpipe profiles as separate, hash-verifiable disposable overlays; no conflicting concurrent agent actions.
3. **Locate the authentic writer/transition of ApplicationManager currentStandbyStatus (currently 10).** Do not misinterpret read-only `ask_standby_status` or outgoing signal as a setter. Previous direct event322 and manager appid10/reason11 attempts were rejected: do not repeat unchanged.
4. Design a **single-variable, bounded** original OEM interaction to validate state before/after Confirm click and return. Require original **Home** restored on-screen with page navigation, Standby hidden correctly, D-Bus calls/response, real Wayland frame callbacks, stable AppAlive and correct geometry.
5. Remain honest about **lab-only** framebuffer callback rescue, focus MouseArea z-order, llvmpipe Home-only and separate IPC namespace, and about Standby's unresolved intermittent black screen. Keep original OEM assets untouched, no physical vehicle contact and publish only sanitized evidence or license-audited original code.
