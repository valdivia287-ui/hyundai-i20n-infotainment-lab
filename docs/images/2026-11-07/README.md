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

## Native BC3N25MY N Mode screenshots

Owner authorization on 7 November 2026 permits relevant correctly rendered images. These full-frame lossless WebPs are from the separate native81/HighPerformance1 profile with 87 original CPU-decoded textures, without N Mode capability/argv adapters. Both were visually reviewed; no blank or transitional image is included. Not native ASTC rendering or a telemetry demonstration.

- [bc3n25my-nmode-spanish-track-decoded.webp](bc3n25my-nmode-spanish-track-decoded.webp): Original Track page after native Home icon. Original PNG `operator-bc3n25-nativecap-icon-reopen.png`, SHA256 `fc8ff622a4aa0699936a3cdd4f3bbd8a976de1427a0efe5d55d6d46ef24a98b7`. WebP SHA256 `4850185a1ad08d0525062d73bcf43f702e90f5297862a4a6d2d0da89f9519096`, 221092 bytes, 1280×800, RGB-identical after decoding.
- [bc3n25my-nmode-spanish-page2-decoded.webp](bc3n25my-nmode-spanish-page2-decoded.webp): Original page 2 after a VNC swipe. Original PNG `operator-bc3n25-nativecap-nmode-page-two.png`, SHA256 `d6a7ad8b772903e24b2623b732ec358c3eeec7c63b7aa4ba782da25cc99cc95e`. WebP SHA256 `0c64997a215800bef65b22bbfebbf8450897b02834741eb34c41fc690ee9b465`, 224328 bytes, 1280×800, RGB-identical after decoding.

## Sesión Windows integrada

Tres capturas revisadas de una misma sesión, autorizadas por el propietario. PNG→WebP sin pérdidas, RGB idéntico, sin recortes ni edición de contenido. Las superficies negras/incorrectas y los menús con iconos ausentes no se publican. Los recursos visibles son originales decodificados en CPU, no ASTC nativo ni aceleración RTX.

- `windows-integrated-nmode.webp`: N Mode original visible en la sesión Windows integrada; ceros/OFF OEM, sin telemetría. SHA256 `10c2c9d3202fec47bbdd516e671e080db109ba020d5208e1832080d70ffe5f66`.
- `windows-integrated-manual.webp`: Vista Manual original en español; el QR no se abrió y no se afirma contenido offline del manual. SHA256 `7a6bc76fe814b4f0e7ccf1c1c81a5d29bf40c7de09960d9555c9e478bb6ee7e4`.
- `windows-integrated-radio.webp`: Radio FM original española0.0; sin hardware. Esta imagen prueba contenido visible, no el retorno posterior que quedó negro. SHA256 `f807751d1f3bcac03bb932b9a6125e4c1c75d16dcdc535fe2eb97ab1819fcb38`.

[Alcance y límites](../../PROGRESS-2026-11-07-WINDOWS-PRODUCT.md).
