Newer evidence: [original Spanish UI, repeated cycle and partial-frame limits](PROGRESS-2026-11-07-SPANISH-PRESENTATION.md).

# Original Radio round-trip with aligned Home — 6 November 2026

A complete experimental original Confirm → Home → Radio → Home sequence now has visual and causal evidence, including a real post-return Home page change. This is one verified execution, not a completed or generally stable emulator.

## Runtime verified

Private run `20261106T231608Z-replay-c3e00c-1` displayed original Confirm. Its real Qt mouse-release handler issued the first and only original Standby return request; no automatic timer return preceded it. Original Home changed page0→1 and its Radio icon brought original AppEURadio77 to the foreground. Radio was already preloaded by original AppLauncher; the icon is not claimed to have created the process.

Radio processed real Station List and Home mouse releases. The Home control issued original transition arguments 304/11/30. Original ApplicationManager requested Home and acknowledged normal operation; final original drawn/managed getters were 11/11. The original Home and Radio processes retained their PIDs, with no observed manager kill or watchdog before clean shutdown.

The post-return capture shows the complete aligned original Home page with eight icons. Its measured source is 1920×720 and destination 0,0,1280,730 on output 1280×800. A further real pointer drag changed the original ListView 1→0. A fresh GUI-thread read reported currentIndex=0, contentX=0, moving=0 and interactive=1; the final capture independently shows aligned page zero. These private captures and their hashes are preserved, not published.

## What changed

The earlier [core investigation](PROGRESS-2026-11-06-RADIO-CORE-VALIDATION.md) captured the GUI waiting for QtQuick and the render thread waiting in EGL/Mesa/Wayland. A real original Ping method return arrived after its caller's four-second deadline. A separate adapter now gives only original Radio Peer.Ping calls a bounded 30-second wait, alongside the existing Home tolerance. All replies remain original; no service-health success is synthesized. This adapts virtual timing and does not prove that an indefinite graphics wait is solved.

The first trial with that tolerance already showed Radio input and an authentic Home request without process replacement, but the controller measured its observations from QMP submission and stopped too early. Input can wait in the guest queue: the completed cycle measured approximately 11 seconds before Radio processed the Station List release and 27 seconds before it processed Home.

A laboratory observer now writes a PID/sequence acknowledgment only after the original Radio QQuickView release notification returns. The controller waits for that acknowledgment before counting its 15/20/40-second observations. It never changes application properties or manufactures input results. A release acknowledgment alone still does not prove that an application acted; actual manager traffic and fresh visible frames remain necessary.

The established Home-only native Qt timer mode, measured viewport fit and experimental sample-HMI/original-WM coordination remain in the candidate. There were no new OEM QML edits for alignment; the preexisting BC3 variant-selection override remains. Software rendering and original decoded PNG artwork remain in use, not native ASTC support or a demonstrated accelerated guest GPU.

## Limits and next checks

Spanish catalog observation now succeeds without a full startup strace: a private opt-in open64/fstat observer recorded original Spanish Home, Standby, Radio and widget catalogs with real descriptors and sizes. One Spanish trial was stopped by the controller's initial Home release deadline; its console later recorded the correct release. That is a censored observation, not evidence that Spanish broke the OEM application. The next clean-overlay trial changes only that observer window. Visual Spanish Radio and a complete Spanish cycle remain pending. Original translations are untouched.

Ten-minute post-cycle stability, clean-overlay repetition and the unified Windows launcher remain pending. A separately enabled stability profile is prepared, not yet executed: it provisions bounded service lifetimes, samples process identity and RSS, and exercises Home input after the cycle. It must not be reported as repeated Radio foreground cycles or long-term stability before execution.

No RF reception, audio, real stations, vehicle connection, Internet access, modem availability or navigation functionality is established by this result. The original 0.0 MHz default is not an invented station. Reference images/profiles remain preserved, experimental modules remain separate, and the guest has no network adapter. No firmware, OEM binaries, QML, maps, textures, raw traces, cores or new screenshots accompany this public report.
