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

The isolated owner-based callback rescue was extended to hidden Radio in `20261101T165216Z-replay-64caa7-1`. It delivered Radio's pending callbacks, and genuine Radio Ping replies and unchanged Home/Radio PIDs were observed. This separates a liveness improvement from functional input: in the same run the apparent Home button was retained output, with no active compositor view to receive the click. Manager getters still said77/77.

## Genuine return and geometry limitation

`20261101T170454Z-replay-9f6182-1` provided stronger evidence. A Station list click caused original Radio to load its DAB station-list QML components, although their content did not render correctly. The original Home button then emitted **`(304,11,30,1,0)`**; Home acknowledged **ret1**, and subsequent original manager readings agreed on **drawn11/managed11**. Home and Radio kept the same PIDs, with no observed manager AppKill during the bounded workflow.

An earlier +20s reading still reported77/11 before completion; the later readings must be used to assess the completed transition. This is evidence of the real OEM return path, **not a complete usable loop**: Home's destination became1920×720 on the1280-pixel output, cropping its icon page.

A read-only observer of genuine manager getters was present, but the experimental foreground repair emitted no activation. Do not credit the return to an unused repair. Subsequent geometry trials also emitted no correction marker; one returned to cropped Home, while another never generated a Home request because Radio had no interactive view. The latter did not exercise the geometry hypothesis at all.

The next diagnostic instruments each adapter guard and correlates manager state, actual listed views and pointer delivery. A visible retained control and a positive drawing getter are insufficient evidence that a click reaches an application.

## Cursor falsely counted as foreground

The instrumented adapter trial `20261101T173821Z-replay-5a7808-1` read authentic, fresh manager state correctly and found Radio's visible buffer. It refused to repair the layout because it counted one other OEM-owned view, although all three main application surfaces were parked.

`20261101T174549Z-replay-c1dad9-1` identified that view as a **10×16 cursor surface**, owned by Home or Radio but **not registered with IVI**. Restricting the count to registered IVI application surfaces allowed the repair to activate for Radio and restore its listed view. This corrects a laboratory guard; it is not a change to an OEM app, manager response or vehicle state. Cursor ownership alone must not qualify a view as a foreground application.

Input still requires separate verification. In `20261101T175403Z-replay-bb5179-1`, the original Radio Qt window received the actual mouse sequence at the visible Home control. Two enabled mouse areas with valid QML contexts processed the press, and Home genuinely acknowledged the original return request. However, the manager rolled back the transition at approximately ten-second intervals, while the IVI Home foreground notification arrived after the first rollback. Final getters remained drawn77/managed11. The observed timing mismatch warrants identifying the exact original deadline; it does not prove that extending every timer would solve the problem. This run skipped Station list because its FM panel was not detected.

## Spanish European startup selection

A separate short startup `20261101T180255Z-replay-9e5adf-1` tested the statically identified Spanish European language value through a labelled synthetic MICOM boot-information input. Original AppLauncher reported **Spanish(EU)** and launched original Home, Standby and ApplicationManager with **`-l:7`**. This verifies the OEM selection path, **not yet Spanish text throughout the UI**, correct BC3N capability options, radio tuning or navigation.

The target remains Spain/Europe, including European FM and DAB/DAB+, separately verified GNSS/navigation and original timezone integration. Runtime Radio tracing confirms an attempted open of the absent DAB device; its hardware protocol still needs analysis before implementing synthetic responses.

## Next controlled interaction

Observe original Radio's actual D-Bus and device calls across startup and Home entry. Click Station list and the original Home control only after checking the visual control, genuine manager state and an actual input-eligible compositor view. Keep original service lifetimes sufficient for the bounded workflow so a scheduled service exit cannot be confused with an OEM failure. Require actual input effects, manager transition, visible Home and stable processes before claiming a complete Home→Radio→Home cycle.

FM tuner responses, audio, DAB/DAB+, virtual GNSS, original navigation/maps, Spanish-language selection, original timezone integration and the consolidated Windows launcher remain separate tasks. Europe selection alone is not a complete Spanish-market BC3N configuration.
