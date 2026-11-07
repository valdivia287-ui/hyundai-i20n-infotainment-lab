# Original N Mode Track, MY23 scope and application audit — 7 November 2026

## Verified UI result

The owner confirmed a **BC3N Hyundai i20 N MY23, Spain/Europe**, with vehicle software last updated in 2025. Update year does not establish model year. BC3N25MY is not selected as this vehicle's identity.

In separate offline overlays, original AppLauncher/ApplicationManager accepted the previously observed N Mode request `(304,500,5185,1,0)`. The original Track interface rendered inside AppHomeScreen using `nm2/pf0`, European region 5 and SpanishEU language 7. Both original Spanish dashboard pages were visible. A real VNC horizontal gesture changed pages; the native Home control returned to the complete aligned Home menu, and a further native page gesture returned to Home page0. Final Home pixels differ from the initial reference only inside the page-indicator rectangle.

The latest closed private reference is `20261107T103656Z-replay-c9f2c2-1`. Actual Home owned IVI 1001; observation now matches geometry and frame evidence to the live original executable/PID instead of assuming a fixed surface ID. Five original process identities were retained. All 67 screenshot exports have matching local hashes and verified secondary Windows copies. Shutdown was clean. A premature gesture and intermediate animation frames are retained privately and excluded from successful-navigation evidence.

## Original textures and explicit limits

Sixty-six further actually requested original N Mode textures were decoded on CPU to PNG, in addition to the earlier 21. All 132 added source files matched the immutable base, and 66 PNG/RGBA pixel roundtrips passed. One other requested header/compressed-data pair was empty in the base; it was excluded and left untouched. A recovered copy is not silently substituted for an unmatched base source. This is decoded original Hyundai imagery, **not native ASTC rendering**. No texture, archive, screenshot or trace is distributed here.

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
| Manual inside Home | Original Spanish text and EU/Spanish QR visible offline | Return not yet verified; not separate AppUserManual 18. QR destination not opened |
| Voice Memo 117 | Original provider registration observed; initial screen reviewed | Separate individual GUI trial underway; no record/play/delete |

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

Next: complete individual Voice Memo and Manual return trials in new offline overlays. Analyze actual dependencies before further adapters. Preserve functional references and close each owned VM cleanly. Keep firmware, maps, QML, binaries, assets and private evidence outside this public repository.
