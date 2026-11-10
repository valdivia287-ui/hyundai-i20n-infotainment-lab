# Real i20 N profile and original N Mode transition

**Date:** 10 November 2026<br>
**Scope:** isolated development overlays; not promoted into the frozen Windows product.

## Runtime verified

- The original launcher/manager processes received the complete application profile observed for the owner's i20 N instead of the earlier partial laboratory defaults.
- Home reached the original manager and drawing state `11/11` and displayed the Spanish application grid with the N Mode entry.
- The original N Mode request reached manager and drawing state `500/500`.
- The original return request restored Home state `11/11`.
- The guest remained offline and the disposable overlay shut down cleanly.
- A separate platform control restored the original persistence package used by Standby. Its registration delay fell from about 24 seconds to 1.029 seconds by eliminating 215 failed persistence retries. This result has not yet been combined with the complete integrated journey, so no new end-to-end startup time is claimed.

## Implementation boundary

The private experiment uses independently authored, opt-in adapters around the original launcher. It supplies only configuration fields confirmed by the owner's own exported diagnostic evidence and preserves unknown and dynamic bytes. It does not modify OEM executables or QML, fabricate D-Bus/CAN/UART replies, or claim live vehicle data.

No vehicle identifiers, raw diagnostic logs, firmware, binaries, QML, textures, maps or private run directories are published here.

## Open limits

- Several N Mode graphics are absent on the software renderer because not every original ASTC resource is decoded yet.
- Engine speed, temperatures, pressure, acceleration and other vehicle-dependent values remain zero or unavailable; no synthetic values are presented as real.
- The faster Standby control exposed a compositor ordering race between Confirm and the early Home surface. A state-gated IVI ordering fix is under test.
- The accepted Windows launcher remains frozen; these results belong to the development laboratory.

## Reviewed screenshots

| Stage | Image |
| --- | --- |
| Profile/Confirm | [profile-confirm.png](images/2026-11-10/profile-confirm.png) |
| Home | [home-real-profile.png](images/2026-11-10/home-real-profile.png) |
| N Mode | [nmode-real-profile.png](images/2026-11-10/nmode-real-profile.png) |
| Media Off/background | [media-off-loading.png](images/2026-11-10/media-off-loading.png) |

The screenshots are owner-approved evidence from completed private QEMU runs. They are included for research documentation only; Hyundai interface artwork and trademarks are not covered by this repository's MIT license.
