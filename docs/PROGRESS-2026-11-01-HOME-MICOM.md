# Original Home startup and MICOM dependency

This checkpoint comes from local inspection of private cores and bounded QEMU trials on 1 November 2026. OEM executables, libraries, cores, UART traces and new screenshots remain private.

## Verified dependency and its limits

Original ApplicationManager sends genuine `org.freedesktop.DBus.Peer.Ping` requests to original Home. Repeated `NoReply` leads to its alive counter reaching six and an explicit Home termination. This explains the termination mechanism; it does not establish one universal cause for all Home failures.

One natural Home SIGTRAP core captured its main thread inside a synchronous Qt D-Bus wait for original MICOM `AskETCEcallStatus`. Static inspection established a one-byte result contract. Concurrent Home/MICOM traces then related the real D-Bus request to an outgoing virtual UART command. A separate, opt-in synthetic zero-status hardware response was accepted by original MICOM, which emitted its own authentic D-Bus `ay=[0]` reply. Home left that wait. No Home Ping or MICOM D-Bus response was fabricated.

**Home still restarted in this initial trial.** Removing this dependency has not yet produced stable combined Home/Radio interaction. Other pending work includes main-loop readiness, outstanding service calls and frame delivery during initialization.

An earlier deliberately generated SIGABRT core caught another Home generation in font initialization. Disassembly showed `fcntl(F_SETFD)`, not a file-lock wait. That snapshot is **not evidence of a font deadlock**. The natural SIGTRAP core and deliberate diagnostic core must remain distinct.

| Private run ID | Evidence |
| --- | --- |
| `20261101T150702Z-replay-dfda7a-1` | Natural SIGTRAP core with synchronous MICOM wait; separate deliberate SIGABRT diagnostic |
| `20261101T151720Z-replay-a56c5c-1` | Original Home sends the eCall-status query |
| `20261101T152313Z-replay-d829bf-1` | Concurrent traces associate the original query with its UART request |
| `20261101T152632Z-replay-a34722-1` | Synthetic hardware response accepted; original D-Bus reply and Home progress; later restart remains |

## Genuine Ping responses measured

A later short trial, `20261101T153703Z-replay-6d50e2-1`, confirmed the original Ping timeout is **4000 ms**. A lab preload intercepting Qt's library resolution temporarily used **30000 ms**, only for ApplicationManager's Peer.Ping to Home. Original Home replied to accumulated requests after about **36 seconds** of initialization, then answered subsequent pings in milliseconds. Matching D-Bus `reply_serial` values establish that these were original Home replies. The first requests could still expire; later replies prevented six accumulated failures. One Home registration and no manager-directed Home kill were observed in the bounded interval.

This is evidence for startup readiness/latency, not permission to claim a permanent timing fix. The final screen was still Standby. Full input/foreground transition testing continues separately; real response latency after initialization and suitability of a bounded startup grace period remain to verify.

## Continuity repair

Inspection found that legacy Windows launchers reinstalled an old bundle over advanced laboratory scripts. The advanced versions were recovered from a matching local backup after preserving the overwritten versions. Own Windows entry points now call the installed local start script directly. This prevents that overwrite path; the complete Windows start/use/stop cycle has not yet been validated.

Functional benchmarks remain preserved: original Home navigation in `20261030T020654Z-13522-1`, and genuine Confirm-driven return followed by Home page navigation in `20261101T095842Z-17749-1`. The latter still needs experimental 45-second Standby timing and compositor foreground repair. Original FM rendering in `20261101T142059Z-replay-8a6447-1` remains evidence of Radio pixels, not stable Home→Radio→Home, tuning or audio.

## Spain/Europe target

The intended vehicle is the Spanish-market BC3N Gen5W_L. The tested MICOM country selection identifies **Europe**, without demonstrating Spain-specific selection. Spanish UI language, European FM/DAB, European/Spanish maps, virtual GNSS, modem/SIM and OEM timezone integration remain separate validation tasks. Host `Europe/Madrid` timezone conversion was checked across winter, summer and both 2026 DST transitions; that does not prove original TimeManager is configured.

## Next experiments

Extend the successful short timing diagnostic to real Confirm, Home navigation and Radio input. Any timing adjustment must be opt-in, report the original timeout, preserve real requests/replies and remain outside functional references. A first ordinary libdbus interposition attempt did not activate because Qt resolves the library dynamically; its result cannot reject the timing hypothesis. The later QLibrary-resolution probe activated successfully; keep its result separate from the ineffective ordinary interposition attempt.

Continue Radio interaction only after Home survival is understood. Validate foreground manager state, stable PIDs, real input, application response and return separately. No real vehicle, physical CAN, cloud identity or official subscription is simulated.

The new public `tools/uart_framing.py` is original, device-independent framing code with arbitrary synthetic-ID tests. It contains no captured vehicle data or OEM application resources. Private request-specific fixtures and diagnostic captures are not included.
