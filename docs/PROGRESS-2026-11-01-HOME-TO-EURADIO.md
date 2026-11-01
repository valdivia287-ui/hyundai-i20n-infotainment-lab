# Original Home to European Radio: verified request and foreground

This is a sanitized summary of locally inspected, private QEMU experiments on 1 November 2026. Original firmware, resources, derived images, traces, cores and new screenshots remain private. See the [hidden Home diagnosis](PROGRESS-2026-11-01-HIDDEN-HOME.md) for the preceding failure mechanism.

## Complete Home page preserved

`20261101T161617Z-replay-14f9b7-1` returned from original Standby Confirm to original Home, received a real pointer drag and logged original `advancedModePageChange(1)`. A later capture shows the complete original icon page. The same Home process remained alive, with original manager standby12/drawn11/managed11 and no observed manager-directed Home/Radio termination before requested shutdown.

This experimental European profile uses synthetic MICOM hardware inputs for Europe/power/eCall, original MICOM responses, the owner-based hidden-Home callback rescue, 30s diagnostic Home Ping tolerance, the existing 45s Standby timer adjustment and decoded original assets. Two additional split backgrounds are generated privately using the existing verified decoder, with source hashes and lossless PNG pixel round-trip checks. The established reference asset set is unchanged. The observer waited twenty extra seconds after the first drag capture: **do not attribute animation completion solely to the additional decoded backgrounds**. The traced GL invalid-format errors for those two backgrounds disappeared, while initial ASTC-header lookup/fallback warnings remained.

The original interactive reference from 30 October and the earlier Confirm benchmark remain intact. The optional owner-based foreground repair emitted no activation in these newer runs; original foreground behavior must not be credited to an unused patch.

## Real European Radio request

In `20261101T162305Z-replay-a25bbb-1`, the original Radio icon on the settled Home page sent **`(304,77,38,1,0)`** to original ApplicationManager. This is the actual observed request in the newer European profile. Earlier **`(304,70,32,1,0)`** requests belong to different configurations; neither should be assumed universal.

The original manager's drawing and managed application getters returned **77**, with app77 registered/active and app70 absent. Compositor telemetry placed original Radio's real surface on active layer102 and in the view list; Home received the original background-hide request. Reply **255** is therefore not a launch-failure diagnosis.

The twenty-second image still showed Home; the forty-second image showed Radio's original header. This proves the original request and foreground transition, while highlighting rendering/state delays. It does not demonstrate a fully usable FM panel, station tuning, audio or return to Home.

## DLT lifetime control

The laboratory previously limited original DLT to 90s; it exited with the expected timeout code124 during the longer workflow. A controlled trial `20261101T163224Z-replay-befd88-1` changed only its lifetime to420s. After the real Home Radio request, its twenty-second capture showed original **FM / Station list / favourites** content, but its forty-second capture again retained only the original header. Home and Radio were not observed being killed by the manager during this trial, and manager getters remained77/77.

Compositor timer intervals remained variable. Keeping DLT alive is useful for service continuity, but **this trial does not establish DLT expiry as the sole cause of the incomplete/unstable Radio panel or delayed rendering**.

## Return attempt and remaining regression

`20261101T164142Z-replay-38c1fc-1` skipped Station list because the FM panel was not detected. It did detect the original Home control and confirmed Radio drawn77 before clicking. Home became visible, but the manager later reported drawn77/managed11, so the transition was not consolidated. Radio was explicitly killed by the manager: a real SIGTRAP preceded the secondary segmentation fault. Compositor telemetry showed Radio parked in layer4000 with an outstanding callback and no listed view for about twenty seconds before that kill.

Home's destination also changed to1920×720 inside the1280-pixel output and cropped part of its page. This run is **not a stable, correct-geometry Home→Radio→Home benchmark**. Preserve the earlier complete Home profile separately.

A new, isolated module trial extends the already tested owner-based callback rescue to hidden Radio and records the manager during return. It changes no OEM service reply or app binary. Its result is pending at this checkpoint.

## Next controlled interaction

Observe original Radio's actual D-Bus and device calls across startup and Home entry. Click Station list only when its FM panel is detected, then the original Home control when visibly present and manager state confirms Radio. Keep original service lifetimes sufficient for the bounded workflow so a scheduled service exit cannot be confused with an OEM failure. Require actual input effects, manager transition, visible Home and stable processes before claiming a complete Home→Radio→Home cycle.

FM tuner responses, audio, DAB/DAB+, virtual GNSS, original navigation/maps, Spanish-language selection, original timezone integration and the consolidated Windows launcher remain separate tasks. Europe selection alone is not a complete Spanish-market BC3N configuration.
