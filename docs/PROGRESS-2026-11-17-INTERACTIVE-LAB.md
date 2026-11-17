# Integrated and interactive laboratory checkpoint — 17 November 2026

## Scope

This checkpoint documents private, owner-authorised, offline QEMU development runs. It publishes only reviewed screenshots and sanitised conclusions. It does not publish Hyundai firmware, binaries, QML, textures, raw vehicle logs, core dumps, credentials, PINs or VM disks.

The accepted Windows launcher v1 remains frozen. The work below belongs to a separate development route and has not been promoted into that product.

## Integrated route

Two consecutive routes used one guest boot each and exercised 16 original views with a native Home return between them:

1. N Mode (500)
2. General settings (56)
3. Sound (50)
4. Display (51)
5. Voice (54)
6. Vehicle settings (61)
7. Theme/layout (480)
8. Keyboard/search (460)
9. Climate (13)
10. Quiet mode (368)
11. Hyundai LIVE (450)
12. Valet (29)
13. Engineering Mode password screen (301)
14. Phone-projection settings (53)
15. Voice Memo (117)
16. Bluelink/TMS provisioning (203)

The second route completed 16/16. The reviewed evidence records the request/drawing pair for each view, Home state `11/11/11` after each return, stable identities for the six sampled platform processes, no observed core, no application kill and a clean ACPI S5 shutdown. The two routes make the result reproducible within this configuration; they are not a claim of complete head-unit emulation.

## Additional accepted exploration

- **Guest profile (362):** the original Spanish Guest page opens, draws and returns to Home. Creating Driver 1/2 profiles is not accepted; that flow depends on account services and its Standby selector remained unreliable.
- **Valet (29):** after the Standby surface geometry settled, the original keypad accepted a test PIN twice and displayed `Modo aparcacoches en uso.` No secret from the vehicle is published. Persistence and the exit flow remain unproven because the harness forced Home and the guest lacks the relevant vehicle response.
- **DAB/FM (77):** the original radio page, station list and selector were exercised without RF data. A one-off destructor core from an earlier exit could not be reproduced in repeated runs; the accepted repeat returned Home with zero cores. This does not prove reception or audio.
- **General settings (56):** Version/update, System information, Date/Time, Language, Keyboard, Units, Media settings and the Latin keyboard layout submenu were navigated without changing values. Update and factory-default actions were not pressed.
- **Phone (121):** when opened first for its shared Bluetooth process, it reaches the native add-device flow. Pairing remains impossible without Bluetooth hardware and is not claimed.
- **Bluelink/TMS (203/227):** provisioning and notice views draw. Modem/VIN/verification fields remain blank or zero as expected without a modem, account or service session.
- **Engineering Mode (301):** only the password-entry screen is accepted. No password, reset, write, diagnostic or configuration action was attempted.

## Interactive wrapper

The private laboratory can now maintain the integrated guest session and expose bounded commands to open a known application ID, return Home, capture a frame, inspect status/processes and stop with a clean shutdown. A browser viewer allows mouse navigation. Startup remains approximately two to six minutes, so this is not yet comparable with the physical car's responsiveness.

One browser-wheel event was shown to crash Weston and consequently terminate Qt clients during compositor loss. The served viewer now blocks wheel events as a mitigation. The underlying Weston fault remains unresolved and the mitigation is not presented as a general fix.

## Deliberate boundaries

The guest has no RF tuner, Bluetooth radio, phone, USB media source, microphone, GPS/GNSS, cellular modem, Hyundai online services, CAN, climate controller, accelerometers or live engine/chassis signals. Views that depend on those inputs may correctly show zero, OFF, unavailable, unprovisioned or empty states. The laboratory does not fabricate cloud responses or physical sensor readings.

Screenshots demonstrate visible states, not the hardware functions named by the UI. In particular:

- DAB/FM has no RF reception or audio proof.
- Bluelink and Hyundai LIVE have no online-service connectivity.
- Phone and projection have no pairing or smartphone session.
- Climate and N Mode have no live vehicle data.
- Valet persistence/exit is not established.
- Engineering Mode is limited to the entry screen.

## Next useful work

1. Preserve the working integrated route while improving the interactive wrapper's reliability and startup time.
2. Confirm the browser wheel-event block in ordinary use and keep the underlying compositor defect documented.
3. Continue internal navigation only where it is meaningful offline; stop at missing hardware or online-service boundaries.
4. Keep the frozen Windows v1 separate until a later interactive product is explicitly accepted.

Reviewed images and their source-run hashes are listed in [the image provenance note](images/2026-11-17/README.md).
