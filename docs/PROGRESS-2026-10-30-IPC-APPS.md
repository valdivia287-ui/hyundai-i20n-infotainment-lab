# 30 October 2026 — 10-minute OEM Home + ApplicationManager coexistence and second-app investigation

> **Source qualification:** This report summarizes the owner's latest private Codex status file, `ESTADO-PROYECTO.md`, last updated **19:22 UTC** on 30 October 2026, plus earlier technical notes. The run traces and screenshots referred to below remain on the owner's machine; they have **not** been independently replayed or uploaded. Results are accurately distinguished from hypotheses and outstanding tests.
>
> **Major milestone:** Original Hyundai `AppHomeScreen` and original `ApplicationManager` ran concurrently in an isolated QEMU/Weston GL laboratory for **10 minutes** in the completed run `20261030T175729Z-3869-1`. This uses an **experimental separate SysV IPC namespace for ApplicationManager**, not fully reproduced OEM interprocess communication. **No secondary OEM application has rendered and become interactive yet.**

## Baseline preserved

- The earlier original Home navigation reference, **`20261030T020654Z-13522-1`**, still retains its recorded SHA-256 and page 0→1 event (`advancedModePageChange(1)`).
- Experiments use disposable overlays; do not modify the original firmware or silently replace the working Home profile.

## Confirmed ten-minute co-existence

**Run:** `20261030T175729Z-3869-1`

- Reported `stability-300.txt` and `stability-600.txt` record the original Weston GL/OEM IVI window manager, OEM Home and OEM ApplicationManager simultaneously running at **5 and 10 minutes**.
- `home-stability-5m.png` and `home-stability-10m.png` reportedly show Home at **1280 × 730**, after a laboratory surface destination-region adjustment (surface **1000** to `0,0,1280,730`).
- No watchdog crash or Pixman assertion occurred during this completed run; VM stopped cleanly.
- **Crucial limitation:** ApplicationManager was launched in a separate SysV IPC namespace with `unshare(CLONE_NEWIPC)=0`, while retaining real Wayland and D-Bus connections. This sidesteps an OEM shared-semaphore contention, **not** a full MICOM/shared-memory implementation. This result proves concurrent processes and visible Home for 10 minutes, **not** end-to-end application navigation or complete service integration.

### Watchdog diagnosis

Codex traced Home's previous main-thread stall to a Qt SysV semaphore named **`MICOMSTATUSMESSAGE`**. In the reported integrated environment, ApplicationManager acquired the semaphore and did not release it in the absence of required shared-memory state. When the manager alone was stopped, Home resumed without a watchdog failure in `20261030T173224Z-22314-1`. A one-key remapping experiment failed because Qt recreated the key file. Starting an OEM MICOM service in an isolated guest exited with code 1 and did not register D-Bus (`20261030T173828Z-13986-1`). Earlier core data were truncated; the conclusion rests on process sampling and SysV traces, not on a complete core backtrace.

## Genuine Home → ApplicationManager request, but not launch

- **Runs `20261030T174954Z-18971-1` and `20261030T182026Z-30876-1`:** original Home navigated to page 1; an N Mode icon click generated `appid=500`; the request **reached original ApplicationManager**. The manager returned **255**, and no target application opened.
- A diagnostic replay of six original Home registrations, all returning zero, **did not change** the 255 result.
- Replaying `registertouchkey` from a different D-Bus sender also failed because the manager listens for signals from Home's specific service name. This does **not** demonstrate a supported workaround.

### ApplicationManager can terminate Home during startup

- **`20261030T181308Z-7816-1`:** with the manager started early, it attempted `org.freedesktop.DBus.Peer.Ping`. After `NoReply` responses, it executed `killall -5 AppHomeScreen`, confirmed as `SIGTRAP` rather than an unexplained Home crash.
- **`20261030T181701Z-26476-1`:** preventing that specific diagnostic signal made the manager escalate to `killall -9`. The signal-blocking guard was therefore rejected; the underlying service behavior remains unresolved.

## A second original application: AppSetup

| Run | Observed result |
| --- | --- |
| `20261030T184356Z-18232-1` | Original AppSetup connected to Wayland, but the compositor rejected IVI `surface_create(1001)` because an auxiliary reference UI already claimed the ID; Setup ended with SIGSEGV. |
| `20261030T185014Z-22041-1` | Removing the reference UI freed the ID, but Home hit a watchdog stall, so the profile was not retained. |
| `20261030T185434Z-31042-1` | Remapping only the reference UI's IVI IDs **1001–1007 → 9001–9007** in a disposable overlay allowed original AppSetup to create **surface 1001**, register interfaces with ApplicationManager and leave Home visible/stable through 170 s. **AppSetup did not attach a buffer**, and the manager later sent SIGTRAP after failed `Peer.Ping`. |
| `20261030T190041Z-25586-1` | Starting AppSetup without ApplicationManager left Home visible; original Setup created surface 1001 **but still attached no buffer**. |
| `20261030T190658Z-30975-1` | A bounded Setup trace showed repeated D-Bus queries/100 ms pauses and `ServiceUnknown` replies for missing OEM services during its first 90 seconds. This does not isolate a single missing service as the cause. |
| `20261030T191232Z-30312-1` | In a 360 s Setup trial, the main thread was later in `pselect`; screenshots at 240/330/420/480 s showed only Home. Setup timed out with code **124** without rendering; Home stayed stable. |

The auxiliary viewer remapping fixes a **surface-ID collision**, but does **not** make AppSetup render. The absence of ApplicationManager also does not, by itself, solve Setup initialization.

## Pending at report cutoff — do not claim outcome

At **19:22 UTC** the owner-supplied status reported an ongoing run `20261030T192157Z-999-1`, attempting **original AppStandbyClock** at 120 s with a 180 s budget, without ApplicationManager and with the same isolated IVI-ID remapping. The hypothesis was that a smaller original app may reach buffer attach/render sooner. **Its outcome was not yet present** in the supplied document; check the newest local run before drawing conclusions.

## Practical priorities for the next agent

1. Check newest finished `runs/` first, including the **AppStandbyClock trial** (if completed); never infer its result from the report cutoff.
2. Preserve both the **original interactive Home reference** and the **new 10-minute concurrent Home/manager baseline** as distinct profiles.
3. Trace manager return **255** and its peer-ping/signal behavior against actual original registration and service dependencies. Do not block OEM signals merely to make a test pass; don't fabricate D-Bus replies.
4. For original AppSetup/StandbyClock, observe actual Wayland buffer attach/commit and real pixels, not surface creation alone. Instrument non-destructively and use one variable per new isolated overlay.
5. Generalize to repeatable **Home → secondary original app → Home** interactions, then verify input and stability and build the Windows one-click launcher. A launcher alone does not constitute a working emulator.

## Publication policy

No OEM firmware, executables, QML, textures, VM disks, core dumps, logs with private data, or novel screenshots from this update were uploaded. Historical owner-approved screenshots remain in the existing README gallery. The proprietary application names and diagnostic results above are used descriptively in this independent, offline research report.
