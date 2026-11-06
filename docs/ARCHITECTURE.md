# Modular offline laboratory architecture

| Module | Boundary and present status |
| --- | --- |
| QEMU / Linux | Disposable overlays, private OEM inputs, isolated network |
| Weston / graphics | IVI, software GL; experimental Home foreground repair opt-in |
| Hyundai applications | Original private executables/resources; no public redistribution |
| ApplicationManager / AppLauncher | Original processes; restricted private preload list, experimental timing |
| MICOM / virtual hardware | Prefer original MICOM downstream of explicit synthetic UART fixtures |
| Virtual GNSS | Contract discovery pending; fixed synthetic position first, route replay later |
| Modem / SIM / connectivity | Contract discovery pending; no real SIM or Hyundai cloud impersonation |
| Laboratory D-Bus | Only observed contracts, deterministic labelled simulation, independently switchable |
| Navigation / maps | Launch, map availability, position reception and routing validated separately |
| Windows launcher | Consolidation pending after the functional application profile |
| Diagnostics | Bounded traces kept private; public tool operates on an explicitly selected PID |

Experimental modules remain separate from functional reference profiles until validated. A synthetic input fixture must state its source, interface, arguments, expected response and observed OEM effect. “Service running”, “valid position”, “map displayed” and “route calculated” are separate results.

See [current status](STATUS.md), [latest Radio investigation](PROGRESS-2026-11-01-RADIO-FILTERING.md) and [firmware acquisition rules](FIRMWARE-SOURCE.md).

## Original diagnostic tool

`bash tools/trace-process.sh PID NEW_OUTPUT_DIRECTORY SECONDS` attaches a bounded strace (1–30 seconds), then interrupts only its own tracer. It does not signal the selected application. Requires Bash and strace plus existing local ptrace permission; do not change global security settings to run it. Output can contain proprietary data or identifiers and must remain outside the public working tree. Validate application behavior separately because tracing can affect timing.

The tool is original laboratory code under the repository MIT license. No OEM files or code are included.

The published boot-info fixture retains diagnostic payload byte1=2, observed as manager power16. It reproduces the eligibility experiment; it is not a ready-to-use Home operating profile.

`python3 tools/elf_core_summary.py /private/path/to/core` checks bounded x86-64 ELF core metadata offline, without running the application or loading debugger scripts. Structural completeness does not establish a hang or matching libraries. Diagnostic outputs and cores remain private. See [core validation and timing limits](PROGRESS-2026-11-06-RADIO-CORE-VALIDATION.md).
