# Roadmap

**Updated 1 November 2026, 01:58 UTC:** Original MICOM now successfully registers on the system bus using a second **virtual QEMU UART**. A **single synthetic AskSysBootinfo hardware response** led to a **genuine MICOM D-Bus response** that original ApplicationManager accepted, moving **`power_status=1→16`** in private run **`20261101T015448Z-28405-1`**. The original manager's Standby-screen branch was found by static inspection to require **power 16**, but **`currentStandbyStatus` 10→11 and Home return have NOT been validated**. The next combined test **`20261101T015819Z-13437-1`** was ongoing at report cutoff; check new local results before repeating. First prove original `set_request_standby_screen` changes Standby state, then separately prove full original **Home→Standby→Home** with visible Home interaction, no watchdog and correct frame callbacks. UART fixtures are synthetic (OEM-derived response ID 0x8201 / power byte 2; all remaining fields synthetic zeros), **not car capture**, and no real vehicle/CAN/firmware interaction is allowed. Preserve previous functional overlays; no unverified services or copyrighted artifacts in public GitHub. See [MICOM report](PROGRESS-2026-11-01-MICOM-POWER-STATE.md), [current status](STATUS.md), [AI handoff](AI-HANDOFF.md).

1. **Publish safe, reproducible tools**: audit original scripts, dependencies, license provenance, private information and hardcoded paths. Provide synthetic fixtures and tests.
2. **Understand IVI visibility**: capture layer assignments, surface ID, buffers and actual composition.
3. **Map theme/variant selection**: distinguish persisted vehicle configuration from firmware defaults without inventing values.
4. **Map graphical resource paths**: document expected mount points and file lookup using metadata, not OEM assets.
5. **Investigate software ASTC support**: test with independently generated textures and document rendering alternatives.
6. **Characterize private D-Bus contracts**: capture interactions in isolated tests; do not fabricate vehicle data.
7. **Developer toolkit**: enable reversible Qt/QML UI experiments and regression tests without touching a vehicle.

A task is complete only with documented evidence, reproducible steps and limitations.
