# Research status — 29 October 2026

**Experimental, private QEMU/Weston/Wayland IVI laboratory. Not a complete head-unit emulator or a navigable OEM UI.** This page summarizes test outputs **reported by Codex and shown to the project owner**; full private traces, capture files, checksums and overlays have not been independently re-audited for this publication. For the current agent handoff see [AI-HANDOFF.md](AI-HANDOFF.md).

## Runtime milestones reported

- Isolated QEMU guest runs Weston/Wayland IVI, original Qt 5.4.1 and the OEM `AppHomeScreen` binary. Original SocketCAN startup dependency was solved in an isolated guest without any CAN traffic.
- A minimal Qt/QML rendering test produced the expected pixels, Wayland buffer attachments and commits. Owner-shared screenshots subsequently showed a genuine partial `AppHomeScreen` panel with background, `STR_HOME_RADIO` and `MEDIA OFF` within the Weston compositor.
- Latest controlled fullscreen Home session reportedly produced the OEM application's area at **110s and 170s**, with a **929,959-pixel difference** against the Weston baseline and corresponding surface-create/attach/commit and `switch_mode(2)` traces. **The earlier disappearance was traced to a 125-second test timeout**, not a demonstrated UI crash. These are bounded observations, not proof of indefinite stability.
- A byte-identical copy of the original QML (SHA verified by Codex) was used only in a disposable overlay. The trial variant setting **BC3 = 23** (original model value observed as **5**) altered the running home: database saved value 23 and a third page indicator appeared. This is an observed behavioral difference; it does **not** demonstrate a working N Mode screen.
- `AppHomeScreen` created SQLite databases; `MenuHome` had **3 rows** and `CustomLayoutFront` **25** in the completed trial. An earlier `no such table` error occurred before schema creation. The guest shutdown path was fixed to stop the Home PID via `TERM`, observe `CA_HOME_DONE 143`, and retain evidence including `client-home.txt` and copied SQLite outputs.
- A parser for outgoing D-Bus `sendmsg` headers reportedly identified **47 distinct calls**, including **12 registration messages** to `com.lge.hyundai.avn.appmanager` and **104 `AskCANMMCANMicomReq` requests** for the absent MICOM. This is evidence of attempted calls, **not** functioning services or fabricated responses.
- A usable English `.qm` translation file appears to exist, but reading the active language from shared memory fails; untranslated keys remain visible.
- Native QML includes horizontal `ListView` pages for widgets/menus. A synthetic swipe changed only pointer pixels, not the page index. Weston originally logged `ivi-controller: No ivi-input-module set`. The original `ivi-input-controller.so` was found in the private rootfs, checked for its SHA/dependencies and loaded in a new disposable guest, yet no client `wl_pointer.enter`/motion was observed. **Current pending experiment:** implement a small lab-owned `ivi_input` v1 client that explicitly accepts the `default` seat for **IVI surface 0**, verify compositor confirmation, then repeat an interactive gesture.
- ASTC resources were partly adapted for software rendering inside overlays; at least one additional asset is outside the converted set. RTX 3080 Ti/VirGL acceleration remains unproven and must stay separate from the stable software path.

## Immediate next steps

1. Complete and document the **`ivi_input` seat acceptance** test; verify `wl_pointer.enter`, motion/button events in the client, then a genuine QML `ListView` index change. If unsuccessful, check surface focus, seat association and coordinate mapping separately.
2. Recover the logs from a clean, reversible guest shutdown, and keep exact proof for BC3=23, fullscreen frames and any gesture response.
3. Trace the original localization/shared-memory contracts and D-Bus service startup **without synthetic MICOM/CAN responses**.
4. Characterize remaining software-rendering ASTC gaps; pursue GPU experiments only in independent overlays.
5. Investigate N Mode after working Home navigation is evidenced; no N Mode success has yet been shown.

## Evidence and publication policy

Keep `observed from owner-shared screenshots`, `reported from private logs`, `static source inspection` and `hypothesis` separate. Public reproduction files must be author-owned or synthetic. Do **not** distribute Hyundai firmware, QML, textures, binaries, keys, raw memory dumps, private VM disks, or unredacted traces. No experiments on a physical vehicle.
