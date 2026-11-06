> Newer evidence: [Radio artwork, Spanish and watchdog](PROGRESS-2026-11-06-RADIO-TEXTURES-SPANISH.md). The later observed Home recovery followed Radio death; do not treat it as a validated button-driven round-trip.

# Home alignment after European Radio — 6 November 2026

The multimedia emulator remains experimental. Original applications run with private OEM inputs and explicitly labelled laboratory adaptations; a repeatable, fully interactive cycle is not yet validated.

## Verified private runtime evidence

`20261106T200006Z-replay-52b018-1` showed original Confirm, a trace-confirmed original Confirm click, Home, a real drag to its Radio icon, original AppEURadio77 FM and Station List, an authentic Home-return request and original manager acknowledgment. After a further Home gesture, its original QML reported page zero, but the last image remained between pages. Logical state is therefore insufficient evidence of completed rendering.

An exact subsequent replay did not reproduce the full cycle: Radio was killed/relaunched by the manager and its Home control was not detected. The input guard correctly skipped that click. The reason for that particular manager kill is not yet established.

## Separating compositor geometry, animation time and input

Read-only laboratory probes now record Home's IVI source/destination rectangles, layer and view transformations, plus the original ListView's `currentIndex`, `contentX`, dimensions and motion flags. Original content is 1920×720; QEMU output is 1280×800 with a laboratory destination of 1280×730. This fits the viewport with nonuniform scaling; it does not reproduce the physical panel's native aspect ratio.

In `20261106T204901Z-replay-52ac9d-1`, one sampled Qt animation interval advanced 13 ms while the driver's monotonic base advanced 10,210 ms. Other intervals recovered. Across eight eligible sampled intervals, two had less than half the corresponding base-clock progress. This is a measured timing discrepancy, not proof that every transition problem shares that cause.

A separate HMI experiment that deferred reference relayout on an active OEM surface's null-buffer configure did not resolve the return. It remains disabled in the following experiment.

`20261106T210804Z-replay-f250f0-1` selected QtQuick's existing timer mode only for Home's scenegraph animation-driver construction. A private opt-in preload checks the exact original QtQuick hash and alters only that constructor's refresh-rate query; other screen queries retain their value. Original QML, ListView properties and animation-step arguments are not edited. The original Qt sources explain this mode selection ([QtQuick 5.4.1](https://raw.githubusercontent.com/qt/qtdeclarative/v5.4.1/src/quick/scenegraph/qsgcontext.cpp), [QtCore 5.4.1](https://raw.githubusercontent.com/qt/qtbase/v5.4.1/src/corelib/animation/qabstractanimation.cpp)); no upstream implementation is redistributed here.

That trial produced an aligned Home page-zero image after Radio return. IVI showed a full buffer, correct source/destination, opacity one and effectively zero translation. Eleven eligible clock samples advanced at approximately the base-clock rate. Home and Radio retained their observed process IDs until shutdown. **However, the following rightward gesture reached different original mouse areas, not the observed Home list, and the final image lost content. This is not a validated interaction fix.** The next bounded trial uses a leftward gesture from page zero and reads the actual input receivers' geometry without changing them.

The same replay also illustrates a causality trap: Standby's automatic timer requested Home before the real Confirm click. This differs from the first November-6 reference. Record the request's original call stack before claiming that a click caused a transition.

## Remaining work

1. Explain the post-return input receiver/content loss and verify a complete visible page change after returning from Radio.
2. Validate the separately prepared private fallback for 60 actually requested Radio textures. These are decoded original images, not native OEM ASTC rendering; Mesa13 software rejects the observed ASTC formats. Texture failures and transition logic are separate findings.
3. Run Spanish(EU) with original language7 propagation, trace actual catalog opens and visually verify translated Home/Radio. Parameter selection alone is not translated UI.
4. Only after those checks, run ten-minute stability and a second clean-overlay cycle, then consolidate the Windows launcher.

The functional guest remains offline. GNSS, navigation/maps, modem contracts and a blocked-egress network-observation profile are separate pending modules. No vehicle, physical CAN, online Hyundai service, account or subscription is used.

## Public diagnostic tool

`python3 tools/qt_animation_clock_summary.py PRIVATE_PROBE_LOG` reads the laboratory probe format and prints aggregate timing counters. It skips invalid/reset intervals and gaps below100ms. Samples are adjacent-call deltas selected by the probe, not a complete timeline; they cannot establish total duration or causality. The tool does not print raw lines, process addresses or identifiers. Inputs remain private. Synthetic tests cover slow intervals, resets, malformed records and unrelated input.

No private traces, screenshots, firmware, OEM binaries, QML, maps or decoded textures accompany this report. Original reference overlays and prior working modules remain intact.
