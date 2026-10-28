# Research status — 29 October 2026

**Experimental research, not a complete head-unit emulator.**

- In an isolated private QEMU test environment, the original Qt 5.4.1 `qmlscene` rendered a **minimal laboratory QML scene**. Recorded checks: expected pixels, 14 frame callbacks, Wayland `attach` and `commit`.
- The original `AppHomeScreen` executable started and reached QML loading and IVI surface creation. SocketCAN support was missing at first; appropriate guest modules allowed startup to proceed without real CAN devices or traffic.
- An earlier 65-second run reported surface creation and a buffer attachment, but showed only the Weston desktop. Later owner-shared captures **visibly show a small panel drawn by `AppHomeScreen`** containing a graphic background, `STR_HOME_RADIO`, and `MEDIA OFF`. This is **partial OEM HMI visualization**, not a complete or navigable system.
- Later Codex reports say the original image tree was exposed within a disposable overlay and lab-only decoded assets overcame the previous ASTC render rejection. Logs and changes have not been independently re-audited for this report. Missing translation values and incomplete/private D-Bus initialization remain.
- Codex also reports an IVI fullscreen switch and a 1280×730 differing region; independent visual confirmation of the exact corresponding fullscreen screenshot is still pending. Some captures after the partial panel still showed only Weston.
- Public release of emulator tooling is pending a code/provenance audit. No OEM files are available here.

## Evidence policy

Distinguish measured runtime output from static analysis and hypotheses. Public examples must use original or synthetic assets; no proprietary traces, firmware images, core dumps or host paths containing personal data. Maintainers can reproduce private tests locally with legally obtained input files, but we will not distribute those inputs.
