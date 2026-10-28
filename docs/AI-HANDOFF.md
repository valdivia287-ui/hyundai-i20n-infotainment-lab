# Agent handoff — Hyundai i20 N infotainment research

_Updated 29 October 2026. This file is a **public summary** of privately reported experiments, not a release of executable OEM assets._

## Goal
Reproduce and understand the Hyundai i20 N BC3N infotainment UI in an isolated Linux/QEMU environment, and develop safe independent tools for UI research. Work is **not** intended for flashing a car or modifying safety systems.

## Where things stand

**Independent evidence from earlier Codex report (28 October):**
- Private QEMU Linux guest + Weston/Wayland IVI was running.
- Original Qt 5.4.1 `qmlscene` displayed a synthetic/minimal QML scene. Pixel check, frame callbacks, attach/commit and captured image were recorded.
- Original `AppHomeScreen` initially aborted after SocketCAN `EAFNOSUPPORT`, then proceeded with compatible guest kernel modules; no virtual/real CAN bus traffic required.
- Original QML and image asset locations identified in the privately recovered rootfs. Asset selection and variant configuration still needed investigation.

**Subsequent Codex progress reports and owner-shared screenshots (28–29 October):**
- In a disposable guest overlay, original `AppHomeScreen` produced a visible **small black/dark-blue panel** including the raw translation key `STR_HOME_RADIO`, `MEDIA OFF`, and a graphic background. Screenshots also show the Weston reference desktop around it. **This is independently visible from the supplied screenshots, but not a full usable HMI.**
- Codex reports replacing the failing ASTC software rendering path with checked, lab-derived compatible images in the overlay only, and exposing the recovered original image tree. This result must be tested independently with logs/hashes and the actual patches.
- Codex reports an IVI controller `switch_mode(2)` event and a fullscreen 1280×730 region differing from the baseline by approximately 929,934 pixels. Review the specific linked screenshot and IVI trace before saying fullscreen rendering is independently confirmed.
- Localization strings are unresolved; private D-Bus services and launch coordination remain to be characterized. Some later screenshots show only Weston.
- GPU acceleration with NVIDIA RTX 3080 Ti / virgl was proposed, but **not demonstrated** in the material reviewed for this handoff.

**Environment reported in the private lab:** Windows 11 Pro, Ubuntu-24.04 WSL, QEMU, AMD Ryzen 7 5800X, NVIDIA RTX 3080 Ti, 32 GiB RAM. Hardware details are context, not performance proof. The private Linux lab is not contained in this repository.

## Current technical workstreams
1. Compare stable UI frames across startup; map IVI surface ID, layer assignment, fullscreen switch, z-order and lifecycle.
2. Identify the original translation loader and which absent service/config returns string IDs instead of localized text.
3. Trace D-Bus private-bus startup, `ListNames` and unresolved calls. Do not fabricate vehicle responses.
4. Run ASTC compatibility tests with **synthetic** assets; characterize how the original provider expects compressed asset headers and decoded data without uploading OEM content.
5. Explore VirGL/WSLg GPU acceleration separately from the validated software setup; prove renderer identity, guest frame output and rollback.
6. Convert independently written scripts into portable, tested, licensed public tooling, after provenance review.

## First 20-minute audit for a new agent
- Read `CLAUDE.md`, `docs/STATUS.md`, `PROVENANCE.md`, open Issues.
- Inspect `git status`, working branch, actual files; note that the public clone contains **documentation only**, not the private emulator.
- Select **one** small, independently executable task (synthetic IVI reproduction, docs, test harness).
- If working on the owner's private PC, ask for the current private `ESTADO-PROYECTO.md`, latest run manifest, sanitized log excerpts and the file-level diff; compare with this overview.
- Work in a separate Git branch/worktree. Do not alter another agent's running QEMU instance. Avoid exposing sensitive/private material in prompts or online logs.

## Starting assignment

> Review the public research status and architecture notes. Identify one verifiable experiment to explain why the original AppHomeScreen surface sometimes appears as a small panel and sometimes disappears from later captures. Create a clean, copyright-safe synthetic Wayland/IVI test or a fully specified test plan. Include evidence criteria, expected logs, and a rollback procedure. **Do not** claim access to the private firmware, modify a physical vehicle or overwrite another agent's VM.

## Success criteria
An experiment has real success only if commands, exact inputs, trace/screenshot evidence, hashes where relevant, and limitations are documented. Keep separate: minimal Qt rendering; partial AppHomeScreen visualization; stable navigable original HMI; and later custom functionality.

## Ownership and licenses
Private, proprietary OEM binaries/textures/QML are never uploaded. Contributions that are author-owned may be MIT licensed. Acknowledgements and source auditing: [PROVENANCE.md](../PROVENANCE.md).
