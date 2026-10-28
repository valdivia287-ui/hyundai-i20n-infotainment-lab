# Research status — 28 October 2026

**Experimental research, not a complete head-unit emulator.**

- In an isolated private QEMU test environment, the original Qt 5.4.1 `qmlscene` rendered a **minimal laboratory QML scene**. Recorded checks: expected pixels, 14 frame callbacks, Wayland `attach` and `commit`.
- The original `AppHomeScreen` executable started and reached QML loading and IVI surface creation. SocketCAN support was missing at first; appropriate guest modules allowed startup to proceed without real CAN devices or traffic.
- A later 65-second run reported surface creation and a buffer attachment, but all screenshots still showed only the Weston/IVI reference desktop. The **OEM HMI has not been visually validated**.
- Observed blockers: unavailable variant selection values (`GUI_VARIANT LOAD FALSE` etc.), inactive image paths, ASTC rejected by the software GL pipeline (`GL_INVALID_ENUM`), and incomplete/private D-Bus initialization.
- Public release of emulator tooling is pending a code/provenance audit. No OEM files are available here.

## Evidence policy

Distinguish measured runtime output from static analysis and hypotheses. Public examples must use original or synthetic assets; no proprietary traces, firmware images, core dumps or host paths containing personal data. Maintainers can reproduce private tests locally with legally obtained input files, but we will not distribute those inputs.
