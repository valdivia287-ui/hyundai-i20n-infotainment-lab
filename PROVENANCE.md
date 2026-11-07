# Research provenance and third-party acknowledgements

We have consulted and benefited from the following public projects:

1. [laralbir/hyundai-kia-gen5w-navi-firmware](https://github.com/laralbir/hyundai-kia-gen5w-navi-firmware)
2. [cantcs/HKG_Gen5W_ReverseEngineer](https://github.com/cantcs/HKG_Gen5W_ReverseEngineer)

Thank you to their authors and contributors. These upstream projects are acknowledged as research sources, not presented as our own work.

## Before publishing imported or adapted code

For every imported file or implementation, record:

| Local path | Upstream repository | Source path and commit | Upstream license | Changes made | Notices retained |
| --- | --- | --- | --- | --- | --- |
| *Pending audit* | | | | | |

Do not copy source or datasets into this public repository until license compatibility is confirmed, required notices are preserved, and the owner has the right to distribute the material. Linking to a third-party repository is **not** permission to relicense its contents. Hyundai OEM binaries, QML, firmware and textures are excluded regardless.

Reference projects may describe different head units or firmware generations. Verify every technical conclusion against the target system.

## Original laboratory additions, 1 November 2026

`tools/uart_framing.py` and `tests/test_uart_framing.py` were written in this laboratory. They were not copied or adapted from upstream projects, contain no OEM code or captured vehicle messages, and use arbitrary synthetic IDs in the public tests. Runtime-specific OEM request mappings remain private.

`tools/dbus_ping_summary.py` and its tests are also original laboratory code, based on observed D-Bus header structure and invented test data. They contain no imported implementation, OEM resources or private diagnostic capture.

## Original laboratory additions, 6 November 2026

`tools/qt_animation_clock_summary.py` and its tests are original laboratory code, with invented test measurements. No Qt implementation, OEM content or raw private trace is included. The linked Qt 5.4.1 sources are primary research references only; no code was copied or adapted from them.

`tools/elf_core_summary.py` and its tests are original laboratory code. Tests contain invented Linux x86-64 ELF metadata only. No upstream implementation, OEM code, real process memory or private diagnostic output is included.


## Offline Radio-fit evidence verifier (7 November 2026)

`tools/verify_radio_fit_evidence.py` is original laboratory code developed for this project and published under the repository license. It uses Python standard-library parsing/hashing and Pillow image comparison; no upstream implementation or OEM code/assets are copied. It requires a separately supplied completed private run and publishes no private fixtures. Its output is diagnostic evidence, not permission to redistribute OEM logs or screenshots.

## Offline N Mode verifier and static inventory (7 November 2026)

`tools/verify_nmode_evidence.py` and `tools/inventory_oem_apps.py` are original laboratory code under this repository's license. No OEM implementation, assets, binary or private trace is included. The verifier requires separately supplied private evidence and Pillow; the inventory uses standard-library ELF parsing, objdump and read-only debugfs. Static metadata extraction does not execute OEM code or establish application eligibility/safety. Outputs should remain private.
