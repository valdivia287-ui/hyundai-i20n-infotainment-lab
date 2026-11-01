# How to obtain Hyundai infotainment updates independently

This project **does not redistribute Hyundai/Kia OEM firmware, extracted executables, root filesystem, QML, maps, navigation databases, textures or licensed update files**. Participants must obtain any compatible materials themselves, subject to Hyundai's terms and applicable law.

## Official source — Hyundai Europe (Spain)

- **Official Hyundai Navigation / Infotainment Update Portal (Spain):** https://update.hyundai.com/EU/ES/home
- **Search by model or VIN:** https://update.hyundai.com/EU/ES/search
- **Official software / navigation update version list:** https://update.hyundai.com/EU/ES/updateNoticeView/software-version

On the official site, search for **Hyundai i20 N** (listed as i20 N **2022–2025** at the time of the 1 November 2026 update) and check the exact **BC3N / S5W_L** model and system identifiers against the vehicle's actual infotainment version. As of the official **July 2026** entry consulted on 1 November 2026, the European i20 N listing displayed:

| Official field | Published identifier (informative; check the current site) |
| --- | --- |
| Infotainment version | `BC3N.EUR.S5W_L.001.001.260128` |
| Map version | `EUR.18.52.69.012.622.5` |
| Examples of listed model identifiers | `BC3NAS.S5BLC.AEU`, `BC3NAS.S5BLN.AEU` |

**Do not assume that this listing is identical to the private firmware build used in our QEMU research, that all versions are downloadable for every VIN, or that an update package includes the complete system filesystem.** Hyundai may change the site, model selector, package, or version. Verify the exact available variant on the official portal. Do not publish anyone's VIN or credentials.

## What can be shared here

**Allowed, after verification/review:** independently written build scripts, small synthetic test fixtures, open-source-compatible tools with license and provenance checks, configuration templates, documented commands, testing methodology, hardware-service emulators written by the contributor, and owner-approved **UI screenshots** already identified as allowed to publish.

**Not shared:** OEM update packages and files extracted from them, full/decrypted firmware, OEM executables/QML or source assets, maps/map databases, proprietary logos and artwork exported as reusable assets, decryption keys, access tokens, raw diagnostic traces, VINs, private drive paths containing secrets, or instructions to modify a physical car.

Keep privately sourced OEM binaries and map data **outside the public Git working tree**, including Git LFS and release assets, and configure ignore rules. Never attach them to GitHub Actions artifacts. A GitHub commit is not an appropriate archive for copyrighted OEM payloads.

## Offline emulation versus vehicle hardware

The physical unit can rely on **GNSS/GPS**, cellular modem/SIM services, network connectivity, vehicle CAN and MICOM, and proprietary backend information. A QEMU laboratory cannot assume these exist. The code should first trace authentic expected APIs and only then implement **clearly labelled synthetic, opt-in laboratory adapters** (e.g. a fixed-position synthetic GNSS device, deterministic time/clock, dummy cellular link reporting explicitly 'simulated', safe hardware-key signals or a mock modem with no real SIM). Use original Hyundai components downstream where possible; record the input/expected output and do not claim a mock represents a real car.

**Navigation requires special caution:** GPS position is not the same as maps or route guidance. Any map database or online service must be obtained independently with proper permissions. Tests should default to **offline networking**, with optional controlled connectivity for independently authored services only; do not imitate Hyundai cloud identity, subscriptions or credentials.

## Reference and limitations

This is an **unofficial independent research project**, not affiliated with or endorsed by Hyundai, and not a vehicle flashing guide. All tests are isolated from the real car. The official Hyundai site is listed to help owners independently locate legitimate updates, not as permission to redistribute them.
