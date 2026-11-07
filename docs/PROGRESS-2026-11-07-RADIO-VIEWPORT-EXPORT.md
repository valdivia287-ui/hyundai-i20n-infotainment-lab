# Repeated Radio viewport and optional Windows export — 7 November 2026

A single new, offline overlay completed the pending Radio-fit trial. The existing Spanish startup preparation was reused; Qt, IVI, translation and ten-minute stability diagnostics were not repeated.

## Runtime verified

After the initial original Confirm/Home/Radio/Home preparation, a local VNC operator changed Home page, reopened original AppEURadio, returned through its original Home control and changed Home page again. The same original Home and Radio processes survived the sequence.

The original window manager restored Radio's native 1920×720 destination on a 1280×800 laboratory output. A separate, opt-in laboratory HMI module fitted only the active Radio destination to 1280×730 after three genuine ApplicationManager getters agreed on Radio77. Its source remained 1920×720; layer and opacity were preserved. Original QML was not edited for this adaptation.

Full Radio artwork and the right-hand station control were visible after reopening. Home returned aligned. Its page1 content matched the complete reference; the final VNC page0 image matched the complete baseline pixel for pixel. Seven health samples retained all six original process identities. The guest was explicitly shut down cleanly, and logs were recovered afterward. The previous frozen software profile and default Windows launcher were preserved.

## Host export correction

The preceding attempt stopped because Windows screenshot export returned EIO, after the original image had already been saved inside its WSL run. That is a host export failure, not evidence of an AppHomeScreen crash.

Screenshots now remain mandatory in WSL. Secondary Windows export uses a temporary file, source/copy hashes and atomic replacement. Export unavailability or corruption is recorded locally without failing an otherwise valid guest experiment. Local original integrity and journal errors remain fatal. Six synthetic tests cover success, EIO, failed replacement, corrupted copy, missing original and changed original. All 77 exports in this new run verified successfully.

The stale Windows session record was examined and backed up before a new, separately identified session was started; it was not blindly deleted.

## Limits and next work

The Station List click reached original Qt after reopening, but subsequent images still showed FM. Its repeated-foreground visual transition remains unverified. Radio presentation was slow: an earlier post-click capture still showed Home, while a later capture showed complete Radio. Do not infer precise presentation latency between sampled images.

This is one bounded viewport/return/VNC result, not a new ten-minute stability claim. Radio and compositor RSS increased during foreground use; constant-memory operation is not established. The earlier independently verified post-cycle stability result remains separate. The Windows launcher has not been promoted or installed as a final usable product. Station List activation/presentation latency are the next targeted questions.

No RF stations, audio tuning, navigation, native ASTC or guest GPU acceleration are claimed. The guest remained offline. No firmware, OEM binaries, QML, translations, maps, images, captures, raw logs or cores are included in this update.

## Reproduction and offline verification

In the private laboratory, start `python3 host/windows-session.py start --profile radio-fit`; wait for `interactive_ready`. Use the existing VNC operator actions in order: `drag-left`, `radio`, optional `station-list`, `home`, `drag-right`, checking each original screen before continuing. Stop through `python3 host/windows-session.py stop`. Every startup creates a fresh overlay.

The original [offline evidence verifier](../tools/verify_radio_fit_evidence.py) reads a completed private run and prints JSON without VM access or evidence modification. It checks software hashes, geometry markers, real getter sequence, original process identities, captured RGB comparisons and local screenshot hashes. Pillow is required on the host. It does not ship the private inputs, and its output must remain private unless separately reviewed.

Example: `python3 tools/verify_radio_fit_evidence.py /path/to/completed/private/run`.
