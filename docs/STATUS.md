# Research status

**Current as of 10 November 2026.** This page replaces the stacked checkpoint banners used until then. The previous text is preserved verbatim in [history/STATUS-to-2026-11-08.md](history/STATUS-to-2026-11-08.md). Individual `PROGRESS-*` reports remain the evidence; this page only summarises them.

> Experimental, isolated QEMU/Weston/Wayland IVI laboratory running original Hyundai i20 N infotainment software offline. **Not** a complete emulator, firmware mod or vehicle tool. No OEM firmware, binaries, QML, textures, maps or raw traces are published.

## Lab state

- **Platform diagnostics resumed by the owner** on 9 November, limited to disposable offline overlays and one guest at a time. No guest is running; the last diagnostic run shut down cleanly. The accepted product remains frozen.
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

## Platform diagnostics (10 November; development route, not promoted)

- A clean KVM route now reaches the original `Confirm` screen and a stable original Home surface on a fresh offline overlay. It uses the validated application-state prerequisite, the original visible confirmation action, Weston GL with Mesa `softpipe`, and remapped reference-UI surface IDs so they do not collide with Home. In the repeat with adaptive image polling, two consecutive Home frames above the visual-content threshold were observed **66.413 s after QEMU start**; the first and second qualifying frames appeared 19.634 s and 24.820 s after confirmation. This is one development configuration, not an accepted-product promotion or a general benchmark.
- The earlier 115–116 s measurements included a fixed 60 s observation tail and did not represent first Home visibility. The historical TCG mean of 263.43 s used different instrumentation, so the apparent ~3.97× difference is descriptive rather than a controlled accelerator benchmark.
- A separate KVM repeat sampled process CPU for 104.7 s: Weston used 4.03 CPU-seconds (3.85% of one core over the window), ApplicationManager 1.14 s (1.16%), AppHomeScreen 0.72 s (0.97%) and AppStandbyClock 0.22 s (0.22%). These counters do not support host/guest CPU saturation as the remaining startup delay.
- Renderer controls are specific: recent `llvmpipe` Home transitions aborted inside the software rasterizer/GL renderer; selecting the historically valid HMI module did not prevent that abort. A Pixman attempt stopped in the DRM backend before compositor readiness. GL with `softpipe` produced the stable Home result. Host-side VirGL/`egl-headless` was not validated because the WSL host exposed no DRM render node under `/dev/dri`; no RTX acceleration claim is made.
- A separate passive diagnostic added process-scoped Wayland/D-Bus summaries and renderer CPU sampling. In one run it recorded 21 Home-surface commit-to-frame-done pairs (p50 9.145 s, p95 16.371 s, max 16.794 s); pending callbacks peaked at one. These are event percentiles from one run, and syscall tracing may add overhead.
- The same run's renderer samples were 157 windows per renderer: llvmpipe p95 44.097% and max 70.978% of one guest core; softpipe p95 62.768% and max 69.968%. These samples do not establish which subsystem dominates. D-Bus calls/replies were correlated across thread trace files; some calls remained unmatched and are not counted as timeouts.
- Two one-run observer controls suggest tracing cost can distort app timing: N Mode and Manual content times were 24.4 s and 16.3 s longer with all-client tracing than with CPU-only sampling. A manager-only trace still showed a D-Bus Ping p95 around 7.5 s (n=440), while the Home surface callback backlog stayed at one in the traced run (n=21). These are descriptive single-run comparisons; they point to investigating base-process dispatch before callback queueing, but do not prove a root cause.
- The analyzer now uses the outer strace timestamp for Wayland events and sorts process thread files before D-Bus pairing. Synthetic tests cover clock jumps, cross-thread pairing, and CPU units. Raw traces and guest logs are not published; the single reviewed Home screenshot is documented separately with its hash and limitations.
- The three-run TCG baseline remains unchanged. The KVM/softpipe result is a faster development route, but the remaining delay has no proven single cause and the accepted Windows product is still frozen. See the [KVM/softpipe report](PROGRESS-2026-11-10-KVM-SOFTPIPE-HOME.md).

## Pending, in suggested order

1. **Phone121**: the original NotificationManager now registers and answers Peer.Ping; the Phone icon click with it present was not executed. No pairing or calls.
2. **Media**: real request 304/2/27 → 302/0/308. Without provider `mediaCount=0`; with the original AppMediaPlayer provider `mediaCount=1`, still no new UI. `enableMediaGate` also reflects popup state.
3. Settings: Position/Guidance headers and shared provider start order.
4. Europe/Madrid timezone through a real configuration path.
5. Navigation: executable recovered separately; maps, mounts and licences must be validated before any run.

Bound attempts per application, record the first real blocker and continue with the next one.

## Publication

Only independently authored or licence-audited code and sanitised evidence are published. No vehicle tests, CAN injection or flashing. See [README](../README.md#publication-rules).
