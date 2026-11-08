# Research status

**Current as of 8 November 2026, ~10:40 UTC.** This page replaces the stacked checkpoint banners used until then. The previous text is preserved verbatim in [history/STATUS-to-2026-11-08.md](history/STATUS-to-2026-11-08.md). Individual `PROGRESS-*` reports remain the evidence; this page only summarises them.

> Experimental, isolated QEMU/Weston/Wayland IVI laboratory running original Hyundai i20 N infotainment software offline. **Not** a complete emulator, firmware mod or vehicle tool. No OEM firmware, binaries, QML, textures, maps or raw traces are published.

## Lab state

- **Experiments paused by the owner** since 8 November ~10:22 UTC. Last real run stopped cleanly (ACPI S5). No guest is running; nothing restarts automatically.
- Target identities, kept separate: physical vehicle **BC3N i20 N MY23, Spain/Europe, software updated 2025**; preferred software profile **BC3N25MY** (native vv81/pf1/nm2). Language7 = Spanish(EU). Country5 = Europe; a Spain-specific index and Europe/Madrid DST are **not** established.

## Accepted product (frozen)

The [Windows launcher v1](WINDOWS-LAUNCHER.md) starts a fresh offline overlay and offers, with mouse input: original Home → N Mode / Radio (FM UI, no tuner) / Manual → native Home return, in Spanish. [Evidence](PROGRESS-2026-11-07-WINDOWS-PRODUCT.md) · [availability matrix](APPLICATIONS-INTEGRATED.md). Later development results are **not** promoted into it and no v2 is being prepared.

## Development results (not in the product)

Each row was verified in a separate development overlay; scopes differ and they are not a count of integrated applications.

| Area | Verified | Open limit | Report |
| --- | --- | --- | --- |
| Settings: General, Keyboard, Display | Original Spanish pages, native Home return; OEM D-Bus subscription limit restored | Resources/latency | [General/Spanish](PROGRESS-2026-11-08-SETTINGS-GENERAL-SPANISH.md) |
| Settings: Theme/layout, N button, Profile | Internal pages, real input, Home return (no preferences changed) | — | [Categories/ASTC](PROGRESS-2026-11-08-SETTINGS-CATEGORIES-ASTC.md) |
| Settings: Bluetooth53 + Android Auto / Apple CarPlay pages | Spanish UI, viewport fit, Back/Home, original illustration via CPU decode | No phone or projection hardware; one 6×6 resource unresolved | [Bluetooth](PROGRESS-2026-11-08-BLUETOOTH-SETTINGS.md) |
| Settings: Sound50 + Equalizer | Complete Spanish content/artwork, internal navigation, Home return | Position/Guidance headers incomplete; DSP/audio unverified | [Order/Sound](PROGRESS-2026-11-08-SETTINGS-ORDER-SOUND.md) |
| Voice Memo117 | Empty-list Spanish UI, Back/Home | No recording/playback | [Categories/ASTC](PROGRESS-2026-11-08-SETTINGS-CATEGORIES-ASTC.md) |
| Original TimeManager | Real VM date/time reaches Home | UTC only; Madrid/DST pending | [Clock](PROGRESS-2026-11-08-ORIGINAL-CLOCK.md) |
| CPU ASTC adapter | Independent decoder; source/block/RGBA hashes match | Not OEM ASTC nor GPU acceleration | [Categories/ASTC](PROGRESS-2026-11-08-SETTINGS-CATEGORIES-ASTC.md) |

## Closed controls (do not repeat without a concrete regression)

- **Without TimeManager** (fresh cold overlay, same graphics/PAS/Bluetooth): the initial General stall **reproduced**. Clock absence is not a fix and TimeManager is not shown to be the sole cause.
- **EGL swap interval 0** (and `vblank_mode=0`) for Settings only: the API call succeeds, but the long presentation wait **remains**. Not promoted. The first attempt failed in the lab's own preloader before reaching Settings and is not a result.
- **Preserved reference graphics**: General recovered after transient NoReply intervals (a first NoReply is not a permanent stall), then Spanish selection and native Home passed.
- Also settled: Home, Radio, N Mode, Manual, Spanish catalogs/persistence, Qt timing, ten-minute stability.

## Pending, in suggested order

1. **Phone121**: the original NotificationManager now registers and answers Peer.Ping; the Phone icon click with it present was not executed. No pairing or calls.
2. **Media**: real request 304/2/27 → 302/0/308. Without provider `mediaCount=0`; with the original AppMediaPlayer provider `mediaCount=1`, still no new UI. `enableMediaGate` also reflects popup state.
3. Settings: Position/Guidance headers and shared provider start order.
4. Europe/Madrid timezone through a real configuration path.
5. Navigation: executable recovered separately; maps, mounts and licences must be validated before any run.

Bound attempts per application, record the first real blocker and continue with the next one.

## Publication

Only independently authored or licence-audited code and sanitised evidence are published. No vehicle tests, CAN injection or flashing. See [README](../README.md#publication-rules).
