# Wireless projection activation path — 18 November 2026

## Scope

This checkpoint documents a bounded, offline VM experiment against the private
BC3N development environment. It does **not** claim a working wireless Android
Auto or Apple CarPlay session, vehicle installation, phone pairing, Bluetooth
transport or Wi-Fi projection.

No OEM firmware, executables, QML, resources, keys, raw vehicle traces, VM disks
or installable packages are published with this report.

## Vehicle-derived observation

Sanitised observations from owner-supplied logs showed the production launch
profile using wireless-projection parameter `0` in AppProjection, while the
wired Android Auto path completed its normal accessory and pairing sequence.
The same private evidence showed the physical unit reading its MFi certificate.

These observations establish useful configuration and hardware context; they do
not prove that changing one launch parameter is sufficient to enable wireless
projection.

## VM experiment

A reversible, process-scoped development adapter supplied `-wpp:1` only to the
three original processes involved in the observed activation path:

- AppHomeScreen
- BluetoothHMI
- AppProjection

The exact-adapter run established all of the following:

- Home received the wireless-projection argument;
- BluetoothHMI parsed it as `m_nWPP : 1`;
- AppProjection started with the same argument;
- no original application executable was modified for the VM experiment.

This is runtime evidence that the launch parameter reaches the intended original
software. It is not evidence that a projection session completed.

## Remaining boundary

The isolated VM has no phone, Bluetooth/Wi-Fi radio or physical MFi device.
AppProjection exhausted its certificate-device retries and stopped with its
native timeout path; BluetoothHMI also encountered the laboratory's unresolved
EGL-configuration boundary. A separate diagnostic configuration kept
AppProjection alive after activation, but still could not supply the missing
physical projection hardware.

The result is therefore classified as:

- **runtime-proven:** propagation and parsing of `WPP=1`;
- **not proven:** wireless discovery, pairing, transport, projection UI or media;
- **not performed:** vehicle installation or head-unit update.

## Next safe step

Keep the activation result separate from transport validation. Further VM work
should emulate only the minimum missing device boundaries needed to observe the
next native state transition, without inventing successful Hyundai services or
claiming phone connectivity that the laboratory cannot provide.

