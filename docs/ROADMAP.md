# Roadmap

**31 October 2026 priorities:** Preserve interactive/fullscreen OEM Home and the four-component 10-minute QEMU stability baseline. Resolve AppStandbyClock's form/load + enable-state sequence (reason 10 then 11) and EngineerMode's Wayland wait; prove **one original secondary app fully interactive** and Home → app → Home before investing in a Windows launcher. Study original UserProfileManager and other genuine services first, with minimal contract-verified virtual services only where demonstrated necessary. For evidence and limitations see the [current status](STATUS.md) and [31 October report](PROGRESS-2026-10-31-OEM-APPS.md).

1. **Publish safe, reproducible tools**: audit original scripts, dependencies, license provenance, private information and hardcoded paths. Provide synthetic fixtures and tests.
2. **Understand IVI visibility**: capture layer assignments, surface ID, buffers and actual composition.
3. **Map theme/variant selection**: distinguish persisted vehicle configuration from firmware defaults without inventing values.
4. **Map graphical resource paths**: document expected mount points and file lookup using metadata, not OEM assets.
5. **Investigate software ASTC support**: test with independently generated textures and document rendering alternatives.
6. **Characterize private D-Bus contracts**: capture interactions in isolated tests; do not fabricate vehicle data.
7. **Developer toolkit**: enable reversible Qt/QML UI experiments and regression tests without touching a vehicle.

A task is complete only with documented evidence, reproducible steps and limitations.
