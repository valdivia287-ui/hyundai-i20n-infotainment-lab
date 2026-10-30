# 30 October 2026 — ApplicationManager, IVI WM, Pixman and GL integration

> **Source:** a private read-only tracking bundle, `HYUNDAI-I20N-SEGUIMIENTO.zip`, prepared from completed lab runs on 30 October 2026 and supplied by the project owner. This is a **sanitized written summary**, not a publication of that ZIP, its private traces, screenshots, guest configuration, OEM assets or scripts. The evidence has been reviewed as exported excerpts, not independently reproduced on the owner’s host.
>
> **Status:** the **original Home remains interactively navigable in the earlier reference profile**. Attempts to integrate original ApplicationManager and the OEM IVI window manager in the same guest **remain unstable**. No second OEM app has launched successfully.

> **This report is historical for the earlier GL/WM failure stage.** Later completed trials confirmed **ten-minute simultaneous original Home + ApplicationManager operation** with a **separate manager SysV IPC namespace**, and further original AppSetup application-launch investigations. The newer status is in the [30 October IPC/application report](PROGRESS-2026-10-30-IPC-APPS.md). The earlier failures below remain valuable diagnostic evidence, not the current best result.

## Last known working baseline

- **Run `20261030T020654Z-13522-1`:** original Hyundai AppHomeScreen navigated from page 0 to page 1 after a pointer drag. Original QML emitted `advancedModePageChange(1)`. A private experimental overlay selected **BC3 = 23**; it does not prove the vehicle's factory-persisted configuration.
- **Run `20261030T021201Z-19064-1`:** the original Home processed a press on N Mode and requested `appid=500`. This did **not** launch N Mode.
- Keep this rendering/input profile as a **regression baseline**; the later integrations should be isolated in new, disposable overlays.

## From missing appmanager to real OEM manager activity

- OEM ApplicationManager was subsequently started in QEMU. The session bus briefly registered `com.lge.hyundai.avn.appmanager`.
- Without the expected OEM IVI window-manager services, an earlier run observed **SIGSEGV / SEGV_MAPERR (null access)** after Wayland global enumeration. The manager binary references `ivi_info_requester` and `ivi_window_manager`; exact crash instruction and its causal dependency are not established.
- Introducing the original `ivi-window-manager.so` allowed the manager to run longer. The later trace recorded real requests to the window-manager interface to identify **VolumeOSD, AvOSD and NotificationManager**. These are requests, **not proof that those applications are open or functional**.
- Suppressing `/usr/bin/early-background` in an isolated guest **did not prevent** the subsequent Pixman assertion, so early-background was not necessary for that failure to reproduce.

## Renderer comparison: observed outcomes

| Completed private run | Graphics/IVI test | Result reported in filtered logs |
| --- | --- | --- |
| `20261030T141120Z-2089-1` | Pixman, OEM WM, Home and delayed ApplicationManager | Home attached an SHM **ARGB8888** buffer, **1926 × 753**, Wayland format **0**; compositor then aborted in `composite_clipped: Assertion src_format failed`. The responsible Pixman image/surface remains **unidentified**. |
| `20261030T141450Z-9916-1` | First GL attempt | Guest script failed **before Weston ran** (Bash 3.2 with `set -u` and an empty array). This test gives no evidence about rendering. |
| `20261030T141623Z-11549-1` | Weston GL, Mesa **softpipe 13.0.6**, OEM WM, **without `hmi-controller`** | EGL/GL initialized and the Pixman assertion was avoided; Home was **black/invisible**, then aborted by its watchdog (**exit 134**). ApplicationManager showed activity, but no app launch was proven. |
| `20261030T151207Z-3791-1` | GL/softpipe, OEM WM **with `hmi-controller`**, manager delayed 60 s, early-background suppressed | Original Home appeared **small in the upper-left (~320 × 365 on a 1280 × 800 output)**, not fullscreen or navigable. Manager made WM requests; Home aborted by watchdog (**134**). |
| `20261030T151528Z-18058-1` | Repeat of previous profile **without `strace` attached to Home** (`CA_HOME_NO_STRACE=1`) | The small Home view and watchdog failure **reproduced**. Removing ptrace is therefore **not sufficient** to fix the hang. No proven Home→app→Home interaction. |

### Distinguish observation from hypotheses

**Observed**

- Pixman composition assertion under the first OEM-WM profile.
- A 1926 × 753 SHM buffer attached shortly before the assertion.
- Weston GL/softpipe starts and can outlive this Pixman composition point, but integration still fails.
- With the OEM WM and `hmi-controller`, Home has a **scale/placement regression** and a **watchdog failure** (no notification from main thread for over ten seconds).
- The newest Home logs record unsupported **ASTC** compressed texture calls (for example a Quiet Mode icon) and `GL_INVALID_ENUM`; temporal proximity **does not prove** they caused the watchdog.
- The latest guest and supervisor were stopped after the tests; the recorded reference interactive profile was retained.

**Not established**

- The Pixman image that actually has `src_format=0`. A solid-color IVI image is a **hypothesis**, not a verified diagnosis. Do not equate Wayland `wl_shm` format code `0` (ARGB8888) with the invalid Pixman format return value `0` without instrumentation: they are different APIs.
- Whether the OEM WM's **1920 × 720** target geometry versus the **1280 × 800** virtual DRM output explains the **~320 × 365** Home scale.
- The root cause of the Home watchdog. Its privately preserved core could reveal the main-thread stack; no publicly reviewed backtrace yet.
- Stable joint Home/ApplicationManager operation, launching N Mode or any second OEM app, return navigation, ten-minute stability, or a verified Windows double-click launcher.

## Latest code change reported

A diagnostic flag **`CA_HOME_NO_STRACE=1`** causes the guest launcher to execute original Home **without tracing through `strace`**, solely in a disposable guest. The default remains the previous traced path. Reported checks: Bash syntax, Python compilation and seven offline tests. The no-`strace` run still aborted by watchdog, so this is a **negative diagnostic result**, not a fix. The project owners should review current local changes before further tests.

## Suggested next experiments (not completed)

1. Preserve the page-0→1 reference, and inspect newer local runs first: this document describes only the exported **completed** sessions.
2. In a separate, instrumented **laboratory Weston build**, inspect the Pixman image's actual format and associated surface/client when `composite_clipped` asserts. Do not patch OEM binaries, publish original code without license review, or treat `early-background` as the only suspect.
3. Independently compare OEM IVI WM's source/destination geometry with `drm-backend` output and `hmi-controller` transformations. Recheck scale and location with one configuration change per run.
4. Diagnose the **Home watchdog/main-thread stall** with a local stack/backtrace from the preserved core and service/Wayland traces. Check ASTC issues independently; do not conflate timing with causality.
5. Once Home and ApplicationManager coexist stably, route an actual original Home application request, observe the target process and surface, demonstrate interaction, return to Home, verify at least ten minutes of operation, then test the Windows launcher.

## Publication / provenance

The original tracking ZIP, filtered traces, screenshots, source scripts and configuration INIs were **not committed**. They remain in the owner's private lab. This public report intentionally excludes original OEM binaries, firmware, derived textures, full logs, private host paths and identifiers, VM images, cores and credentials. Earlier specifically approved Home screenshots remain in the repository's separate README gallery.
