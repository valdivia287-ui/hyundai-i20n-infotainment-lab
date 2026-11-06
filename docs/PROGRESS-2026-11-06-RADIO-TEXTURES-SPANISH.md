# Radio artwork, Spanish catalogs and the remaining watchdog — 6 November 2026

The latest private evidence improves rendering and measurement, but does **not** demonstrate a reliable button-driven Home → Radio → Home cycle.

## Runtime verified

In `20261106T221638Z-replay-02acf6-1`, a private overlay installed 60 previously observed original Radio/shared textures decoded from ASTC/LZ4 into PNG. All 120 source-file checks and 60 output checks passed. The decoder preparation had already checked dimensions and lossless PNG/RGBA roundtrip. Original headers are retained inside the disposable overlay; original firmware and reference disks remain intact.

Original AppEURadio now visibly draws its frequency tubes at 0.0, seek/favorite controls and background. These are **decoded original Hyundai textures**, not recreated images, native OEM ASTC rendering, working RF hardware or invented stations. Some elements/transitions are still incomplete.

Original Home was complete and aligned after Radio disappeared, with its source 1920×720 fitted to the laboratory destination 1280×730. A real post-return drag changed the original ListView from page 1/contentX 1920 to page 0/contentX 0; a fresh GUI-thread read reported no movement and the final capture showed aligned page zero. This is a verified Home recovery/navigation result, with experimental timing/compositor adaptations and nonnative aspect ratio.

## The return must not be credited to the button

Correlating the manager trace changed the interpretation: original Radio accumulated `Peer.Ping` NoReply responses, the original manager's APP_DAB alive counter reached 6, and it killed Radio. Radio deregistration was followed by a Home restore with reason 30. AppLauncher relaunched Radio. The observed window did not provide Radio mouse events or an inbound transition request proving that the Home button caused that return.

**This is watchdog recovery, not a validated interactive round-trip or stability result.** Radio's underlying blocking call remains to identify. The next private diagnostic is explicitly labelled: obtain a process core only after an actual failed Ping, then inspect the original threads and dependencies. Any deliberately triggered abort must be distinguished from a spontaneous crash.

## Spanish original catalogs

`20261106T222921Z-replay-fb7d23-1` supplied the observed language 7 Spanish(EU) contract through the synthetic MICOM input. File-only tracing recorded successful access/stat/open of:

- Home: `/app/share/AppHomeScreen/localization/qm/translation_es.qm`, 219,588 bytes.
- Radio: `/app/share/AppEURadio/localization/AppEURadio_es_ES.qm`, 13,627 bytes.

The Home capture visibly says **“Medios apagados”**. Radio's Spanish catalog was opened, but translated Radio text was not visually verified in that trial. Standby was restarted and Confirm did not reappear; the controller correctly sent no click. Catalog presence, successful opening, translated text and a functional navigation cycle are separate claims. No original translations were edited or rebuilt.

## Laboratory changes and validation limits

The earlier [animation-clock investigation](PROGRESS-2026-11-06-HOME-ALIGNMENT.md) remains relevant. A private Home-only adaptation selects QtQuick's native timer mode; source hashes and the exact constructor query are checked. Original timing fidelity is not restored. The inherited BC3 variant-selection override remains in use; this alignment work makes no new OEM QML edits.

A sample-HMI relayout competes with the original IVI window manager. Disabling those example relayouts from boot prevented initial buffers, so that variant was rejected. A separate candidate preserves bootstrap and yields later relayouts only after Confirm is visibly available. It remains experimental.

The controller now waits for actual original ListView release processing, rather than starting every delay at QMP input submission. Read-only layout and visual-tree probes distinguish native page state from the frame currently displayed. One intermediate capture was still partial despite settled properties; getters alone do not prove presentation. The initially attempted QObject-tree lookup failed and was corrected to use the QtQuick visual tree. No application properties are set to manufacture a test result.

## Next work

1. Capture Radio's real blocked-thread state during NoReply and fix the demonstrated cause.
2. Verify the original Radio Home control without a watchdog restart and repeat the aligned page change.
3. Visually verify original Spanish Radio text and repeat the complete Spanish flow.
4. Only then run the ten-minute stability check, repeat from another clean overlay and consolidate the Windows launcher.

Static offline navigation inventory located the original AppNavi engine and PRM6/EUR configurations. It has not established usable Spanish map datasets or valid local licenses. GNSS, blocked-egress network observation and the guest GPU bridge remain separate pending work. The functional trials keep networking disabled; no physical vehicle/CAN or Hyundai online service is used.

No new screenshots, traces, cores, firmware, OEM binaries, QML, maps or decoded assets are published with this report. Private evidence and the last working references remain preserved.
