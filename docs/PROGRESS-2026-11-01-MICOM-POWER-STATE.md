# 1 November 2026 — OEM MICOM startup and real ApplicationManager power-state transition

> **Latest owner-supplied report cutoff: 01:58 UTC, 1 November 2026.** This sanitized technical summary is derived from a private `ESTADO-PROYECTO.md` supplied by the owner. The repository does **not** include the original OEM firmware, binaries, UART response data, images, source QML, raw traces, VM overlays or private runtime logs. Results are reported from local Codex investigations and have **not been independently reproduced** from this public repository.
>
> **New verified milestone:** Original Hyundai MICOM responded to a **single synthetic virtual-hardware boot-information reply** via QEMU UART. MICOM itself emitted the corresponding **genuine D-Bus response**, original ApplicationManager accepted it (`reply is VALID`), and the manager's **`power_status` changed from 1 to 16**. **This does NOT yet prove `currentStandbyStatus` changed from 10 to 11 or that Standby returns to Home.** That integration was still under test at the report cutoff.

## Why this matters

On 31 October the original AppStandbyClock's Confirm button became genuinely interactive in a controlled private lab QML overlay (pressed/released/btnClicked: **P=R=C=1**). Its resulting original request **appid 2, reason 12** was rejected by original ApplicationManager with **`currentStandbyStatus[10]` / `StandbyStatus is not enabled[10]`**. The return-to-Home transition has not been achieved. See [31 October foreground and return investigation](PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md).

On 1 November, static investigation of the **original ApplicationManager executable** indicated the branch that would emit **Standby status 11** requires its power-status property to equal **16**. Previous original manager observations had **`power_status=1`**. This narrowed the investigation to a specific power initialization dependency; **meeting the power precondition does not guarantee a second unknown guard will pass**.

## Chronology and test evidence (private run IDs)

| Run | Owner-reported observed result | Limitations |
| --- | --- | --- |
| **`20261101T012316Z-4751-1`** | Original Home visible in two captures, genuine Standby buffer attached and original manager foregrounded Standby. Original `/clock` calls replied. Method `/Information com.lge.avn.appmanager.info.set_request_standby_screen` was called once; original `ask_standby_status` returned **10 before and after** and manager logged **`return Logic OFF`**. An original `power_status=1` event was visible. | A successful method invocation is **not** a Standby state transition. The original ELF branch requiring power 16 was identified by static analysis, not by a functioning return. |
| **`20261101T013557Z-29220-1`** | Original MICOM failed its initialization when **`TCGETS/TCSETS` on `/dev/ttyS1` returned `EIO`**. Launching OEM DLT alone was insufficient. | Isolated diagnosis, not a working MICOM instance. |
| **`20261101T013715Z-19560-1`** | Adding a **second QEMU virtual UART with null backend** allowed those terminal ioctls to succeed. Original MICOM registered its genuine system-bus name **`com.lge.car.micom`** during a bounded **60-second** test. | Bus registration proves service startup, **not** successful hardware emulation, power state change or vehicle communication. |
| **`20261101T014027Z-6473-1`** | A bounded attempt to read manager power status while real MICOM was alive was reported as **started** in an earlier status. | No final outcome for this specific run is present in the latest supplied brief; do not invent one. |
| **`20261101T014824Z-15950-1`** | Calling original **`NotifyMonitorPowerEvent(16)`** reached original manager but **did not change `power_status`**, which stayed **1**. | This direct notification is **not** the working boot-initialization path. |
| **`20261101T015448Z-28405-1`** | A single synthetic virtual-hardware response to an **authentic original MICOM `AskSysBootinfo` request** was processed by MICOM. The **original MICOM** then generated a genuine D-Bus reply; ApplicationManager logged **`reply is VALID`**, its state switched **`power_status=1 → 16`**, and the OEM getter returned **16**. Original Home was visibly rendered fullscreen at 110 seconds. | The reply is a **lab-generated fixture, not vehicle capture**. The payload's response identifier **`0x8201`** and power byte value **2** came from static OEM-binary examination; **remaining payload bytes were zero-filled synthetic data**. This establishes *one successful authentic OEM processing chain*, not full MICOM protocol support. |
| **`20261101T015819Z-13437-1`** | **Integration underway** combining the validated UART-response lab fixture with prior stable original Home + ApplicationManager + Standby profile. OEM MICOM and DLT intended to remain running until the transition. | **Not yet reported:** whether `set_request_standby_screen` moves `currentStandbyStatus` from **10 to 11** while `power_status=16`; no return to Home yet. |

### Evidence chain: synthetic hardware input versus original software output

**Synthetic only at the virtual-hardware boundary:**

`QEMU UART (second virtual port, no physical cable) → single lab-generated response to MICOM AskSysBootinfo`

**Authentic original OEM software behavior after that input:**

`Original MICOM process → real OEM D-Bus reply → original ApplicationManager validates reply → power_status=16`

No physical vehicle connection, CAN traffic, real vehicle serial feed or Internet access is part of these tests. The first result does **not** establish that the rest of MICOM's asynchronous messages are emulated, that `power_status=16` is stable throughout all later lifecycle states, or that an application can successfully navigate back to Home.

## Concrete next test and verification gates

1. **Before changing anything, inspect newer private run artifacts after 01:58 UTC**; the report's last run `20261101T015819Z-13437-1` was **still in progress** at cutoff.
2. In **one disposable overlay** using the already validated MICOM UART fixture, compare original **`ask_standby_status`** before and after `set_request_standby_screen`, while proving original manager **`power_status=16`** *at the time of that call*. Record original manager response, relevant branch diagnostic messages and actual status change or unchanged value.
3. **If status becomes 11**, move to a **separate controlled test** of original Confirm click and **true visible Home return**; require original Home interaction, manager foreground/drawing state, stable hidden frame callbacks and `AppAlive`, and no watchdog or SIGTRAP. **Do not conflate power 16 with accomplished return**.
4. **If status remains 10**, determine any other original branch guards or lifecycle dependencies through static inspection and observed OEM calls; do not fabricate extra state, install a generic always-success D-Bus mock or repeatedly brute-force events.
5. Preserve earlier baseline `20261030T020654Z-13522-1` (original navigable Home), `20261031T163512Z-9562-1` (original Home with manager / Standby foreground, bounded survival), and earlier ten-minute coexistence runs. Never write to firmware base; use separate qcow2 overlays, original-binary read-only inspection, isolated agent worktrees and **only one active QEMU owner**.
6. Explicitly keep the existing lab-only workarounds separate from OEM behavior: **isolated SysV IPC namespace for manager**, experimental Weston callback rescue, Home-only llvmpipe and QML input focus adjustment. Do not present them as faithful original in-car conditions.

## Current status and publication boundary

**Verified (owner report):** MICOM startup with virtual UART, the original `AskSysBootinfo` → MICOM D-Bus → ApplicationManager path, and `power_status=16` in one bounded test. **Pending (not claimed):** manager Standby status **10→11**, genuine **Home→Standby→Home** navigation, stable graphics, fully functioning vehicle-service simulation and Windows one-click launch.

**Never publish:** OEM executable/binary data, firmware/decrypted rootfs, proprietary QML, UART packet bytes/captures, raw trace, core, original or derived OEM textures, unapproved screenshots, private paths revealing sensitive info, keys or secrets. This document contains only sanitized descriptive metadata and non-sensitive outcome labels.
