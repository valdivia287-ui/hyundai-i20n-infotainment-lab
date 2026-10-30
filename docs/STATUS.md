# Research status — 30 October 2026

**Experimental, isolated QEMU/Weston/Wayland IVI Hyundai i20 N infotainment laboratory.** The original Home interface has now **navigated from page 0 to 1** in a private test reported by Codex running **GPT-6 Sol Alto**. The overall OEM multimedia is **not yet complete**, and other applications have not been proven to launch. See [30 October progress](PROGRESS-2026-10-30.md) and [AI handoff](AI-HANDOFF.md).

> Evidence qualification: the findings below are based on progress logs and screenshots supplied by the owner; the underlying private VM, complete traces and diffs have not been independently inspected for this public report.

## Working foundation

- Original Hyundai `AppHomeScreen` and Qt 5.4.1 run in a disposable Linux/QEMU guest with Weston/Wayland IVI. Original OEM QML and recovered assets were loaded in guest overlays, leaving the base firmware untouched.
- AppHomeScreen rendered a partial genuine UI, later fullscreen; Codex reported stable screenshots at **110s** and **170s**, with **929,959 pixels** differing from the Weston reference. An earlier disappearing Home panel was explained by a **125-second test timeout**.
- Vehicle variant **BC3 = 23** was measured in original QML. A controlled overlay test changed active value from 5 to 23, added a third Home page indicator and saved the value in SQLite. This did not itself establish page navigation.
- Original application created SQLite tables (`MenuHome`: 3 rows; `CustomLayoutFront`: 25). Outgoing D-Bus header analysis identified **47 distinct calls**, including 12 appmanager registrations and 104 requests for unavailable MICOM; those are attempted calls, **not successful responses**.
- Localization remains incomplete: an English `.qm` file was found, but reading active language through shared memory failed. Some translation keys appear untranslated.

## 30 October: input and navigation breakthrough

1. The original `ivi-input-controller.so` was loaded in an isolated guest, and a lab utility confirmed `ivi_input` seat `default` acceptance for Home surface ID **0** on a retry.
2. Weston was initially directing touch toward a **reference interface surface IVI 2001** (`wl_surface@42`), not Home. Terminating only the auxiliary reference UI within a disposable guest removed that input blocker; simply hiding it had not sufficed.
3. After waiting for Home to be ready, the original client trace recorded **`wl_touch.down`, motions and `up`**. This was real delivery to the OEM client, not just the Linux kernel. The touch event by itself did not change the QML page index.
4. A pointer drag reached Home but original input-controller coordinates appeared unexpectedly small. Codex compared the original controller with a separate, **experimental, lab-built IVI controller based on public COVESA sources** and reported corrected pointer motion from approximately x=1430 to x=422. Provenance/licensing of any borrowed code needs an audit before publication.
5. The original QML then reported **`onMovingChanged: true`**, **`onFlickStarted`** and **`advancedModePageChange(1)`**; a captured frame reportedly showed **Home page 1**. These three pieces of evidence support an actual **page 0→1 navigation event** using the original Home application.
6. A subsequent click on an application icon reached the Home surface, but the screen stayed on Home. **Later, Codex running GPT-6 Astra Medio traced the N Mode icon press into the original Home application and reported an application-launch request with `appid=500`.** The lab's D-Bus service **`com.lge.hyundai.avn.appmanager` is missing/not registered**, so that target application does not open. This establishes a concrete app-manager launch blocker, **not** a working N Mode implementation.
7. Codex's selected model subsequently displayed **“Selected model is at capacity”**. This is a capacity limitation and does not establish that user credits were exhausted.

## Astra follow-up checkpoint (30 October)

- In a reported **1 min 57 s** Codex run under **GPT-6 Astra Medio**, the program identified the `appid=500` → missing appmanager-service dependency.
- Codex reported **8 passing checks, 281 verified hashes**, clean VM shutdown, preserved disposable overlays and logs.
- A configuration option to try the **original Hyundai ApplicationManager** has been prepared, **but it has not yet been executed/tested in QEMU**. This is the next bounded experiment, not a completed milestone.
- Local private files named in the Codex report: `ESTADO-PROYECTO.md` and `investigacion/nmode-click-20261030.md`; only their names and the report text are available to this public snapshot.

## Next work

- Inspect the latest private `runs/` logs, screenshots and patch diffs before new experiments; preserve the working software renderer and successful input/controller overlay.
- Validate the existing `appid=500` and D-Bus service-missing evidence in the newest private traces. **Run the prepared original ApplicationManager option in a fresh disposable overlay**, checking process startup, D-Bus name registration, handler behavior and any further dependencies. Do not simulate success or fabricate service answers.
- Characterize input-controller coordinate conversion and license provenance; prove the page transition is repeatable in a new disposable overlay.
- Continue original service orchestration, additional apps, localization and remaining ASTC graphics. Research RTX 3080 Ti/VirGL only in a separate optional setup.
- Aim for a **complete interactive OEM multimedia laboratory**, not one particular application.

## Publication

No OEM firmware, binaries, QML, textures, maps, keys, VM disks, unredacted raw logs or vehicle data are distributed. Only independently authored or appropriately licensed code and sanitized evidence may be published. No vehicle flashing, physical CAN injection or testing on the car.
