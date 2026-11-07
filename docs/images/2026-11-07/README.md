# Screenshot provenance — 7 November 2026

These owner-approved screenshots are a curated visual record of completed, offline QEMU runs. They are lossless WebP conversions of the private PNG captures; decoding the published files reproduces the source RGB pixels exactly. No EXIF or private filesystem paths are embedded. The owner explicitly authorized all relevant, correctly rendered screenshots on 7 November; empty, white/black and unfinished transition frames remain excluded.

| Published file | Private completed run | Source PNG SHA-256 | Published WebP SHA-256 |
| --- | --- | --- | --- |
| `home-menu-spanish-after-nmode.webp` | `20261107T103656Z-replay-c9f2c2-1` | `2c5ba36ba277090c92e7ea2ed2c250fb1470fbd594c7828937c89a93cf88cc19` | `4f2ceac150fd231f7f4e5a7b726b24f5ee7dfee670138fe9ba6ed9ed710a4d08` |
| `radio-fm-spanish.webp` | `20261107T073353Z-replay-4fc508-1` | `336309272966735a6073ee5d48fb4ff71b761c0b362b1f37999597ee94fbd059` | `2a14e312ecc9622948f3b5a4f8f98e15c0a076671c6faa71d7e3876509fca5ad` |
| `nmode-track-dashboard.webp` | `20261107T103656Z-replay-c9f2c2-1` | `d85cdc585290a2c993829517d41253da14c24e4f8f870b2bfc09c443c9285308` | `72b04afa220bcc41c29486ea5446603d4b0a176fc01ed6bf2467dec92a193f89` |
| `nmode-track-page-2.webp` | `20261107T103656Z-replay-c9f2c2-1` | `6d5deae985395ae3972c32bce78c90a8f411a42eeeba7c5d11c1d5b8a554d412` | `2ff73f0c8f71b937be2928eb1d50e7b8645e96937c39589dc11178ad638db064` |
| `voice-memo-spanish-decoded.webp` | `20261107T115821Z-replay-f1b778-1` | `f4226f35a57b044b3f4a05eb18ce0870f6b6b380a711959f32afd86359eea5af` | `2a2f4eaeedb474cc4ba8f1aa72ba0d10dd327c34432e6690d85afcdd377d09c7` |

All images are 1280 × 800. Intermediate animation frames, blank/black/white captures, duplicates and partially rendered states were excluded by review.

## Scope and limitations

- The Home and N Mode images come from the original Hyundai applications running in the private laboratory, with the reversible adaptations documented in the corresponding progress reports.
- N Mode is the original `nm2`/`pf0` Track UI selected for the BC3N MY23 investigation. The existing CarType fixture still reports `0/LX2`, so full physical vehicle identity is not claimed.
- Original requested textures were decoded to PNG for software rendering. This is not native ASTC rendering, and the decoded source files are not distributed.
- Displayed sensor values are unavailable, zero or laboratory state. They are not physical vehicle measurements.
- The Radio image establishes visible original UI presentation only, not RF reception, station tuning or audio output.
- Voice Memo shows original Spanish empty-list content and restored original artwork. Its right assistant pane has no content; recording/playback/audio were not tested. The observer and viewport adaptations are disclosed in the Voice Memo report.
- The guest remained offline; no vehicle, CAN network or Hyundai online service was contacted.

These screenshots contain third-party Hyundai GUI visuals and trademarks. They are provided as owner-approved research evidence and are **not** covered or relicensed by the repository's MIT license. No firmware, executable, QML, texture source, map, trace, core dump or VM disk accompanies them.
