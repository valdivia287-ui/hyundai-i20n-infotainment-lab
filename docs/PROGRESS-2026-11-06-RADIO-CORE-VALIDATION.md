Newer functional evidence: [original Radio round-trip and aligned Home](PROGRESS-2026-11-06-ORIGINAL-RADIO-ROUNDTRIP.md). Historical diagnostic limits below still apply.

# Radio diagnostic cores and evidence validation — 6 November 2026

At this earlier diagnostic checkpoint, the interactive Radio return was pending. This diagnostic does not replace the [texture, Spanish and Home recovery evidence](PROGRESS-2026-11-06-RADIO-TEXTURES-SPANISH.md).

## Completed diagnostic evidence

A late observer found that the first Radio process had already exited. Its retained natural core was only 8,470,528 bytes, while its ELF segments required 194,379,776 bytes. Intact thread notes did not make the missing stack/memory usable. A backtrace from that file must not be treated as reliable. The preceding OEM signal backtrace separately recorded a GUI-thread QtQuick wait; a later cleanup destructor failure is not proof of the original cause.

A separately labelled early diagnostic captured a complete 138,993,664-byte kernel core with 11 thread records. The original executable hash matched. The deliberate SIGQUIT capture reserved only that signal in the original Radio process, after a genuine Peer.Ping NoReply; the two owned guest supervisors were briefly paused during the dump and resumed afterward. This was a diagnostic intervention, never a stability or application-success result. Original firmware and reference profiles were preserved.

With matching libraries and SONAME aliases, the complete core resolves the main thread to IviShellIntegration::waitForGetSurfaceId, then QWaylandDisplay::blockingReadEvents and the Wayland dispatch/poll path. The surface-ID reply field was still zero. However, the surface-ID request had been sent less than a second before the trigger. **This captures initialization, not a demonstrated sustained IVI failure.** Do not fabricate a surface ID or bypass this original contract based on that snapshot.

The subsequent selective trial required consecutive genuine NoReply results, an existing QtQuick render thread and a GUI futex wait. Its complete 194,920,448-byte core has 12 thread records: the GUI waits in QWaitCondition/QtQuick, while the render thread waits in eglMakeCurrent → swrast_update_buffers → Wayland dispatch/poll, with a nonnull throttle callback. This is a captured wait, not proof of an indefinite deadlock; the diagnostic supervisor pause also limits causal conclusions.

The accompanying trace separately records an authentic Radio Ping method return emitted after the four-second caller deadline had elapsed. Radio's GUI did resume processing. This supports testing a bounded longer real-reply deadline before treating every NoReply as permanent unresponsiveness.

## Original public tool

`python3 tools/elf_core_summary.py /private/path/to/core` validates little-endian x86-64 ET_CORE metadata without executing the inferior or contacting symbol servers. It checks program-header bounds, nonempty file-segment bounds, bounded note parsing and thread PRSTATUS records. File-free mappings may legitimately point beyond EOF.

Exit 0 means structurally complete within these checks; exit 1 reports incomplete/invalid evidence; exit 2 reports an unsupported file or input error. This is not a debugger, a full ELF verifier or proof that the application was hung. Matching executable/shared libraries and causal timing remain necessary. Keep both the core and generated diagnostic output private.

Four new tests use wholly synthetic ELF bytes: complete multi-thread data, an interrupted dump with intact notes, legitimate file-free mappings beyond EOF, and rejected non-core input. All 23 public tests pass. No Qt implementation or OEM content was copied into this tool.

## Next functional test

Earlier original Radio GUI render waits measured approximately eight to nine seconds, exceeding the manager's four-second Ping deadline. A separate opt-in candidate extends only the genuine Radio Ping wait to 30 seconds, analogous to the existing Home-only diagnostic tolerance. It must still receive real original replies and demonstrate button input, unchanged PIDs, visible aligned Home return and subsequent page navigation. A longer deadline does not solve an indefinite wait and is not evidence of OEM timing fidelity. This candidate is now executing in another disposable overlay without deliberate signals or supervisor pauses; its functional result is not yet validated.

Original Spanish Radio presentation, the ten-minute complete-cycle check, clean-overlay repetition and the Windows launcher remain pending. The guest stays offline. No cores, raw traces, screenshots, OEM binaries, QML, maps or resources are published.
