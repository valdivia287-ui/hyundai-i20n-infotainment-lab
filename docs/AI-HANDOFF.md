# AI agent handoff — Hyundai i20 N infotainment lab

**Snapshot: 30 October 2026 — Codex running GPT-6 Sol Alto.** This public note gives new agents a **precise, non-proprietary handoff**. It is **not** a replacement for private WSL run logs, exact scripts, overlays, and captured screens.

Read [status](STATUS.md), [30 October timeline](PROGRESS-2026-10-30.md), [CLAUDE.md](../CLAUDE.md), [architecture](ARCHITECTURE.md) and [provenance](../PROVENANCE.md).

## Environment

- Private Windows 11 Pro system: Ryzen 7 5800X, RTX 3080 Ti, 32 GiB RAM.
- WSL distribution **Ubuntu-24.04**, private lab path `/home/valdi/i20n-lab/codex-autonomo`.
- QEMU Linux guest using isolated disposable overlays; Weston/Wayland IVI, original OEM Qt 5.4.1 and `AppHomeScreen`. Current reliable software-rendered profile must be preserved.
- GitHub provides project documentation, **not** the private firmware/VM or source code of the OEM UI.

## Verified as reported in private Codex progress

- Original `AppHomeScreen` reached fullscreen UI; 110s/170s screenshots and surface/buffer traces were reportedly recorded. Prior disappearance came from a test timeout.
- Original QML enum `E_VEHICLE_BC3 = 23`. Setting the active vehicle variant to 23 in a disposable overlay affected Home's visible pages. Original QML and binaries are not changed in the base image.
- Earlier missing pointer/touch input was progressively traced to a missing IVI input module, seat-focus acceptance, timing and an overlaying reference Weston interface (surface IVI **2001**). Home is surface **0**.
- A lab-built `ivi_input` v1 tool accepted `default` seat for Home; the original client eventually received `wl_pointer.enter` and `wl_touch.down/motion/up` after removing the auxiliary reference interface and waiting for client readiness.
- The OEM input controller yielded implausibly small pointer coordinates. A **separate experimental COVESA-derived IVI input-controller build** corrected the coordinate path for a pointer drag. Do **not** overwrite OEM controller files in the base image, nor publish imported source before attribution/licensing audit.
- **Major new result:** a drag produced original QML `onMovingChanged: true`, `onFlickStarted`, `advancedModePageChange(1)` and a captured **second Home page**. This is a page 0 → 1 navigation demonstration, **not** complete UI interactivity or proven touch-driven page navigation.
- **Latest blocker:** a click on an app icon reached the surface but did **not** open the target app. Codex was about to inspect the original client trace for a QML handler or downstream application-manager dependency, when the selected model displayed **“Selected model is at capacity.”**
- Separate unresolved work: D-Bus services (47 call types documented, including appmanager/MICOM requests), shared-memory locale selection, ASTC software rendering gaps, GPU acceleration (not verified).

## Resume protocol

1. On the private PC, **inspect** latest `runs/` and `investigacion/` outputs, run manifests, launcher and source diffs, QEMU processes, guest state and overlays. The model may have written further outputs after the screenshot. Do **not** restart an old task based on this snapshot alone.
2. Preserve the **successful controller/configuration and page 0→1 evidence**. Distinguish actual source code of the OEM controller from the experimental COVESA-derived controller, and verify license provenance.
3. For the last icon click, trace **QMP/Wayland pointer → `AppHomeScreen` QML item / handler → appmanager / D-Bus → target original executable**. Check whether the click is on the intended bounds. Record what the logs really show.
4. Run small, reversible tests in **new QEMU overlays** only. Do not let Claude and Codex drive the same live VM/overlay. Preserve working software rendering, perform clean shutdowns, and record logs/captures/hashes.
5. Build toward multiple original applications and services, rather than focusing on one icon or a single special feature. Never claim complete UI functionality until original target application launch and navigation are demonstrated.

## Starter instruction for another agent

> Continue the Hyundai i20 N Gen5W_L Linux/Qt QEMU laboratory from the **latest local run**, not from scratch. Codex (GPT-6 Sol Alto) reported original Home page 0→1 navigation, supported by `advancedModePageChange(1)`, `onFlickStarted` and a screenshot. An icon click was delivered to the Home surface but did not open an application. Identify whether the click reached the target QML handler and trace its subsequent service/application launch dependency. Audit the lab-built input controller's coordinate fix and third-party code provenance. Preserve original binaries/Qt/QML and use isolated overlays. Report any missing evidence instead of assuming success.

## Safety and sharing

No physical-car tests, CAN/MICOM injections, firmware flashing, OEM asset publication, private disk publishing, credentials, or unreversed host security changes. Any public code must be original or license-audited with attribution. Report facts as **runtime observed**, **reported**, **static inspection** or **hypothesis**.
