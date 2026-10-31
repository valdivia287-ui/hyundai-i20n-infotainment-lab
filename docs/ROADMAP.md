# Roadmap

**31 October 2026, 16:43 UTC priorities:** Original Home now navigates **0→1→0 with ApplicationManager running**. Original Standby's visible Confirm button has produced a real **pressed/released/btnClicked** sequence in a private controlled QML diagnostic overlay. A lab-only Weston **hidden-Home frame callback rescue** and **Home-only llvmpipe** preserve Home heartbeat through a foreground transition in bounded runs. **Next blocker:** original ApplicationManager retains **currentStandbyStatus[10]** and rejects the OEM **appid2/reason12** return request. Identify the original state writer and valid transition; **do not repeat** rejected event322 or manager appid10/reason11 requests as fixes. Prove a visible, interactive, repeatable **Home → Standby → Home** cycle before packaging a Windows launcher. Preserve original firmware, separate experimental overlays and independent agent worktrees. See [latest integration report](PROGRESS-2026-10-31-HOME-STANDBY-INTEGRATION.md), [current status](STATUS.md) and [AI handoff](AI-HANDOFF.md).

1. **Publish safe, reproducible tools**: audit original scripts, dependencies, license provenance, private information and hardcoded paths. Provide synthetic fixtures and tests.
2. **Understand IVI visibility**: capture layer assignments, surface ID, buffers and actual composition.
3. **Map theme/variant selection**: distinguish persisted vehicle configuration from firmware defaults without inventing values.
4. **Map graphical resource paths**: document expected mount points and file lookup using metadata, not OEM assets.
5. **Investigate software ASTC support**: test with independently generated textures and document rendering alternatives.
6. **Characterize private D-Bus contracts**: capture interactions in isolated tests; do not fabricate vehicle data.
7. **Developer toolkit**: enable reversible Qt/QML UI experiments and regression tests without touching a vehicle.

A task is complete only with documented evidence, reproducible steps and limitations.
