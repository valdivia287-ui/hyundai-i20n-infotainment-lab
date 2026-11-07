# Original Spanish Home/Radio cycle and bounded post-cycle stability — 7 November 2026

A clean-overlay run completed original Spanish Confirm → Home → Radio → Home, a genuine post-return page change, and then 658.75 seconds of monitored operation with five further native Home page changes. All six original participants retained their process identities. This is a bounded offline UI milestone, not a completed multimedia emulator.

## What the evidence establishes

Private run 20261107T002558Z-replay-90c655-1 used original AppLauncher, ApplicationManager, Home, AppEURadio, MICOM and Weston. Original Confirm input, Radio Station List/Home input and manager return acknowledgment were observed. Home genuinely changed pages after returning from Radio. The monitor then ran for more than ten minutes after that cycle, with Radio retained in the background.

Eleven saved Home screenshots were compared numerically with the complete reference for their actual native page. Their header and content pixels were identical throughout the checked region, as was the lower reserved margin. The small auto-hiding page indicator was excluded from equality checks. Fresh original GUI readings confirmed settled content positions and real alternating page changes. The previous partial-frame interpretation is explicitly corrected in the [Spanish presentation report](PROGRESS-2026-11-07-SPANISH-PRESENTATION.md); no new graphics fix was applied for that mistaken finding.

Twelve process-health samples, including the final endpoint, preserved each original PID and start time. No manager AppKill was observed. The guest synchronized and powered down through its controlled shutdown path, and no QEMU or worker from that run remained.

| Original participant | RSS change during observation |
| --- | ---: |
| AppLauncher | +4 KiB |
| ApplicationManager | 0 KiB |
| Home | +20 KiB |
| AppEURadio | 0 KiB |
| MICOM | 0 KiB |
| Weston | 0 KiB |

These small changes describe one bounded measurement; they are not a long-term leak guarantee. The workload checks Home interaction after one Radio round-trip, with Radio in the background. It does not establish repeated foreground Radio cycles throughout the full observation window.

## Reproduction and retained adaptations

The private laboratory froze the configuration, launch options, own modules, exact source snapshots and evidence hashes separately from earlier functional references. Rebuilding the selected own Qt observer from its frozen source produced a byte-identical module. The public checkout intentionally excludes OEM inputs and the private VM.

The validated profile still uses original Qt 5.4, software Mesa, the disclosed genuine-reply timing tolerances and laboratory IVI adaptation. Original 1920×720 Home content is fitted to 1280×730 inside a 1280×800 output; the aspect ratio is adapted. Original texture pixels are decoded for software fallback, not rendered through native ASTC support. The [original round-trip report](PROGRESS-2026-11-06-ORIGINAL-RADIO-ROUNDTRIP.md) explains the causal input guards and real OEM replies.

Original Spanish catalogs remain unchanged. This result does not establish RF tuning, audio, DAB reception, working navigation/maps, GNSS, modem/cloud services or guest GPU acceleration. The guest remains offline.

## Windows follow-up in progress

A separate user-mode launcher has now started another new overlay through native Windows CMD → WSL. It is being validated, and has not replaced the owner's canonical launcher yet. Its initial viewer is read-only while the native cycle is checked; afterward the automatic pointer actions end and a bounded operator window begins. PID/start-time/command/profile checks prevent adoption or stopping of an unrelated test. Synthetic ownership, transport, viewer and handoff checks pass, and Windows can reach the local viewer status endpoint.

Next: verify actual operator input, a further original Radio/Home cycle and clean stop from Windows, then consolidate the existing launcher. Later work remains modular: original N Mode/other applications, offline navigation and observed vehicle-interface contracts. No firmware, binaries, QML, translations, maps, textures, private traces, cores or screenshots are included with this report.
