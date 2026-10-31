# 31 October 2026 — OEM second-application experiments: Standby/Clock and EngineerMode

> **Source and cutoff:** Sanitized report from the project owner's private ESTADO-PROYECTO.md, latest note **31 October 2026, 11:34 UTC**. All original binaries, firmware, proprietary QML, screenshots, raw traces and guest overlays remain private. Findings here summarize owner-supplied Codex reports, **not independently replayed QEMU runs**.
>
> **Current assessment:** Original AppStandbyClock and AppEngineerMode have **rendered limited original Hyundai UI** inside disposable QEMU/Weston laboratory guests. Neither is yet a stable, interactive secondary application. A functioning Home → secondary app → Home journey is **not** demonstrated.

## Better preserved baselines (30–31 October)

| Completed run | What the reported evidence demonstrates |
| --- | --- |
| 20261030T020654Z-13522-1 | Original Hyundai Home navigated page 0 → 1; original QML recorded advancedModePageChange(1). |
| 20261030T201814Z-17465-1 | Home + original ApplicationManager alive at guest uptime ~619s. Home navigated 0 → 1 → 0, delivered real N Mode request (304,500,5185,1,0) to manager, which returned 255. No N Mode opening. |
| 20261030T211509Z-11579-1 | The earlier **320×365** display geometry was traced to Weston 1.10 HMI-controller initial TILING mode. A separately compiled, reversible public-source HMI-controller selecting initial **FULL_SCREEN** achieved full 1280×730 Home **without the previous manual destination-region override**; original Home drag navigation worked. |
| 20261030T212548Z-18144-1 | Weston, original Home, ApplicationManager and AppStandbyClock coexisted at **guest uptime 619.73s**, with correct fullscreen geometry and Home in threaded Qt scene-graph mode. Standby was still white, so this is **not** proof of usable application switching. |
| 20261031T102501Z-6447-1 | Four components alive at **guest uptime 619.96s**; Home heartbeat through sequence 112, direct original Clock method responded int32 1. AppStandbyClock intermittently showed **“Confirm / Language”**, “--:--” and black. Home exited 143 on deliberate shutdown; no verified interactive clock. |

The original ApplicationManager still uses a **separate SysV IPC namespace** to avoid the previously traced MICOMSTATUSMESSAGE semaphore contention. This is a lab workaround, **not original shared IPC restored**. Using QSG_RENDER_LOOP=threaded for Home avoided a prior overlap-triggered watchdog in bounded testing, but does not fix all application behavior.

## AppStandbyClock: original pixels and D-Bus transitions

- Original AppStandbyClock creates IVI surface 1001 and has attached a genuine Wayland buffer in completed tests (a previous attach measured 1926×753). The auxiliary Weston viewer's conflicting surface IDs were remapped in disposable overlays.
- Original ApplicationManager accepted transitions for app IDs **10** (Standby) and **29** (Valet), received original callback ret[1], then sent foreground requests to the OEM IVI WM. Early views remained plain white, so those tests proved the transition *route*, not usable screens.
- A touch-key request to app ID **14** was redirected to Standby app ID **10** in run 20261031T100218Z-32004-1. Home later watchdog-aborted in that run (134); **not a stable baseline**.
- A **direct original method call** to /com/lge/hkmc/avn/appfunc/clock, method show_window_fg, **app ID 14, reason 10, plane 1, avmode -1, command 0, temporal=false**, returned **int32 1** in run 20261031T101313Z-16747-1. The visible output intermittently included **“Confirm”**, **“Language”**, **“--:--”** or black. Method success is **not proof that a clock was functional**.
- The black intervals also occurred **without user input**. Converting 16 OEM ASTC button resources to PNG in a *private, reversible test overlay* produced only minor visual differences, **not a solution**. Those converted resources were not uploaded.
- Pointer events reached the original Standby Wayland surface, but the QML event/interaction initially was not demonstrated.

### 31 October state-probe breakthrough: why Confirm cannot be clicked

A diagnostic copy of original QML in run **20261031T104715Z-5497-1** reported **enableBtn=0** and **enableTouch=false** while the “Confirm / Language” form was visibly loaded. The OEM button's MouseArea disables pointer action when enableBtn is false. Even the high-z probe disappeared during a black interval, so **black was not explained by an empty QML Loader alone**.

| Controlled test | Observed outcome |
| --- | --- |
| 20261031T105606Z-14495-1, reason 10 and temporal=true | Original method returned int32 1, but loaded form remained **enableBtn=0, enableTouch=false**. The temporal boolean alone does not enable Confirm. |
| 20261031T110336Z-22256-1 | Original **UserProfileManager (UPM)** created KEYSUPPORTCHINESE shared memory, registered D-Bus and emitted notifyUpmIdWhenBotting. Its 180s lifetime ended **before** the Clock request at guest uptime 320s; no conclusion possible about UPM's effect while alive. |
| 20261031T111043Z-10907-1, UPM lifetime extended to 450s | Original Standby created IVI 1001 but **no buffer until guest uptime 620.49s**; the test skipped the conditional Clock request. Correlation with longer UPM run does **not establish causation**. |
| **20261031T112444Z-17824-1**, reason 11, temporal=true | QML probe showed **enableBtn=1** at 20s and 60s, supporting original **eUSER_INPUT_STANDBY_AGREE_ENABLE** branch identified by static examination. **But item1=false, item2=false, isDrawed=false** at those times: the form was **not loaded at the same time**. No usable Confirm click yet. |

**Pending at the report cutoff:** A fresh isolated-overlay trial **reason 10 first** to show the form, then **reason 11 + temporal=true** to enable Confirm, measuring loader state, real QML click, visual transition, Home heartbeat and stability. This is a reasonable hypothesis, **not yet a reported success**.

## AppEngineerMode: original fullscreen title; main-thread wait

- Starting original **UserProfileManager** created the **KEYSUPPORTCHINESE** shared-memory dependency EngineerMode required. This removed an earlier null-access failure.
- In **20261031T091312Z-3435-1**, OEM AppEngineerMode created **two IVI surfaces**, registered with original ApplicationManager as app ID **301**, and showed **“Engineering Mode”** fullscreen. Later trials acquired D-Bus name **com.lge.hkmc.avn.appfunc.AppEngineerMode**. This is **genuine but very limited rendering**, not a usable engineering menu.
- ApplicationManager's **AppAlive** checks timed out (NoReply) and it deliberately called **AppKill()**; EngineerMode exited by SIGTRAP (133). Setting its scene-graph render loop to threaded did not fix this (20261031T092029Z-2538-1).
- Without manager, EngineerMode remained visible longer but Peer.Ping/Introspect sometimes timed out. Later trace associated **fd 9 with Wayland** and **fd 17 with session D-Bus**; the main thread repeatedly remained in indefinite poll on Wayland fd 9 after its drawing callback. One Ping succeeded under strace, but Introspect still timed out. **Exact wait stack and reason for missing return to Qt remain unproven**; manager termination is a distinct policy action.
- A pointer-movement-only test did not deliver wl_pointer.enter, but the lab IVI controller assigns focus on a **button press**; an isolated click test was the next justified check.
- The original OEM **AppLauncher** executable exists but was **not executed**: its multi-application startup table could create duplicates alongside manually started OEM processes.

## Minimal virtual vehicle services — proposed, not implemented

Observed progress supports a **real OEM service first** approach: inspect existing original processes, D-Bus signatures and service owners, SysV/shared-memory contracts and IVI callback dependencies before implementing any synthetic substitutes. EngineerMode progressed using the **original UserProfileManager**, so not every missing dependency needs a new simulator. Only emulate a service where an actual external dependency is demonstrated and its contract is understood. No generic “always OK” D-Bus replies, physical CAN, vehicle flashing or device access.

## Next steps

1. Check **newer private runs after 11:34 UTC** for the completed outcome of the pending two-reason Clock test.
2. Preserve the interactive Home baseline, ten-minute Home+manager stability, fullscreen-controller version and 4-process ten-minute baseline in **distinct disposable overlays**.
3. For Clock, demonstrate **a loaded Confirm form with enableBtn=1**, real MouseArea action, stable pixels, and ideally a return-to-Home transition.
4. For EngineerMode, identify precise Wayland/Qt main-thread stall and D-Bus health-check behavior; distinguish blocked app from ApplicationManager kill policy.
5. Reach **one second original application fully visible and interactive**, then Home → app → Home, stability and Windows one-click launch.
6. Keep parallel coding agents in **separate worktrees** and avoid competing for one VM or shared overlays.

**Publication policy:** This file is a non-proprietary narrative only. No original firmware, OEM binaries, QML code, ASTC-to-PNG derivatives, unapproved screenshots, raw/private traces, VM images, device details or secrets are distributed.
