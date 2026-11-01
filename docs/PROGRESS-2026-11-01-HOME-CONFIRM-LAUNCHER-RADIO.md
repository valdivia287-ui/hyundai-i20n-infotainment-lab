# 1 November 2026 — OEM AppLauncher, real Confirm-driven Home return, Settings and Radio investigation

> **Owner-supplied private progress cutoff: 10:19 UTC, 1 November 2026.** This is a *sanitized* summary of the owner's 532-line `ESTADO-PROYECTO.md` update. The raw runs, stack traces, OEM QML, binaries, screenshots, virtual machines and tools described here remain private. This is **reported local experimental evidence**, not a public, downloadable or independently reproduced Hyundai head-unit emulator.
>
> **Milestone:** In the private run **`20261101T095842Z-17749-1`**, **one real click on the original Standby Confirm button initiated the first and only original OEM return request**. Original ApplicationManager updated its foreground status to original Home, and a subsequent original pointer drag displayed a complete second page of the original Home UI. This is a controlled **Standby → original Home → interactive Home** path, **dependent on a reversible 10→45-second timer extension and experimental Weston compositing repair**; it is not a production-ready, timing-faithful OEM boot flow.

## Executive status

| Capability | Owner-reported evidence as of cutoff | Important qualification |
| --- | --- | --- |
| Original `AppLauncher` starts original manager, Standby and Home | Working private reduced app-list profile; original processes registered themselves and remained running in bounded trials | Startup uses lab-only environment correction and optional launcher timing extension; **not** stock vehicle initialization |
| Original Standby shows Confirm/Language | Confirm appears on original QML, receives real input and can emit request | Rendering/arrival timing can be slow and sometimes partially/black rendered under QEMU |
| **Original Confirm click initiates return to Home** | `20261101T095204Z-16827-1`, `20261101T095842Z-17749-1`: single original QML press/release triggers **only** `(304,2,12,1,0)`; original manager moves to `standby_status=12`, drawing Home11 | **Only verified with temporary targeted clock-timer extension**; 10-second nominal timing can issue an **automatic** request before user input |
| **Home is navigable after the Confirm-driven return** | `20261101T095842Z-17749-1`: genuine Wayland pointer drag changes original Home to its complete second page | Initial screenshot at +55 s was still a **partial** Home; this is not instantaneous, visually stable return |
| Original Settings submenu and back | `20261101T052217Z-19198-1` shows original Home-owned Settings submenu; `20261101T053427Z-13124-1` shows successful back-to-Home second page | Tested in earlier integrated profile with **automatic** Standby return, not separately verified in the Confirm-causal run |
| Original Radio icon generates real launch request | `20261101T101301Z-27925-1`: original Home QML sends `(304,70,32,1,0)` over genuine D-Bus to original manager | **AppEURadio did not start**, manager still drew Home; D-Bus return 255 **alone** does not determine success/failure |

## A. Original AppLauncher orchestration: root cause and controlled workaround

Original `AppLauncher` is now used rather than manually starting every OEM process. It sends its real preload-complete signal and original ApplicationManager updates `preload_complete_status` and `standby_status`. A reduced private app-launch configuration includes manager, Home and Standby; the full OEM launch table previously produced unrelated app restarts and is not a stable baseline.

- In **`20261101T025038Z-30966-1`**, a preserved original Home core showed a **Wayland protocol failure before a secondary `free()` SIGSEGV**, not primary allocator corruption. Original Home was accidentally inheriting `QT_WAYLAND_SHELL_INTEGRATION=ivi:ivi`; a one-variable reproduction confirmed the double shell selection led to an IVI protocol error. Removing the inherited setting **only from the launcher-parent environment** allowed the original child to choose `ivi` once.
- **`20261101T032004Z-1523-1`** showed original Home full screen at 50 and 110 s with original AppLauncher and manager and no earlier SIGSEGV. A later reduced launcher configuration starts original Home, Standby and manager, but AppLauncher’s original short timeouts caused Standby restarts.
- **`20261101T034232Z-26717-1`** used a **lab-only, selective extension of AppLauncher 10-second timers to 120 seconds** so original Standby registered autonomously; original Home and manager also registered. Genuine original `preload_complete_status=true` and `standby_status=11` were observed, although the launcher may send completion by timeout: **signal presence is not proof that every app is healthy**.
- The original manager recognized Standby as drawn on a genuine request; in the launcher-controlled profile the surface assignments were **Standby1000 and Home1001**, opposite earlier manually started profiles. The earlier HMI hidden-frame rescue assumed static 1000/1001 roles and was not universally correct.

**A separate, optional compositor-level experimental repair**, `hmi-controller-home-repair.so`, restores original Home surface1001 to foreground layer102 only in the observed case of Home being parked in layer4000, excluded from active repaint, while Standby has released its buffer. It preserves original OEM binary assets but is **not proof of faithful original Weston/vehicle compositing**. See earlier `20261101T045045Z-28913-1` and the 31 October report for the original callback/wait context.

## B. Standby → Home: distinguish *automatic timeout* from **actual Confirm**

The critical causal distinction required multiple controls:

1. Early launcher-controlled runs showed `standby_status=11→12`, Home11 drawn and sometimes visually restored **without any Confirm click**. A previous click followed by a visible Home return **could not establish causation**.
2. In **`20261101T054231Z-31758-1`**, the original manager received `(304,2,12,1,0)` from the *original AppStandbyClock process*, even with no user input. In **`20261101T091352Z-1495-1`**, a passive stack trace identified original `QTimer::timerEvent → onTimeoutHandler → confirmSkPressed → gotoHomeScreen` as a genuine **automatic return** path.
3. A control showed the original clock calls `QTimer::start(10000)`, and observed callback processing after **21.56 guest seconds** under the examined emulation schedule; the timing discrepancy does **not yet establish** a unique root cause. In trials without a timer change, the automatic request often preceded the real click, making visual outcome attribution invalid.
4. A narrowly scoped **reversible preload probe** increased **only the measured Standby clock timer from 10000 to 45000 milliseconds**, without modifying OEM QML, OEM executable, firmware base, response D-Bus contents or original mouse handler. Several initial runs were **invalid** because the probe depended on `__isoc23_sscanf`, absent in the guest's older libc. The probe was corrected by removing that dependency; those earlier failed trials do **not** count as OEM failures.
5. **`20261101T095204Z-16827-1`**: with that targeted timer extension and original Standby QML, one visible Confirm click produced **the first and only** original request `(304,2,12,1,0)`, with a stack rooted in original **QQuickMouseArea release → OEM Confirm handler → gotoHomeScreen**. There was **no QTimer-driven request** in the traced window. Original manager advanced to **standby11 then standby12**, drawing original Home11; original AppLauncher, manager, Home and Standby processes remained present. However the +55 s Home screenshot still lacked its complete icons, so **that trial alone did not prove navigable return**.
6. **`20261101T095842Z-17749-1`** repeated original QML + one-click timer-controlled return. The only request was from the original Confirm button handler (not timer). ApplicationManager reported **standby12 and drawn Home11**. Although a +55 s Home image remained partial (“Media Off”), a subsequent genuine drag on the returned original Home produced a **complete second Home page** with **Phone, Phone projection, Voice memo, Climate, Radio, Media, Manual and Settings**. Wayland pointer down/motion/up and changed screenshot checksums corroborated genuine interaction. The old baseline and OEM source files stayed intact, and QEMU shut down after the bounded test.

**Interpretation:** Original Confirm → original manager → original Home becomes *functionally navigable* with explicit experimental timing/composition adjustments. This is **not** evidence that the unmodified original 10-second timer always permits human confirmation, that the initial return image is immediate/complete, or that the entire system is stable in long runs.

## C. Original Home Settings: complete internal QML round trip

In separate controlled original Home runs following the **automatic** Standby return:

- **`20261101T051541Z-7765-1`** traced an actual Settings icon click to the original Home handler `itemID=24`, which opened its **internal Home QML Settings submenu**. This is *not* proof that a separate `AppSetup` process launched.
- **`20261101T052217Z-19198-1`** showed the original full-screen Settings submenu with **Sound, Phone connection, Profile, Theme/Layout, Display, Button and General**. Some original graphics were missing or dark; a Mesa `GL_INVALID_ENUM` on an original ASTC background was separately observed.
- **`20261101T053427Z-13124-1`** delivered a real click on the Settings back arrow and later displayed Home page1 **with original icons** after an intermediate partial repaint. Home remained in the same process without launcher restart.

This establishes an **internal QML Settings → Home** navigation path, subject to slow and incomplete rendering in QEMU. It must **not** be reported as a new independent OEM app.

## D. Radio icon: original request captured; application **not launched**

A single click on the original Radio icon after dragging Home to page1 was examined:

- Initial run **`20261101T100519Z-17623-1`** proved Wayland input reached original Home but did **not** prove that the QML handler recognized Radio; partial UI graphics impeded visual interpretation.
- The next run **`20261101T101301Z-27925-1`** captured original Home's real `MAIN_LIST_ITEMCLICKED_HANDLE 4`, `homeListSendToApp itemID=4` and original request **`eventid=304, appid=70, reason=32, plane=1, command=0`**. Original D-Bus send to `/transition` with `com.lge.avn.appmanager.screentransition.request` carried **`(304,70,32,1,0)`**.
- Home's D-Bus reply included **255**. **Do not interpret the code 255 alone as failure:** an earlier *successful visible* Standby transition also returned it. But at +20/+40 s original manager remained **standby12, drawing Home11**, and **no `AppEURadio` process** was observed. Therefore there is **no verified Radio launch**.
- The private reduced AppLauncher app-list profile covers **manager, Home, Standby** only. **Potential explanation to test, not a proven cause:** Radio's appid70 might require genuine registration, a dedicated on-demand start path, startup-order conditions or missing OEM dependencies.

**Next high-value test:** inspect original `AppEURadio` executable/config/launch registration **read-only** and the reduced original AppLauncher config, then use a **single isolated new overlay and one-variable change** to observe whether appid70 registers, whether AppLauncher starts a process, whether manager requests a real foreground and whether an actual Radio IVI buffer attaches. Compare D-Bus request/manager app state, process PID, Wayland surface/buffers, QML render and AppAlive. Do not claim functionality based only on a D-Bus return or an empty/black surface.

## E. Preserved references and precautions

- Retain **`20261030T020654Z-13522-1`** as earlier independently navigable original Home baseline.
- Retain **`20261031T163512Z-9562-1`** as Home page0→1→0 plus Standby foreground / bounded survival with original manager.
- Treat **`20261101T095842Z-17749-1`** as the **newly reported Confirm-driven return + original Home navigation reference**, explicitly labelled **timer-extended and lab-compositor-repaired**. Never silently replace a stock/untouched comparator or discard earlier overlays.
- Treat the original MICOM→manager power=16 experiment and subsequent `standby_status` state studies as a **separate integration path**, not proof that every later launcher-controlled run exercised that same synthetic UART boot state. See [the earlier 1 November MICOM report](PROGRESS-2026-11-01-MICOM-POWER-STATE.md).
- Keep single-VM ownership across Codex agents, immutable OEM firmware images, new qcow2 overlays, opt-in reversible probes and tightly bounded timeouts. Do not publish OEM firmware, executable, recovered QML, payload bytes, proprietary texture derivatives, cores, raw logs or unapproved screenshots; **no real vehicle, CAN injection or reflashing**.

## Next priorities

1. Save and annotate the **confirmed original Confirm-click→Home-navigation profile**, with exact caveats around the 45-second timer, launcher timeout workaround and foreground compositor repair; validate repeatability and renderer stability.
2. Investigate original **Radio appid70** registration and launch prerequisites using the original AppLauncher configuration, service dependencies and observed D-Bus/Wayland evidence; aim to open one **independent second original application**, not another internal Home menu.
3. Identify why nominal **10-second Standby timer** and render events are delayed under QEMU TCG; work toward unmodified timings rather than permanently extending timers.
4. Independently address ASTC graphics compatibility, partial/black frames, hidden-Home callback handling and AppAlive stability, with reproducible one-variable tests and no unsafe vehicle interaction.

**Public project state at 10:19 UTC:** real interactive Confirm-controlled return **achieved in a bounded modified-timing lab test**; standalone Radio launch, faithful OEM timing, fully working graphics and turnkey emulator **not achieved**.
