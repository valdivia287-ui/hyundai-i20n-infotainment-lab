# Agent handoff — Hyundai i20 N infotainment lab

**Public snapshot: 29 October 2026.** This is an operational handoff for coding agents, not a replacement for the **private** run manifests, evidence, patch diffs or the OEM firmware. Start by reading [STATUS.md](STATUS.md), [../CLAUDE.md](../CLAUDE.md), [../AGENTS.md](../AGENTS.md) and [../PROVENANCE.md](../PROVENANCE.md).

## Mission and context

Study the Hyundai i20 N BC3N Gen5W_L Linux/Qt infotainment UI in a disposable **QEMU + Weston/Wayland IVI + Qt 5.4.1** lab. The owner runs Windows 11 Pro, Ubuntu-24.04 WSL, Ryzen 7 5800X, RTX 3080 Ti, 32 GiB RAM. Do not assume an independent GitHub clone includes the private laboratory, code, overlays, firmware or run logs.

## Latest reported progress (read this instead of older screenshot-only conclusions)

- OEM `AppHomeScreen` drew partial original UI and later rendered fullscreen. Codex reported screenshots at **110 s and 170 s**, a **929,959-pixel difference** from Weston reference, and IVI surface creation/buffer commits/switch-to-fullscreen. Former apparent disappearance was explained by a **125 s test timeout**.
- Original QML was duplicated **byte for byte with matching SHA** into a disposable guest overlay. A diagnostic copy demonstrated `vehicleVariant` value **5 → 23**, corresponding to the original QML enum **`E_VEHICLE_BC3 = 23`**. The trial SQLite database stored 23, and the Home visual gained a **third page indicator**. This did **not** establish N Mode or stable menus.
- Home created three SQLite databases. `MenuHome` has 3 rows and `CustomLayoutFront` has 25 after startup; the earlier missing-table error was transient.
- The supervisor was changed to background the Home process, record its PID, send `TERM` only to Home, wait for **`CA_HOME_DONE 143`**, then shut down and preserve `client-home.txt`, other logs and SQLite evidence.
- Outgoing message header parser reports **47 unique D-Bus method calls**, with **12 appmanager registration entries** involving `com.lge.hyundai.avn.appmanager` and **104 `AskCANMMCANMicomReq` requests** addressed to missing MICOM. `dbus-monitor` alone showed signals, not those unicast calls. Do not invent replies or infer that services are working.
- English `.qm` files are found and can open, but a shared-memory active-language lookup fails. Visible raw translation keys remain.
- OEM Home QML uses a **horizontal `ListView`** for widget and menu pages. A synthetic swipe was not delivered: Weston initially printed **`ivi-controller: No ivi-input-module set`**. Codex found the original **`ivi-input-controller.so`** in the OEM rootfs, verified SHA-256/dependencies, and successfully loaded it in a separate overlay. Nevertheless client-side **`wl_pointer.enter` and motion are still absent**.
- **Active investigation at credit cutoff:** the input module exposes COVESA-like **`ivi_input` v1** protocol. Implement/compile a tiny **lab-authored** tool to **accept the `default` seat for Home IVI surface 0**, verify compositor acknowledgement, and then trace pointer events and QML list index after a controlled swipe. The tool must be restricted to this disposable virtual machine; avoid altering OEM binaries.
- Software path still needs some ASTC resources. GPU/RTX 3080 Ti acceleration is a separate **unverified** track, not a reason to replace the functional software-rendering configuration.

## How to resume safely on owner's PC

1. Discover the current *local* private workspace, and locate the latest private `ESTADO-PROYECTO.md` / `PROGRESO.md`, `runs`, launchers, overlay manifests, log parser and evidence. WSL distribution is **Ubuntu-24.04** (not `Ubuntu`). Check what has already been committed or executed; the public repo may lag the private lab.
2. Identify **the last active `ivi_input` experiment** and whether any commands continued after the status above. Never claim it failed/succeeded without seeing its outputs.
3. Record `git status`, list running QEMU instances, examine scripts and disk overlays before creating your own. **Never attach two supervisors/agents to the same live guest or overlay.** Prefer a separate worktree and copy-on-write image.
4. First test independently that the input controller is loaded and advertises seat protocol; then attempt seat acceptance for IVI surface 0. Record events, compositor logs, and a before/after `ListView` index/capture. If this still fails, inspect focus and coordinate translation rather than forcing a QML replacement.
5. For every test keep commands, changed files, hashes, timestamps and screenshots, and provide a short `RESULTS` summary marking `proven / observed / reported / hypothesis`.

## Starting assignment for Claude Code

> Resume from the 29 Oct 2026 Codex checkpoint. Inspect the most recent private logs, scripts and QEMU state **first**; do not restart from the beginning. The highest-priority blocker is that the OEM `ivi-input-controller.so` loads, but AppHomeScreen still gets no `wl_pointer.enter` / motion. Investigate `ivi_input` version 1, implement a minimal independent seat-acceptance experiment for `default` and IVI surface ID 0 in a disposable VM, and test whether it allows an OEM QML horizontal `ListView` swipe. Preserve the stable software rendering path and do not change the original Hyundai binary/QML. Report failures precisely rather than inventing events.

## Safety and attribution

Do not distribute OEM firmware, binaries, QML, textures, keys, complete VM images or unredacted logs. No writes to vehicle hardware, CAN injection, flash, or changes to host security. Code must be original or have an audited compatible license; provenance tracked in [../PROVENANCE.md](../PROVENANCE.md). The uploaded screenshots and Codex progress text are not by themselves a full independent verification of the private evidence.
