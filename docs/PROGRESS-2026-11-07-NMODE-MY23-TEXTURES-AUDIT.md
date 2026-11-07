# Original N Mode Track, MY23 scope and application audit — 7 November 2026

## Verified UI result

The owner confirmed a **BC3N Hyundai i20 N MY23, Spain/Europe**, with vehicle software last updated in 2025. Update year does not establish model year. BC3N25MY is not selected as this vehicle's identity.

In separate offline overlays, original AppLauncher/ApplicationManager accepted the previously observed N Mode request `(304,500,5185,1,0)`. The original Track interface rendered inside AppHomeScreen using `nm2/pf0`, European region 5 and SpanishEU language 7. Both original Spanish dashboard pages were visible. A real VNC horizontal gesture changed pages; the native Home control returned to the complete aligned Home menu, and a further native page gesture returned to Home page0. Final Home pixels differ from the initial reference only inside the page-indicator rectangle.

The latest closed private reference is `20261107T103656Z-replay-c9f2c2-1`. Actual Home owned IVI 1001; observation now matches geometry and frame evidence to the live original executable/PID instead of assuming a fixed surface ID. All five monitored process identities were retained: four OEM processes (Launcher, ApplicationManager, Home and MICOM) plus Weston. All 67 screenshot exports have matching local hashes and verified secondary Windows copies. Shutdown was clean. A premature gesture and intermediate animation frames are retained privately and excluded from successful-navigation evidence.

## Original textures and explicit limits

Sixty-six further actually requested original N Mode textures were decoded on CPU to PNG, in addition to the earlier 21. All 132 added source files matched the immutable base, and 66 PNG/RGBA pixel roundtrips passed. One other requested header/compressed-data pair was empty in the base; it was excluded and left untouched. A recovered copy is not silently substituted for an unmatched base source. This is decoded original Hyundai imagery, **not native ASTC rendering**. No texture, archive or trace is distributed here. Two owner-approved lossless screenshots of the rendered N Mode pages, plus one Home-return frame, are published in the [curated image set](images/2026-11-07/README.md); they do not include the decoded texture sources.

The original BC3 configuration row supplies `nm2/pf0`; that supports the frontend comparison, not a complete MY23 vehicle identity. The existing boot fixture still reports CarType 0/LX2. Existing explicit frontend BC3 configuration, local writable Qt N-capability adaptation, timing/IPC adaptations and software compositor remain in use. No new CAN/MICOM/D-Bus replies, sensor values or real-vehicle interactions were added. N Mode QML remains original. Dynamic readings/defaults are not vehicle measurements. Launch Control, Custom settings, recording and driving controls were not activated.

N Mode remains **partial, with a verified two-page UI round trip**. This does not establish full vehicle integration, guest GPU acceleration, audio or a new ten-minute stability result. Spain-specific country configuration, OEM time-zone/DST handling and the exact complete physical-model profile remain separately unverified. Previous stable Home/Radio and legacy N Mode references remain preserved.

## Expanded application audit

| Interface/provider | Observed result | Remaining limit |
| --- | --- | --- |
| Standby 10, Home 11, European Radio 77 | Earlier original GUI cycles verified | No RF/audio/full vehicle claim |
| N Mode 500 | Track pages, mouse, native aligned Home return | Explicit frontend adaptations; hardware unavailable |
| BluetoothHMI 121 | Genuine original on-demand startup and registration | Manager Peer.Ping timeout/kill before operator interaction; repeated missing persistence-file accesses observed, causal contribution not isolated |
| Phone projection | Native Home reports CarPlay=false and AndroidAuto=false, then original popup | No process/surface transition; no setting or phone invented |
| AppMediaPlayer provider | Original startup exit 127 traced to absent temporary libtse provider link; separate runtime profile links the hash-verified original45-step OEM library | Original process survives and registers logical 101/102/117/270, but generic Medios opens no UI. No audio or playable-source claim |
| Manual inside Home | Complete original Spanish text/QR, native Back to aligned Home menu and further Home page navigation verified | Integrated Home11 subview, not separate AppUserManual18; QR destination not opened |
| Voice Memo 117 | Native Home117/28 reaches original provider requestShow and response1; no visible UI | Surface exists but has no buffer; manager rolls back after 45s. Passive later runtime tracing is the next diagnosis. No record/play/delete |

The media runtime link is temporary and overlay-local, following the observed OEM 45/75-library selection mechanism. It does not establish which physical amplifier variant the vehicle uses and supplies no AMP or hardware reply. Logical registration alone is not a usable GUI application.

Static audit identifies 35 deduplicated Launcher entries and 154 manager logical entries. These are metadata, not 189 independent usable apps. Nineteen declared Launcher executable paths exist and sixteen do not in the inspected base. Integrated providers and archived alternatives require separate review. Engineer/dealer/diagnostic/update/flashing routes remain excluded. Settings submenu is not AppSetup 60.

## Reproducible own tools

```sh
python3 -m unittest discover -s tests
python3 tools/verify_nm2_evidence.py /private/path/to/completed-nm2-run
python3 tools/inventory_manager_apps.py /private/ApplicationManager /private/disassembly.txt /private/new-inventory.json
```

The verifier requires Pillow and completed private evidence; visual review remains mandatory. The manager extractor is guarded to the specifically reviewed binary hash and constructor layout. It never executes OEM code and retains unknown fields without invented semantics. Its output should remain private.

`tools/layout_evidence_match.sh` is an original pure observation predicate. Synthetic tests cover reordered surface allocation and reject wrong owners, PIDs, frame IDs/ticks, clipping, scale and hidden surfaces. It neither changes the compositor nor sends input. No OEM trace fixtures are included.

Next: resolve the Voice Memo presentation blocker in a separate offline overlay; the corrected Manual return trial is now complete. Analyze actual dependencies before further adapters. Preserve functional references and close each owned VM cleanly. Keep firmware, maps, QML, binaries, assets and private evidence outside this public repository.

## Additional closed audit evidence

The corrected Manual interaction trial `20261107T110014Z-replay-858e71-1` waited for the complete original Spanish QR/text before using the native Back arrow. The full Home menu returned aligned; only six antialiasing pixels differed from its initial menu reference. A further real VNC drag returned to Home page0, matching the initial page except for the indicator. All 57 screenshot copies were verified and shutdown was clean. Existing original QML warnings were retained; no QML or translation was edited and no QR URL was opened. This verifies another original integrated subview, not an additional standalone executable.

The separate Voice Memo trial `20261107T105125Z-replay-e8bd69-1` retained original AppMediaPlayer through 97 health samples without AppKill. Its own IVI surface was present, but all 65 sampled existing-surface frames had buffer0x0, no layer and no visibility. Native Home item22 emitted `(304,117,28,1,0)`; original requestShow/response1 did not complete the drawn transition. Original manager intent was117 while drawn application remained11, followed by 45s rollbacks. Home stayed usable and returned to page0. This is a concrete missing-buffer/acknowledgment observation, not proof that ASTC or absent physical hardware caused it. The earlier 18s launcher-child trace did not cover this later period; a separately enabled passive runtime trace is being evaluated.

Correction of monitoring terminology: the five-process no-Radio baseline includes Weston. It does not establish the health of five OEM applications or monitor Standby. Individual process identities remain explicit in private evidence.

A subsequent closed runtime-only diagnostic attached after the original startup tracer had detached. It confirms the original Voice Memo QML is instantiated, the original playback/list screen is selected and `QMLController::showView()` runs. The actual MediaPlayer renderer is llvmpipe, LLVM3.9, GLES3.0/Mesa13.0.6. The GUI thread continues responding, while the sampled IVI surface has no attached buffer. Missing persistence files and ASTC warnings are observed, but neither is established as the cause. The next isolated observation measures original Qt window geometry, visibility and exposure without setters, new protocol replies or a forced foreground transition.
