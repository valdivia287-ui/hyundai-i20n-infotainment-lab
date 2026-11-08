# AI agent handoff — Hyundai i20 N infotainment lab

**Current as of 8 November 2026.** Earlier handoffs (30 Oct – 7 Nov) are preserved in [history/AI-HANDOFF-to-2026-11-08.md](history/AI-HANDOFF-to-2026-11-08.md); their "next steps" are superseded.

## Where the truth lives

The public repository holds documentation and author-owned tools only. The owner's private lab (not in this repo) is centralised under one root, `<OWNER_HOME>/i20n-lab/codex-autonomo`:

| Private file | Purpose |
| --- | --- |
| `LEEME-LABORATORIO.md` | Entry point and layout |
| `ESTADO-PROYECTO.md` | Current human-readable state and exact stopping point |
| `CONTINUIDAD.json` | Already-proven results, evidence paths, artifact hashes, rules |
| `LABORATORIO.json` | Official profiles (product / development / historical) and paths |
| `estado.json`, `windows-session.json` | Runtime files written by the tools — read, do not hand-edit |
| `runs/`, `host-logs/` | All runs/overlays and host logs; indexes in `runs/INDICE.json` |

Read-only checks: `python3 herramientas/laboratorio.py estado|verificar` and `python3 herramientas/coherencia.py`. None of them starts a VM.

## Resume protocol

1. Inventory first: `git status`, newest `runs/`, live `qemu-system*` / worker processes and their owner. Keep **one** guest operator.
2. The owner pause (`estado.json` → `owner_pause.active`) must be explicitly lifted by the owner before any VM start.
3. Start from the pending list in [STATUS.md](STATUS.md#pending-in-suggested-order) — currently the Phone121 click with original NotificationManager present.
4. Use the development profile (`herramientas/desarrollo`), a new disposable overlay, one change per run. Never modify the accepted product, its manifest or the base images.
5. Do not repeat settled work (Home, Radio, N Mode, Manual, Spanish, Qt/EGL, SwapInterval, stability) without a concrete documented regression. A fresh overlay losing a stored selection is a preparation regression, not a new translation problem.
6. Separate **reported**, **inspected**, **runtime-proven** and **hypothesis**. A D-Bus return 255, a first NoReply or a single retained screenshot is not success or failure by itself.

## Safety and sharing

No physical-car tests, CAN/MICOM injection, firmware flashing, reset/update/Variant/DTC/engineering/eCall actions, or network access from the guest. Do not publish OEM firmware, QML, binaries, textures, UART payloads, cores, raw logs, PINs or unapproved screenshots. Any public code must be original or licence-audited with attribution.
