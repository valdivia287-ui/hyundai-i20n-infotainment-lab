# Original clock service and remaining integration work

The original TimeManager now registers its actual session-bus service and supplies date/time to original Home in an isolated offline development VM. Home changed from time placeholders to the real VM clock and original Spanish date formatting. This is a shared-service advance, not full Spanish vehicle configuration or completion of Settings.

## Verified observations

- The recovered service runs without arguments, following the original startup unit’s AppLauncher/PAS dependencies and the laboratory’s private bus addresses.
- Its actual PID owns `com.lge.car.timemanager` on the session bus. Original local-time broadcasts reach Home; no replacement clock widget or forged success response is used.
- The test supplied no additional GPS position, RTC reply or vehicle telemetry. Original MICOM RTC queries were observed; a valid hardware time response has not been verified. Existing explicitly simulated boot inputs remain separate.
- The first90-second observation ended with the programmed timeout124. A subsequent bounded exploration used the same original binary. These are controlled stops, not spontaneous process failures or a new long stability certification.

## Spain timezone is still pending

The observed clock is UTC. The guest’s original localtime link points to Universal and the inspected runtime lacks the Europe/Madrid zone file. The original systemd-timedated daemon briefly registers, then exits1 when its NTP-state query reaches the absent `org.freedesktop.systemd1` service. No fake systemd/NTP reply was added.

Static analysis identifies Europe/Madrid at direct timezone-array index146 and Atlantic/Canary at148 in this exact TimeManager build. Those are array indices, not Country/Language codes or a demonstrated runtime selection. Madrid/DST still needs a real configuration path and verification. Physical MY23/update2025 and the owner-preferred BC3N25MY software profile remain distinct.

## Graphics regression is being isolated

In the latest combined Settings experiment, the original manager selects and marks General56 drawn, but the original UI only presents an incomplete oversized first frame before an original AppKill. A fresh same-PID readiness check reproduced the stall; the captured GUI waits through Qt Quick, while the render thread passes through EGL/Mesa/Wayland. This is not evidence of a direct GPS/Bluetooth wait, and TimeManager has not been proven the sole cause.

A concrete lab-controller guard rejection was measured: original General is in front of a still-visible original Home background, but the destination fitter requires a single registered view. A separate narrow foreground-over-Home destination adaptation was tested in a new overlay. It applied1280×730 while preserving the original1920×720 source and Home properties, but the render stall persisted. After the native Settings close, Home remained alive with a detached buffer and no visible content; no Home crash is inferred. The adaptation is not a complete fix or a replacement of the accepted Windows profile. A paired fresh-boot control now omits TimeManager while retaining the same graphics, original PAS and Bluetooth provider; its result is pending. Original Settings categories verified in earlier development overlays remain preserved.

## Related results

[Bluetooth Connection Settings](PROGRESS-2026-11-08-BLUETOOTH-SETTINGS.md) now also passes a cold CPU-adapter boot, complete Spanish root, native Home return and actual native transaction checks. The first Telephone icon trial with the healthy original provider still failed to produce verified phone content; the original global Home request recovered page0 and a real drag recovered the applications page. Missing phone hardware is not asserted as the sole rendering cause. No pairing, call or external connection was attempted.

No firmware, OEM binary, QML, source texture, raw trace or additional screenshot is published with this update. The accepted launcher and frozen software profile remain unchanged.
