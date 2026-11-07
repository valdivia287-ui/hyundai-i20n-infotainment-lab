# Original integrated N Mode UI and application audit — 7 November 2026

## Runtime verified

An independent offline software-rendered overlay displayed original Spanish N Mode through the original ApplicationManager and AppLauncher flow. The original observed Home request `(304,500,5185,1,0)` was accepted, the manager reported logical application500, and original N Mode QML loaded inside AppHomeScreen. N Mode is an integrated Home interface in this tested firmware, not a separate AppNMode executable.

The original overview artwork was visible. Real VNC pointer input selected Medidores/Fuerza G and Velocidad, then the original Home control returned to aligned Home. A further Home page drag succeeded. The final Home page matched its initial complete reference except for its page indicator. Five monitored process identities (four OEM processes plus Weston) were retained across nine health samples. The guest powered down cleanly.

Private reference: `20261107T084831Z-replay-92f360-1`. Original evidence is retained privately. No OEM screenshot, trace, resource or executable is distributed here.

## Explicit laboratory adaptations and limits

- The existing synthetic boot fixture leaves the N capability disabled. A separate opt-in frontend adapter configures the original writable Qt property `nModeVariantFlg` locally. It does not alter MICOM/CAN/D-Bus replies or provide sensor values. This is UI capability configuration, not a demonstrated vehicle state.
- Original AppLauncher starts Home with the tested legacy/integrated `nm0` selection. Exact BC3N/nm2 fidelity remains unverified. Static analysis distinguishes `guiVariant` from the N Mode selection; the getter's GUI exclusions must not be misattributed to nm2.
- Twenty-one actually requested original textures were decoded to PNG on CPU. Forty-two immutable source hashes, twenty-one output hashes and PNG/RGBA roundtrips were verified. Originals remain intact. This is decoded original imagery, not native ASTC rendering or recreated artwork.
- Nine additional requested detail textures still lack fallback. Sensor values remain zero/unavailable. `/dev/shm` is absent in this guest, and constructor hardware/shared-memory contracts are not fully captured by the later trace.
- Existing private software, timing, IPC and root-HMI laboratory adaptations remain in use. No N Mode QML was edited. Stable earlier profiles are preserved separately.
- The matrix therefore records N Mode as **partial, with a verified UI round trip**. No full vehicle function, new ten-minute stability result, audio, navigation or accelerated guest renderer is claimed.

## Audit breadth and negative evidence

A static parser identifies35 deduplicated original AppLauncher entries. Nineteen declared executable paths exist in the inspected immutable base; sixteen do not. Missing paths are not proof that an integrated or archived alternative is absent. Logical Home interfaces, submenus and excluded utilities are separate metadata rows, not additional usable applications.

Previous verified GUI IDs are original Standby10, Home11 and European Radio77. This round adds an original N Mode500 UI cycle with the limits above. Home Settings submenu is not a verified AppSetup60 launch.

A native Home Medios click emitted `(304,2,27,1,0)`, not a direct MediaGate23 or AppMediaPlayer100 request, and did not open another interface. A native Teléfono click emitted `(304,121,40,1,0)`; the original manager returned255, no BluetoothHMI process/surface was observed, and Home remained usable. The precise refusal condition remains under investigation;255 alone is not a generic failure code. Projection and qualified original on-demand startup are subsequent independent experiments, not results of these runs.

## Reproduce supporting checks

With a separately supplied completed private reference run:

```sh
python3 tools/verify_nmode_evidence.py /private/path/to/completed-run
```

Python3 and Pillow are required. The verifier checks original-manager evidence, hashes, input action records, process identities, Home pixels and clean shutdown. Screen identity still requires visual review; metadata alone cannot establish a rendered usable application. Its diagnostic output remains private.

For static metadata extraction from the owner's independently obtained firmware:

```sh
python3 tools/inventory_oem_apps.py /private/AppLauncher /private/base.img /private/new-inventory
```

This reads ELF metadata and a read-only debugfs directory listing; it never executes an OEM binary. It does not establish runtime eligibility or safe behavior. Review every candidate before a bounded isolated test. Exclude update, flashing and vehicle diagnostic paths. Never attach physical vehicle/CAN interfaces, enable unrestricted Internet, bypass licensing, or populate fictitious phones/stations/accounts.

## Next work

Individually test reviewed graphical candidates in fresh offline overlays, recording the real native request, actual process/surface owner, original content, safe interaction and native Home return. Analyze missing real dependencies before designing any adapter. Preserve the functional Home/Radio profile. Improve the exact N Mode variant and remaining original texture fallback separately from this verified legacy UI reference.
