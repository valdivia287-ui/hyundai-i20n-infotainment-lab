# Original Spanish UI, repeated cycle and remaining presentation limits — 7 November 2026

Original Home and Radio now visibly use their original Spanish translations. Another clean-overlay run completed the causal application cycle and post-return page navigation. An intermittent partial Home frame remains; post-cycle ten-minute stability has not yet been measured successfully.

## Verified Spanish evidence

The observed language 7 Spanish(EU) input is propagated by original AppLauncher. A laboratory observer passes through original Qt open64 calls, preserving their descriptor, file offset and errno, then records successful catalog opens and fstat sizes. Home opens its original translation_es.qm (219,588 bytes), Radio its original AppEURadio_es_ES.qm (13,627 bytes), and original Spanish Standby/widget catalogs are also opened. No catalog was edited or rebuilt. Earlier private file-only strace evidence independently recorded the principal Home/Radio catalog paths.

In private run 20261106T233319Z-replay-b84de8-1, Home visibly shows original Spanish labels including Teléfono, Climatización and Ajustes. Radio visibly shows Lista FM and Emisora, plus the original Spanish explanatory text. Screenshots, traces and catalog contents stay private. The native 0.0 MHz placeholder is not evidence of RF reception or an invented station.

The same run completed original Confirm, Home page 0→1, foreground original Radio77, genuine Radio input and its Home transition request, original manager acknowledgment and final drawn/managed 11/11. Home and Radio retained their original PIDs without an observed AppKill/watchdog before clean shutdown. Home was complete and aligned at the 40-second post-input observation; a real further drag completed page 1→0 and the final image showed aligned Spanish Home. The [previous English cycle and its adaptations](PROGRESS-2026-11-06-ORIGINAL-RADIO-ROUNDTRIP.md) remain preserved separately.

## Do not hide the partial frame

Between complete return and final page-zero images, another capture showed only the Radio icon. Read-only geometry still reported source 1920×720, destination 1280×730, opacity 1, correct transform and a settled original ListView. Nearby registered Standby/Radio surfaces were invisible with no buffer in the sampled scene. Those observations narrow the question, but do not prove whether the client buffer, upload or final composition produced the partial frame. Do not attribute it to translation, ASTC or hardware without further evidence.

The full/aligned frames and successful input are real; continuous visual fidelity remains unresolved. The emulator is not finished.

## Observation failures distinguished from OEM failures

One earlier Spanish trial was censored by the controller's Home release deadline. Its console later contained the valid original release acknowledgment. A separate bounded observer window was added; the subsequent successful run observed its initial release in 29.2 seconds, so that run alone does not demonstrate that a longer window was necessary.

The first post-cycle stability attempt completed another cycle and sampled all six original participants alive: AppLauncher, ApplicationManager, Home, Radio, MICOM and Weston. Its new live-query monitor then timed out because the cursor was already at exactly the submitted absolute coordinates. No new MouseMove was generated. The monitor now alternates nearby harmless pointer positions for its own queries; a wholly synthetic transport regression test reproduces the no-event behavior at unchanged coordinates and verifies the correction. This is a monitor fix, not an OEM success reply.

A fresh bounded trial is executing with 600 seconds requested after the cycle, explicitly provisioned service lifetimes, PID/starttime/RSS sampling and additional real Home drags. It must not be credited with ten-minute success until it completes. Radio is retained in the background during that phase; repeated Radio foreground cycles are a separate validation claim.

## Next diagnostic and usability work

A separate private pixel observer is prepared for the partial-frame investigation. It passes through genuine EGL swaps and reads only the same original Home process's CPU buffer, with exact original library/layout guards, fixed dimensions, bounded output and at most three samples. It performs no GL readback or state change. Synthetic host memory/file checks pass; actual guest capture is not yet verified. Never publish captured buffers.

Existing Windows launchers have been inspected. They use an earlier profile; consolidation remains pending after the functional profile is sufficiently validated. No installer was rerun and no original/reference disk was replaced. The guest remains offline; no vehicle/CAN, cloud service, modem or navigation claim follows from these UI results. No OEM binaries, firmware, QML, translations, maps, textures, raw traces, cores or screenshots accompany this report.
