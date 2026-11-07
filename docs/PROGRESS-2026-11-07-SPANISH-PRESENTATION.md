Newer result: [bounded post-cycle stability and Windows follow-up](PROGRESS-2026-11-07-SPANISH-STABILITY.md). The pending stability statements below describe the earlier checkpoint.

# Original Spanish UI, repeated cycle and remaining presentation limits — 7 November 2026

Original Home and Radio now visibly use their original Spanish translations. Another clean-overlay run completed the causal application cycle and post-return page navigation. Direct comparison of the saved PNG pixels corrects the earlier partial-frame interpretation: these Home frames are complete and aligned. Post-cycle ten-minute stability has not yet been completed.

## Verified Spanish evidence

The observed language 7 Spanish(EU) input is propagated by original AppLauncher. A laboratory observer passes through original Qt open64 calls, preserving their descriptor, file offset and errno, then records successful catalog opens and fstat sizes. Home opens its original translation_es.qm (219,588 bytes), Radio its original AppEURadio_es_ES.qm (13,627 bytes), and original Spanish Standby/widget catalogs are also opened. No catalog was edited or rebuilt. Earlier private file-only strace evidence independently recorded the principal Home/Radio catalog paths.

In private run 20261106T233319Z-replay-b84de8-1, Home visibly shows original Spanish labels including Teléfono, Climatización and Ajustes. Radio visibly shows Lista FM and Emisora, plus the original Spanish explanatory text. Screenshots, traces and catalog contents stay private. The native 0.0 MHz placeholder is not evidence of RF reception or an invented station.

The same run completed original Confirm, Home page 0→1, foreground original Radio77, genuine Radio input and its Home transition request, original manager acknowledgment and final drawn/managed 11/11. Home and Radio retained their original PIDs without an observed AppKill/watchdog before clean shutdown. Home was complete and aligned at the 40-second post-input observation; a real further drag completed page 1→0 and the final image showed aligned Spanish Home. The [previous English cycle and its adaptations](PROGRESS-2026-11-06-ORIGINAL-RADIO-ROUNDTRIP.md) remain preserved separately.

## Correction of the earlier visual interpretation

An earlier version of this report described an intermediate Home image as partial. That interpretation was wrong and is explicitly retracted. The original private PNG files have not been altered.

In run 20261106T235700Z-replay-42154f-1, the two sampled menu-page images during monitoring are byte-identical to the complete aligned Home return image; decoded RGB differences are zero. In Spanish run 20261106T233319Z-replay-b84de8-1, the allegedly partial intermediate image differs from the complete return image only in the small bottom page indicator, with an otherwise identical menu region. All eight original icons and labels are present at their expected positions. Private hashes and numerical comparisons preserve this correction.

Logical state alone still does not prove presentation, and sampled full frames do not establish continuous long-term fidelity. However, these specific files do not demonstrate the reported partial-frame fault. Do not spend more experiments fixing that mistaken finding or attribute it to Qt, ASTC, translation or Weston.

## Observation failures distinguished from OEM failures

One earlier Spanish trial was censored by the controller's Home release deadline. Its console later contained the valid original release acknowledgment. A separate bounded observer window was added; the subsequent successful run observed its initial release in 29.2 seconds, so that run alone does not demonstrate that a longer window was necessary.

The first post-cycle stability attempt completed another cycle and sampled all six original participants alive: AppLauncher, ApplicationManager, Home, Radio, MICOM and Weston. Its new live-query monitor then timed out because the cursor was already at exactly the submitted absolute coordinates. No new MouseMove was generated. The monitor now alternates nearby harmless pointer positions for its own queries; a wholly synthetic transport regression test reproduces the no-event behavior at unchanged coordinates and verifies the correction. This is a monitor fix, not an OEM success reply.

The corrected monitor's next run completed another original Spanish application cycle and further native Home page changes. Four samples over approximately 192 seconds retained all six original process identities with constant measured RSS. It was stopped cleanly by the investigator after the mistaken visual interpretation described above. This was not a spontaneous OEM failure, and it is not a completed 600-second stability result. A repeat with direct checks of saved pixels is justified; no new graphics correction follows from this evidence.

## Next diagnostic and usability work

A separate private pixel observer is being validated to corroborate original client content. It passes through genuine EGL swaps and reads only the same original Home process's CPU buffer, with exact original library/layout guards, fixed dimensions, bounded output and at most three samples. It performs no GL readback or state change. The first guest observer exposed a laboratory symbol-resolution defect and is not an OEM failure result. The correction delegates through an explicit handle to already-loaded original EGL when a Qt local plugin scope hides it from RTLD_NEXT; it does not load or promote another library. A synthetic local-dependency test checks original return and errno preservation. Actual guest buffer capture remains unverified. Never publish captured buffers.

Existing Windows launchers have been inspected. They use an earlier profile; consolidation remains pending after the functional profile is sufficiently validated. No installer was rerun and no original/reference disk was replaced. The guest remains offline; no vehicle/CAN, cloud service, modem or navigation claim follows from these UI results. No OEM binaries, firmware, QML, translations, maps, textures, raw traces, cores or screenshots accompany this report.
