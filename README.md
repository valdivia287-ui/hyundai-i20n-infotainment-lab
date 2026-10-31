# Hyundai i20 N Infotainment Lab

**Independent, community-driven reverse engineering and offline emulation research.**  
**Status:** experimental — original OEM `AppHomeScreen` is fullscreen and navigable; **multiple original applications now produce limited on-screen UI** in a private QEMU lab. **No secondary app is fully interactive yet**, and a complete Home → app → Home flow remains unresolved.

We are studying how selected software components from a Hyundai i20 N infotainment environment work, with the long-term goal of reproducible offline testing and UI-customization research. The private test lab uses QEMU, Linux, Weston/Wayland IVI, EGL and original Qt 5.4.1 components.

> **This is not a downloadable OEM emulator, firmware mod, unlock tool or vehicle flashing kit.** No original Hyundai firmware, binaries, extracted QML, textures, maps or other proprietary assets are distributed here.

## Research progress (through 31 October 2026, 11:34 UTC; privately reported tests)

| Component | Status |
| --- | --- |
| Isolated QEMU Linux guest and graphics | Running in the private lab |
| Weston + Wayland IVI | Running |
| OEM Qt 5.4.1 `qmlscene` rendering a **minimal laboratory QML scene** | **Verified** via pixel checks, 14 frame callbacks, Wayland `attach` and `commit` |
| OEM `AppHomeScreen` | Original fullscreen Home, confirmed page 0 → 1 → 0 navigation and real N Mode request; **1280 × 730** via reversible fullscreen Weston HMI controller, without manual surface destination override |
| SocketCAN startup dependency | Identified; compatible modules allowed isolated startup to progress without any CAN traffic |
| Original Home navigation | **Page 0 → 1 transition reported** after corrected pointer drag via a separate lab-built IVI controller; corroborated by original QML event and screenshot |
| OEM application launching | Real original ApplicationManager handled Home `appid=500` but still returned **255**. Standby/Valet foreground calls can return success, but the original UI remains partially rendered and unreliable |
| Rendering and stability | A reversible **FULL_SCREEN** Weston HMI-controller resolves the original tiling at **320 × 365**. **Home, ApplicationManager and AppStandbyClock** (plus Weston) ran simultaneously for 10 guest minutes; **threaded** Home render loop prevented an earlier overlap watchdog. The manager still uses an isolated SysV IPC namespace; ASTC/localization remain incomplete |
| Private D-Bus services | Original services/routes examined, including Clock `show_window_fg` and real **UserProfileManager**. Synthetic service compatibility is a **future research direction**, not a completed implementation |
| Second original application UI | **AppStandbyClock** intermittently displays original **Confirm / Language** and `--:--`; **AppEngineerMode** has drawn its original fullscreen title after starting real UserProfileManager. Neither yet provides a stable interactive UI |

**Latest checkpoint (31 October 2026, private status at 11:34 UTC):** a reproducible **fullscreen Weston lab controller** and Home's **threaded** Qt render loop enabled a four-component original stack—Weston plus **Home, ApplicationManager and AppStandbyClock**—to remain alive at guest uptime **~620 seconds** (runs `20261030T212548Z-18144-1` and `20261031T102501Z-6447-1`). AppStandbyClock now intermittently displays genuine **“Confirm / Language”** and `--:--`, but also black screens. A private QML probe found the loaded Confirm button **disabled** (`enableBtn=0`); changing original Clock `show_window_fg` **reason 10 → 11** enables it (`enableBtn=1`) but **the form was then not loaded**, so no functioning click yet. Separately, **original AppEngineerMode rendered its fullscreen title** after **original UserProfileManager** created required shared memory; its main thread subsequently waited on Wayland and manager health checks failed. The **first fully usable second application and Home → app → Home remain open**. These results are owner-supplied Codex reports, not independent QEMU replays. See the [31 October original-app progress](docs/PROGRESS-2026-10-31-OEM-APPS.md).

Details: [Research status](docs/STATUS.md) · [Latest: 31 Oct original applications](docs/PROGRESS-2026-10-31-OEM-APPS.md) · [Earlier IPC/app trials](docs/PROGRESS-2026-10-30-IPC-APPS.md) · [Earlier GL/WM investigation](docs/PROGRESS-2026-10-30-GL-INTEGRATION.md) · [30 October progress log](docs/PROGRESS-2026-10-30.md) · [29 October progress log](docs/PROGRESS-2026-10-29.md) · [AI-agent handoff](docs/AI-HANDOFF.md) · [Roadmap](docs/ROADMAP.md) · [Architecture notes](docs/ARCHITECTURE.md)

## Screenshots from the private QEMU lab (30 October 2026)

These **owner-supplied screenshots** show the original Hyundai Home application running inside a disposable QEMU/Weston guest. They document visible test results, **not** a finished emulator or verified launch of N Mode or other applications.

| Home inicial (110 s) | Segunda página original | Pulsación en icono N |
| :---: | :---: | :---: |
| [![Home original: radio/media keys and dark wave background](docs/images/home-inicial-110s.webp)](docs/images/home-inicial-110s.webp) | [![Home: segunda página con iconos originales y segundo indicador activo](docs/images/home-pagina-1.webp)](docs/images/home-pagina-1.webp) | [![Home: puntero sobre el icono N Mode; aplicación aún sin abrir](docs/images/home-clic-n-mode.webp)](docs/images/home-clic-n-mode.webp) |
| Initial fullscreen Home (untranslated labels remain) | Original menu page 1 reached after a pointer drag | Click routed to original Home; later Codex logs identify `appid=500` and a missing appmanager service |

The 170-second capture supplied by the owner duplicates the page-1 frame, so it is not stored a second time. Images are optimized WebP versions of the supplied captures; no original firmware, extracted textures, binaries, or QML are provided. Hyundai GUI visuals and trademarks remain the property of their owners and are **not relicensed** by this project's MIT license.

## Using another coding agent

This project provides [CLAUDE.md](CLAUDE.md) for Claude Code, [AGENTS.md](AGENTS.md) for other agents, and a shared [AI handoff](docs/AI-HANDOFF.md). These public documents describe the research but **do not** contain the private VM or proprietary input files.

## Where the community can help

- Qt 5.4.1 / QML and Wayland IVI surface visibility and layering
- Linux graphics / EGL / Mesa software rendering
- ASTC texture handling with legally shareable synthetic test assets
- Hyundai/Kia software architecture documentation **without posting OEM files**
- Reproducible offline experiments, original Python/Bash tooling and tests

See [open Issues](../../issues), [contributing guidelines](CONTRIBUTING.md), and [security guidance](SECURITY.md). We encourage small, well-evidenced pull requests. Please mark findings as **runtime verified**, **static analysis**, or **hypothesis**.

## Publication rules

Do **not** submit original firmware, root filesystems, executable binaries, proprietary QML, Hyundai textures, map data, keys, personal identifiers, full core dumps or raw vehicle logs. Do not upload private laboratory directories or VM disk images. Use a clean public working tree, not the private lab checkout.

This research is designed for **offline, isolated software experiments**. The repository does not support CAN injection, interactions with a running vehicle, bypassing vehicle security, or flashing physical head units.

## Licensing and disclaimer

Original code and documentation contributed to this repository are available under the [MIT License](LICENSE), where contributors have the right to license them. The license **does not apply** to Hyundai/Kia or other third-party proprietary works.

This is an unofficial independent project. It is not affiliated with or endorsed by Hyundai Motor Company, Kia or their suppliers. Product names and trademarks belong to their owners.

## Acknowledgements and upstream research

This project has benefited from publicly shared research and materials from the following independent projects. **Thank you to their maintainers and contributors:**

- **[Hyundai/Kia Gen5W navigation firmware research — laralbir](https://github.com/laralbir/hyundai-kia-gen5w-navi-firmware)**: useful reference for studying Gen5W firmware structure and related research.
- **[HKG Gen5W ReverseEngineer — cantcs](https://github.com/cantcs/HKG_Gen5W_ReverseEngineer)**: useful reference for reverse-engineering workflows and Hyundai/Kia Gen5W investigations.

We acknowledge their prior work and ideas. This repository is **not a fork** and does not claim their work as its own. The precise file-level provenance of any adapted scripts or code is still being audited: **do not publish copied upstream code until its origin, license and required notices are verified**. See [PROVENANCE.md](PROVENANCE.md) for the attribution checklist. The platforms researched by these projects may differ from the i20 N BC3N variant.

