# Hyundai i20 N Infotainment Lab

**Independent, community-driven reverse engineering and offline emulation research.**  
**Status:** experimental — original OEM `AppHomeScreen` is fullscreen and navigable **with original ApplicationManager running**; original `AppStandbyClock` now displays and processes a real **Confirm** button click in an isolated QEMU test. **Returning visibly to Home is still blocked by ApplicationManager's Standby state**, so a complete Home → app → Home flow is not yet demonstrated.

We are studying how selected software components from a Hyundai i20 N infotainment environment work, with the long-term goal of reproducible offline testing and UI-customization research. The private test lab uses QEMU, Linux, Weston/Wayland IVI, EGL and original Qt 5.4.1 components.

> **This is not a downloadable OEM emulator, firmware mod, unlock tool or vehicle flashing kit.** No original Hyundai firmware, binaries, extracted QML, textures, maps or other proprietary assets are distributed here.

## Research progress (through 31 October 2026, 16:43 UTC; privately reported tests)

| Component | Status |
| --- | --- |
| Isolated QEMU Linux guest and graphics | Running in the private lab |
| Weston + Wayland IVI | Running |
| OEM Qt 5.4.1 `qmlscene` rendering a **minimal laboratory QML scene** | **Verified** via pixel checks, 14 frame callbacks, Wayland `attach` and `commit` |
| OEM `AppHomeScreen` | Original fullscreen Home at **1280 × 730**; navigation **0 → 1 → 0 while original ApplicationManager is running** (run `20261031T163512Z-9562-1`); independent original N Mode request still returns **255** |
| SocketCAN startup dependency | Identified; compatible modules allowed isolated startup to progress without any CAN traffic |
| Original Home navigation | **Page 0 → 1 transition reported** after corrected pointer drag via a separate lab-built IVI controller; corroborated by original QML event and screenshot |
| OEM application launching | Real original ApplicationManager handled Home `appid=500` but still returned **255**. Standby/Valet foreground calls can return success, but the original UI remains partially rendered and unreliable |
| Rendering and stability | **Fullscreen** Weston controller fixed old **320 × 365** tiling; multiple OEM processes have coexisted for ten guest minutes. A **lab-only Wayland frame-callback rescue** prevented Home's hidden-surface watchdog in bounded trials; Mesa **llvmpipe on Home only** avoided manager `AppKill` in later bounded foreground transitions. Manager IPC namespace remains isolated; no production-grade integration |
| Private D-Bus services | Original services/routes examined, including Clock `show_window_fg` and real **UserProfileManager**. Synthetic service compatibility is a **future research direction**, not a completed implementation |
| Second original application UI | **AppStandbyClock** renders original **Confirm / Language**, enabled (`enableBtn=1`); its **real OEM button emitted pressed, released and btnClicked** in one diagnostic QML overlay (`P=R=C=1`). Manager receives a resulting transition request but **rejects it**; intermittent black screen remains. **AppEngineerMode** rendered its original fullscreen title; neither app has a complete stable navigation flow |

**Latest checkpoint (31 October 2026, owner-supplied status at 16:43 UTC):** genuine OEM **Home navigation 0→1→0** is logged **with ApplicationManager running** in `20261031T163512Z-9562-1`. Original **Standby/Clock** becomes foreground and the Confirm/Language form is visible with **`enableBtn=1`**. An earlier controlled run `20261031T132500Z-6658-1` proved the **original Confirm button's pressed/released/btnClicked signals** (`P=R=C=1`) and delivery of a genuine **appid 2 / reason 12** request. **Manager still rejects return**, retaining **`currentStandbyStatus[10]`**. The direct GoHome event `322` returned **255**; neither it nor re-requesting Standby reason 11 is a valid fix. A separate lab **HMI Wayland callback rescue** and **Mesa llvmpipe on Home only** allowed foreground transitions **without Home watchdog or AppKill** in bounded runs, but are **experimental workarounds**. The last test stopped at its programmed **600s limit (`home-exit=124`)**; its final `home_rendered=false` flag must not be mistaken for proof that Home never rendered or for a successful Home return. **A full interactive Home → Standby → Home cycle is not working yet.** Detailed findings: [31 October foreground/return integration report](docs/PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md).

Details: [Research status](docs/STATUS.md) · [Latest: 31 Oct Home/Standby integration](docs/PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md) · [Earlier 31 Oct app experiments](docs/PROGRESS-2026-10-31-OEM-APPS.md) · [Earlier IPC/app trials](docs/PROGRESS-2026-10-30-IPC-APPS.md) · [Earlier GL/WM investigation](docs/PROGRESS-2026-10-30-GL-INTEGRATION.md) · [30 October progress log](docs/PROGRESS-2026-10-30.md) · [29 October progress log](docs/PROGRESS-2026-10-29.md) · [AI-agent handoff](docs/AI-HANDOFF.md) · [Roadmap](docs/ROADMAP.md) · [Architecture notes](docs/ARCHITECTURE.md)

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

