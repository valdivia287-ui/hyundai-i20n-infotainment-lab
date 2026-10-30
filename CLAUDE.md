# Hyundai i20 N Infotainment Lab — CLAUDE.md

This is the public project brief for Claude Code. **Read [docs/AI-HANDOFF.md](docs/AI-HANDOFF.md) and [docs/STATUS.md](docs/STATUS.md) first.** Also review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [PROVENANCE.md](PROVENANCE.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

**Important:** reading this file does not load Codex's former chat, private WSL filesystem, QEMU overlays, or pending processes. To resume the exact experiment, **Claude Code must run with permitted local access to the owner's Ubuntu-24.04 WSL lab and inspect the latest private state and evidence first.** Do not claim continuity based on documentation alone.

## Current checkpoint — 30 October 2026 (latest status 19:22 UTC)

**Read [the latest ten-minute IPC/app trials](docs/PROGRESS-2026-10-30-IPC-APPS.md), [the agent handoff](docs/AI-HANDOFF.md), and [research status](docs/STATUS.md) BEFORE older graphics investigations.** The private files and ongoing Codex sessions are not present in this public repository.

- A preserved run `20261030T020654Z-13522-1` produced original Hyundai Home page **0→1** navigation with a lab IVI input controller; `advancedModePageChange(1)` was logged.
- **New milestone**: `20261030T175729Z-3869-1` kept original `AppHomeScreen`, original `ApplicationManager`, Weston GL and OEM IVI WM **running concurrently for 10 minutes**; screenshots showed Home **1280×730**, without Home watchdog or Pixman assertion in this setup. **Do not extrapolate this to interactive cross-app stability.**
- The earlier watchdog was traced to a Qt SysV semaphore **`MICOMSTATUSMESSAGE`**. As a **laboratory isolation workaround**, the OEM manager was started in a **separate SysV IPC namespace**, preserving real Wayland and D-Bus, **not** the full original shared IPC.
- Surface **1000** was given an overlay-only destination region **0,0,1280,730**; the former **small/black Home** reports are historical failures, not the current best result.
- Original Home page navigation and a click **`appid=500`** reached OEM ApplicationManager; manager returned **255**, so **N Mode did not open**. A diagnostic six-registration replay did not change this.
- Early original manager startup makes `org.freedesktop.DBus.Peer.Ping` calls; after `NoReply`, it deliberately runs `killall -5 AppHomeScreen` (**SIGTRAP**). Preventing SIGTRAP caused escalation to SIGKILL, so that workaround was **rejected**.
- Original **AppSetup** now connects to Wayland and creates IVI surface **1001** after remapping the auxiliary viewer's IDs 1001–1007 to 9001–9007 in an isolated overlay. It **does not attach a buffer, render or provide an interactive page**. A 360-second trial without manager still produced no Setup UI.
- As of 19:22 UTC, run **`20261030T192157Z-999-1`** for original **AppStandbyClock** was **still in progress**. Check newest private files before drawing conclusions; the evidence may have changed.

**Immediate priority:** inspect the newest finished `runs/` and status, preserving **both** the interactive Home and ten-minute coexistence baselines. Diagnose manager **return 255 / Peer.Ping-triggered SIGTRAP**, and actual startup/rendering requirements of original AppSetup and AppStandbyClock. Successful `surface_create` alone is insufficient: require attach/commit, image pixels, interactivity and return to Home. Do not invent replies from OEM D-Bus services, modify firmware bases or publish proprietary artifacts.

## Agent rules

1. First inventory actual local files, open running processes, scripts, logs, and `git status`. The **public repository contains documentation, not the private firmware or full VM**.
2. Keep **reported**, **inspected**, **runtime-proven** and **hypothesized** facts separate.
3. Work in a separate branch/worktree and **a new disposable QEMU overlay**; never let Codex and Claude control the same live guest/overlay.
4. Do not edit original Hyundai binaries, QML, images or rootfs. Preserve working SHA-checked snapshots and the validated software rendering path.
5. Public commits: author-owned code, synthetic fixtures, carefully redacted logs/metadata only. **No** OEM firmware/binaries/QML/textures/maps, private dumps, credentials, cryptographic secrets or private VM disks.
6. No physical car tests, installation/flashing, CAN injection, weakening host security or invented service responses.
7. Audit provenance of any upstream adaptation before publication, and document reproducible results and rollback.

## Immediate task

Continue from the newest **actual local** run and project status; the public documents may lag behind Codex. Known completed milestone: `20261030T175729Z-3869-1` = Home+manager running for ten minutes using separate IPC namespace. Latest trial in supplied report: **AppStandbyClock `20261030T192157Z-999-1`**, result pending. Preserve immutable OEM bases and both successful reference profiles. Seek real Home→another original app→Home operation. Avoid two agents driving the same VM, synthetic service replies, unsafe vehicle interaction and publication of private lab assets.
