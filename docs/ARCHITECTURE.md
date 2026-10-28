# Architecture — known pieces

**Private lab (overview):** Windows / WSL Ubuntu 24.04 host → QEMU guest → Linux kernel and isolated recovered userspace → Weston/Wayland IVI → original Qt 5.4.1 client → QML test scene / attempted `AppHomeScreen` initialization.

## Observed interfaces

- Qt client uses `ivi_controller` and `ivi_application`; a missing controller caused an earlier null dereference. Enabling an original IVI module in an isolated experimental configuration allowed minimal Qt rendering.
- `AppHomeScreen` attempts `socket(AF_CAN, SOCK_RAW, 1)`; absent guest SocketCAN produced `EAFNOSUPPORT` and later SIGABRT from invalid descriptor handling.
- `AppHomeScreen` later called `ivi_application.surface_create(0, ...)` and committed a buffer, with no verified OEM HMI on screen.
- Original resource paths and selected theme variants still require investigation.
- Some image assets use ASTC; the tested Mesa software path reported `GL_INVALID_ENUM`.

**Scope:** these are observations from a private research environment, not installation instructions or verified behavior of every Hyundai/Kia system. Do not publish or upload proprietary input images.
