# Hidden Home during original Radio preload

Locally inspected private QEMU evidence, 1 November 2026. This continues the [MICOM/startup investigation](PROGRESS-2026-11-01-HOME-MICOM.md). Original firmware, logs, cores and new captures remain private.

## Distinct failures, distinct evidence

The synthetic eCall hardware response removed one demonstrated synchronous MICOM wait. A longer genuine Ping timeout helped initial Home readiness. Neither alone fixed the combined Radio profile: `20261101T153957Z-replay-6eb090-1` still saw manager-directed Home termination and an AppEURadio segmentation fault during its termination path. No stable Home→Radio→Home was established.

The next natural Home core, from `20261101T154831Z-replay-9f2e36-1`, shows another failure mechanism: the main thread waits on Qt Quick's render thread; that thread waits in Wayland/Mesa software buffer update. Its throttle callback remains outstanding, with only one of four buffers marked locked. Concurrent compositor telemetry shows a pending Home frame callback while Home is excluded from the active view list in hidden layer4000.

This extends the hidden-frame problem already investigated on 31 October to the newer original Radio preload sequence; it is not a new universal diagnosis for every application.

## Surface ownership must be measured

Wayland client credentials and guest process names identified **Home1000, Standby1001, Radio1002** in this run. The prior launcher/foreground reference expected **Standby1000, Home1001**. Startup order or a fixed ID is therefore insufficient to identify the current application.

A separate experimental compositor module now finds Home by its actual client process, delivers its pending callbacks only when parked outside the active view list, and requires an observed Standby/Radio foreground view. It does not answer D-Bus Ping, change OEM executables or move the foreground surface. The original reference module is preserved unchanged.

## Bounded result and remaining interaction issue

`20261101T155341Z-replay-bb9619-1` kept the same original Home process and observed no manager-directed Home or Radio termination before requested shutdown. Original manager reached standby12/drawn11/managed11. An offline correlation of visible D-Bus headers matched **14 genuine Home returns against 20 observed requests**, median **1.57s**, maximum **13.08s**. Six unmatched requests are **not six proven timeouts**: truncated/coalesced trace records limit this analysis. The tested 30s diagnostic Ping tolerance remained enabled.

The final image still did not establish navigable Home. In the later Confirm trial `20261101T155957Z-replay-54a793-1`, Home remained alive and its actual surface became listed on active layer102. The new optional owner-based foreground repair emitted no activation marker: **do not credit that repair with the foreground change**. Home's image was partial and the drag did not yet demonstrate a page change. Additional input/focus tracing is required.

The Radio-click guard in that trial skipped input because its console query could not find `timeout` in PATH, **not because a successful query proved Home absent**. The regular query script reported drawn11. The controller PATH was corrected, and the next test records original Home Qt mouse delivery and compositor pointer focus, without clicking Radio. An earlier diagnostic also aborted because its own `pidof` check treated “Home not started yet” as fatal; that instrumentation failure is explicitly excluded from OEM conclusions.

## Original Home input now traced

`20261101T160840Z-replay-580aa1-1` identifies pointer pick/focus on original Home, receives original Qt press/move/release events, and records original `advancedModePageChange(1)`. Its image shows genuine page-one icons entering the screen, still horizontally displaced. This proves delivery and a logical page transition, but not a fully settled page or usable Radio. No Home/Radio manager kill was observed before shutdown.

The same trace identifies two unsupported ASTC6×6 split backgrounds outside the established fallback asset set. A separate private overlay experiment decodes only those observed originals with the existing verified decoder and validates lossless PNG pixel round-trip. It adds a later observation frame because input/page change was delayed. Whether this removes the texture errors or improves the settled image is not yet established; do not attribute all latency to ASTC.

## GNSS contract inventory

Static inspection identifies `/dev/ttyGPS` and a specific netlink interface in original LocationManager, plus Hippo/ttyhook references. NMEA formatting and CarPlay/MirrorLink forwarding functions do not prove that the physical receiver input accepts NMEA. No virtual fix, original navigation screen, licensed map access or route calculation has been demonstrated. These remain separate tasks for the Spain/Europe configuration.

## Reusable diagnostic

`tools/dbus_ping_summary.py` reads an explicitly selected caller strace offline and correlates Peer.Ping with return/error headers by connection fd and reply serial. It never connects to a bus or device. Counts cover visible complete headers only; split/truncated headers and independent processes in a combined trace require further inspection. Tests use an invented service and synthetic wire data.

Example with a private local capture:

```sh
python3 tools/dbus_ping_summary.py /path/to/private-caller.strace --service org.example.LabHome
python3 -m unittest discover -s tests -v
```

Next: verify real mouse delivery and page navigation, then genuine Home→Radio and return. Measure a bounded startup-only Ping grace period separately before attempting to restore OEM 4s timing. Do not integrate the experimental modules into preserved functional profiles or claim full multimedia stability.
