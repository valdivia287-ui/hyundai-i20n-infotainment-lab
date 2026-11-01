> Current order: verify original Radio interaction; consolidate Home→Standby→Home with original services; prepare the Windows launcher. In parallel, perform non-invasive GNSS, modem and navigation contract analysis. Keep each adapter opt-in and independently validated.

> Runtime update: a one-byte synthetic UART boot-info change (country0→5) through original MICOM made original AppLauncher report Europe and admit AppEURadio77 in group4 (`20261101T140338Z-23977-1`). Independent Radio UI/audio remains unverified; see the linked report below.

> Update, 1 November 2026: [Radio filtering evidence and modular simulation scope](PROGRESS-2026-11-01-RADIO-FILTERING.md). Original Home requests logical Radio70; static launcher entry identifies AppEURadio77. AppEURadio was omitted from both group3 and group4; populating group3 with accepted AppOSDManager22 did not admit Radio in group4. Next: map the OEM startup eligibility input from bounded MICOM/AppLauncher traffic. Confirm→Home benchmark and its experimental timing/foreground limitations remain in force. Radio/GNSS/modem/navigation functionality is not yet established.

# Roadmap

**Updated 1 November 2026, 10:19 UTC:** Original **AppLauncher** now orchestrates a restricted original Home + ApplicationManager + Standby profile under reversible experimental environment/startup-timer corrections. **Original Confirm → original manager standby12/drawn Home11 → original Home page1 navigable** is demonstrated in bounded private run **`20261101T095842Z-17749-1`**: a targeted reversible **Standby QTimer 10→45s extension** allowed the *original Confirm QML click*, rather than the separate original 10s **automatic return**, to issue the **first and only** genuine transition request; original Home navigated after an initially partial frame. Experimental Weston hidden-Home foreground repair still applies. Original Home internal **Settings submenu/back** is proven separately in automatic-return trials. Latest original **Radio** icon request **`(304,70,32,1,0)`** reached the original manager, but no **AppEURadio process** launched; investigate original appid70 registration/on-demand AppLauncher behavior next. **No fully stable unmodified-timing/graphics flow or independent second-app launch** yet. Preserve original Home and new Confirm functional benchmarks in separate disposable overlays, keep MICOM synthetic UART results distinct, do not confuse D-Bus reply255 with launch success, and do not publish OEM assets or connect the vehicle. See [latest Confirm/AppLauncher/Radio report](PROGRESS-2026-11-01-HOME-CONFIRM-LAUNCHER-RADIO.md), [current status](STATUS.md), [AI handoff](AI-HANDOFF.md) and [earlier MICOM research](PROGRESS-2026-11-01-MICOM-POWER-STATE.md).

1. **Publish safe, reproducible tools**: audit original scripts, dependencies, license provenance, private information and hardcoded paths. Provide synthetic fixtures and tests.
2. **Understand IVI visibility**: capture layer assignments, surface ID, buffers and actual composition.
3. **Map theme/variant selection**: distinguish persisted vehicle configuration from firmware defaults without inventing values.
4. **Map graphical resource paths**: document expected mount points and file lookup using metadata, not OEM assets.
5. **Investigate software ASTC support**: test with independently generated textures and document rendering alternatives.
6. **Characterize private D-Bus contracts**: capture authentic interfaces first; then test clearly labelled, deterministic synthetic vehicle inputs in isolated opt-in adapters.
7. **Developer toolkit**: enable reversible Qt/QML UI experiments and regression tests without touching a vehicle.

A task is complete only with documented evidence, reproducible steps and limitations.
