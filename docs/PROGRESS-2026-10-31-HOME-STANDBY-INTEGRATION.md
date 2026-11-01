# 31 October 2026 — OEM Home ↔ Standby: input, hidden frame callbacks and return-state blocker

> **Source cutoff: 31 October 2026, 16:43 UTC.** This sanitized progress report summarizes two private, owner-supplied Codex files: an updated ESTADO-PROYECTO.md and INFORME-SEGUIMIENTO-20261031.md, plus the final supervisor state.json. The underlying QEMU guest, raw logs and screenshots have **not** been independently reproduced from this public repository. No original Hyundai firmware, QML, converted textures, private screenshots or raw traces are published.
>
> **Bottom line:** Original Home navigates 0→1→0 **while original ApplicationManager is active**. Original Standby displays its Confirm/Language screen, and the **real OEM Confirm button has emitted pressed, released and btnClicked**, with a genuine request delivered to the manager. A revised lab profile keeps hidden Home alive during the foreground transition without SIGTRAP/watchdog in a bounded run. **The manager still rejects return-to-Home requests because its internal Standby state remains 10. No complete Home→Standby→Home journey yet.**

> **Further progress on 1 November:** Original MICOM can now start on a second QEMU UART and accept a single synthetic boot-information hardware reply, yielding a genuine MICOM→ApplicationManager D-Bus response and `power_status=16`. **At the latest provided 01:58 UTC snapshot, no completed run has yet demonstrated standby_status 10→11 or a real return to Home**. See [the 1 November MICOM/power report](PROGRESS-2026-11-01-MICOM-POWER-STATE.md). Earlier status below remains a valid historical record.

## Core completed results

| Private run ID | Reported observed outcome |
| --- | --- |
| **20261031T132500Z-6658-1** | Original Standby Confirm displayed and enabled; a repeated genuine click generated **P=1, R=1, C=1** for pressed/released/btnClicked and caused OEM request **appid=2, reason=12**. ApplicationManager rejected it because it did not consider Standby the drawing application in that profile. This proves *button interaction*, not navigation. |
| **20261031T141450Z-28429-1** | Complete Home core: main thread waiting in Qt Quick QWaitCondition, and its previous Wayland frame lacked callback.done after the foreground transition. Home aborted by watchdog **134**; this is an earlier failing profile. |
| **20261031T145237Z-20724-1** | Experimental Weston HMI probe found Home surface **1000** moved from active foreground layer **102** into hidden layer **4000** when Standby surface **1001** became foreground. Its layer/surface reported visible but Home's view was **not listed for repaint**; Home's frame callback stayed pending. This explains why a simple visible=true check was insufficient. |
| **20261031T150154Z-12177-1** | A **separately built, reversible lab HMI-controller variant** delivered two pending Wayland frame callbacks to hidden Home, allowing heartbeat to continue through the planned stop (**exit 124**, no watchdog). Standby showed Confirm/Language at +12s but black at +65s. This is a bounded workaround, not an OEM compositor repair. |
| **20261031T153103Z-31661-1** | Two real original Clock show_window_fg calls (**reason 10/temporal=false**, then **reason 11/temporal=true**) returned success. Later, with Standby in foreground, private QML probe showed **item2=true, drawn=true, enableBtn=1** and Confirm/Language. A click generated the original **appid=2, reason=12** request, but manager rejected it: **currentStandbyStatus[10] / StandbyStatus is not enabled[10]**. |
| **20261031T154108Z-4155-1** | Asking original ApplicationManager for **appid 10, reason 11** did **not** enable its Standby state. It normalized the request to reason 10; Confirm remained disabled. Do **not** repeat as if a fix. |
| **20261031T155406Z-12394-1** | Direct **Transition::request(322,11,0,1,0)** reached UserInputHandler::handleEvent, returned **255**, did not dispatch handleGoHomeKey, and did not bring Home forward. Home registration was missing in this run; not a successful return. |
| **20261031T161129Z-13234-1** | With six original Home registrations replayed, a complete core and manager trace confirmed a **deliberate manager-initiated SIGTRAP**. The manager performed six unsuccessful **APP_HOME AppAlive** checks, then **AppKill(AppHomeScreen)** while Home waited in Qt Quick; the frame callback arrived only ~4s after the kill. |
| **20261031T162201Z-9612-1** | With only **Home** switched to Mesa **llvmpipe** (Weston/Standby stayed on softpipe), Home remained alive through the Standby foreground transition. Manager AppAlive failures were intermittent (0,1 then 0,1), **no AppKill**, Home heartbeats until sequence 78; planned timeout **124**, no SIGTRAP **133** or watchdog **134**. Return key 322 still returned **255**. |
| **20261031T163512Z-9562-1** | **Latest completed reproduction:** original Home, registered in the original manager, navigated **page 0→1 and 1→0** through two QMP drags; QML emitted advancedModePageChange(1) and (0). Then original Standby became foreground and its real Clock methods replied; private capture showed **Confirm/Language, btn=1, item2=true, drawn=true**. Home continued heartbeats; exited by **planned timeout 124**, without manager kill or watchdog. **GoHome event 322 returned 255**, and manager rejected **appid=2, reason=12** while its internal Standby status stayed **10**. QEMU shut down via ACPI; the report says no QEMU/supervisor remained active at completion. |

## Cause and limits of the hidden-Home watchdog

The reported failure sequence is now well constrained:

1. Original ApplicationManager and IVI WM bring Standby surface **1001** to the front.
2. Original Home surface **1000** moves to layer **4000** and is excluded from the compositor's active repaint list although its own visible flags may still be true.
3. Home's Qt Quick render synchronization can request a Wayland frame and wait for a callback that the compositor does not deliver while its view is excluded.
4. Home stalls, the watchdog may abort it (**134**) or the original ApplicationManager may independently decide it is unresponsive after AppAlive timeouts and run **AppKill**, producing SIGTRAP **133**.
5. A **lab-only HMI frame-callback rescue** keeps hidden Home progressing in tested runs, and Mesa **llvmpipe for Home only** helped the registered app meet enough health checks to avoid manager termination in two bounded configurations.

Important distinction: forcing callbacks is an **experimental workaround** and may not reproduce the original OEM frame scheduling. The exact visual/black-screen issue in Standby is still unresolved. Earlier llvmpipe tests **on Standby**, not Home, reduced Standby's render-thread CPU usage but did **not** prevent Home's watchdog; do not conflate the two tests.

## Genuine OEM Confirm click, but manager state mismatch

- The real Clock D-Bus method uses **reason 10, temporal=false** to display the form, then **reason 11, temporal=true** to enable the Confirm branch. In the newer runs this produced **loaded + enabled** Confirm together, superseding the older 11:34 UTC result in which reason 11 enabled an unloaded form.
- The original QML root had a focus MouseArea at **z=1000**. In an isolated diagnostic QML copy, moving it to **z=-1** *after* enableBtn became true allowed original Confirm button signals to pass. A repeated click produced **P=R=C=1**: genuine press, release and btnClicked. This modification is a **private experimental input fix**, not a final OEM configuration.
- Original Standby emitted a transition request **appid=2, reason=12** following a click. In a profile where manager did not recognize Standby as foreground, it rejected the request with a drawing-app mismatch.
- In later profiles manager recognized **CurrApplication[10] / DrawApplication[10]**, and still rejected the request because **currentStandbyStatus[10]** was not enabled. These are different failure conditions; do not conflate them.
- The tested **Transition::request(322,11,0,1,0)** returned **255** and reached only handleEvent, **not** handleGoHomeKey. Do not present repeating event 322 as an answer.
- Reverse-engineering of the original manager's embedded interface metadata identified **com.lge.avn.appmanager.info.ask_standby_status** (read method) and **standby_status** (outgoing signal). The integer's actual **OEM writer/state transition** is not yet identified. The **set_request_standby_screen** method has no status-value argument and must **not** be assumed to be an integer setter. **NotifyConfirmStatus(false)** was seen, but it apparently updates a different boolean field; the manager's integer state remained 10.

**Key outstanding question:** Which original process/event moves manager's Standby state into the condition accepting the reason-12 transition to the requested destination, and what authentic input path returns to Home?

## Latest supervisor metadata does not override the logs

For **20261031T163512Z-9562-1**, the final supervisor JSON reported phase **home_expired**, message **600-second limit reached**, ready=false, home_validated=false, home_rendered=false, changed_pixels=722511. This status reflects its **final validation condition at timeout** and is **not proof that original Home never rendered**: the same run has original page-change QML messages and an earlier Home screenshot. Conversely, those observations do not prove a restored visible Home after Standby foreground.

## Recommended next experiment

1. **Do not blindly repeat** direct event **322** or manager **appid=10, reason=11**: both were tested and rejected.
2. Identify the original *writer* and valid changes for the manager's integer **Standby status** using existing sanitized call traces, original embedded D-Bus metadata and controlled static inspection. Distinguish NotifyConfirmStatus's separate boolean from currentStandbyStatus.
3. In a **new disposable overlay**, change **one variable**, using original Home/manager/Standby apps and existing stable input/render baseline; verify before/after the original manager's state, genuine calls/responses, layer switch, original Home frame callbacks, AppAlive, and user-visible screens.
4. Require a real **Home → Standby/Clock → Home** cycle, visible/in-focus and navigable at both ends, **without** watchdog, manager kill, or black-screen regression. Only after repetition call this end-to-end usable.
5. Keep the manager's separate SysV IPC namespace, lab HMI callback rescue and private QML probing explicitly marked **experimental**; investigate correctness before folding into a stable launcher.
6. One agent owns the guest/overlays at a time. Any second Codex uses a separate worktree, analyzing existing artifacts without touching the first agent's live VM.

## Publication and provenance

No OEM executable, firmware, rootfs, QML, proprietary graphics, translated raw traces, vehicle data, private cores, screenshots newly supplied but not approved for public posting, or VM disks have been committed. Historical approved README gallery unchanged. This is an independent, isolated software-laboratory progress report, **not** a production emulator or vehicle security modification.
