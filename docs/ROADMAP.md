# Roadmap

1. **Publish safe, reproducible tools**: audit original scripts, dependencies, license provenance, private information and hardcoded paths. Provide synthetic fixtures and tests.
2. **Understand IVI visibility**: capture layer assignments, surface ID, buffers and actual composition.
3. **Map theme/variant selection**: distinguish persisted vehicle configuration from firmware defaults without inventing values.
4. **Map graphical resource paths**: document expected mount points and file lookup using metadata, not OEM assets.
5. **Investigate software ASTC support**: test with independently generated textures and document rendering alternatives.
6. **Characterize private D-Bus contracts**: capture interactions in isolated tests; do not fabricate vehicle data.
7. **Developer toolkit**: enable reversible Qt/QML UI experiments and regression tests without touching a vehicle.

A task is complete only with documented evidence, reproducible steps and limitations.
