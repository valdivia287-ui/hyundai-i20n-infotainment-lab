# BC3N25MY software profile: owner choice and native startup checks

The owner requests **BC3N25MY as the preferred software profile**. The physical vehicle remains reported as a **BC3N i20 N MY23**, Spain/Europe, with software last updated in 2025. Choosing the software profile does not establish a different physical model year or prove a match to the installed vehicle firmware. This preference supersedes earlier notes that excluded BC3N25MY from experimental software selection.

The existing original MICOM boot-information path is retained. The initial CarType comparison changes only synthetic boot payload byte3 (CarType), keeping European country 5, Spanish(EU) language 7 and the other payload fields unchanged. Original MICOM and AppLauncher interpret the reply. The Launcher receives no argv replacement in these trials. The fixture is synthetic, not a captured vehicle message. No physical CAN, vehicle hardware or new service replies are involved.

## Completed comparison

| Software selection | Original runtime observation | Visible result |
| --- | --- | --- |
| Previous CarType0 reference | Existing limited lab configuration; three instrumented Voice Memo117 UI/Back/Home cycles | Original Spanish Voice Memo content and decoded original artwork visible; recording/audio untested |
| CarType23, BC3 table | Native `vv23`, `nm2`, `pf0`, `sc0`, `vc65`; provider alive, logical117 registered | Home navigable; original117/28 request reaches manager but no requestShow117 or Voice UI |
| CarType81 (0x51), BC3N25MY, HighPerformanceCar0 | Native `vv81`, `nm2`, `sc1`, `vc66`, `ke:new`, `os1`, `osr9`, `un1`; **effective `pf0`** | Home navigable; MediaPlayer killed by original manager after six failed AppAlive probes, before the Voice icon input; no Voice UI |
| CarType81 plus HighPerformanceCar1 | Original Launcher logs the option1 and launches Home with native `vv81`, `nm2`, `pf1` | Two original N Mode pages, native Home return and further Home0 navigation verified; final Home matches initial exactly; artwork remains partial |

The old OEM diagnostic string reports numeric CarType23/81 as `Unknown value!!`. Identification here uses the original configuration table and actual child arguments, not a textual model label from that logger. The static BC3N25MY row contains pf1, but the zero-bit control produces effective pf0; the difference is resolved by the separate boot option: HighPerformanceCar1 produces native pf1. No child argument replacement is needed.

In the native81 Voice test the window observer logs entry to QQuickView show with dimensions1920×720, visible0/exposed0, but no completed show. The manager's kill precedes the original Home Voice request by more than one minute. This does not demonstrate an ASTC cause, a user-input crash or a failed rendered Voice return. Final Home differs from its initial reference only at the page indicator, and shutdown is clean. Native23 is a different failure: its provider survives but the manager does not dispatch the UI request.

## Native81 N Mode cycle verified

A separate offline overlay tests original N Mode 500/reason5185 under native CarType81, keeping the existing local HMI capability adapter and 21 decoded original textures. It uses no argv adaptation and does not change the frozen Home/Radio or earlier N Mode/Voice references. The native81 N Mode test completed: original Spanish Track content appeared, a real VNC swipe changed to page 2, the original Home control emitted the native 11/30 return, the aligned full Home menu reappeared, and a further VNC drag restored a Home0 image exactly matching the initial one. Four OEM process identities plus Weston were retained in four health samples;54 screenshot exports verified, no manager AppKill was seen, and shutdown was clean. Opening used a lab replay of the already observed original 500/5185 call; the native Home icon itself was not clicked in this run. Existing lab frontend/capability/timing/compositor adaptations remain explicit. Only 21 decoded textures were installed, so artwork is incomplete; these frames are not published as correctly rendered screenshots. This is a partial UI cycle, not a new ten-minute stability or sensor test.

Phone remains hardware-dependent without Bluetooth hardware or a paired smartphone; it is not a priority for further launch attempts. Relevant, correctly rendered screenshots are owner-authorized for publication; blank or failed-stage frames are excluded. No firmware, OEM resources, QML, binary, raw trace or map is included here.

## Separate HighPerformanceCar boot-option trial

Static inspection identifies the Launcher log field HighPerformanceCar as bit3 of the big-endian boot options word, corresponding to payload byte33, mask8. A separate fresh overlay changes only this bit while retaining native CarType81, the local capability adapter and baseline 21 textures. It tests whether the original Launcher itself selects pf1. Runtime evidence now confirms the original log HighPerformanceCar1 and native Home pf1. Two N Mode pages, native Home return, a subsequent Home drag and clean shutdown are verified; 51 screenshot exports pass. The local capability module remained loaded but produced no correction log. That absence alone did not prove it unnecessary; the following removal control supplies the missing evidence. The native81 argv adapter is absent throughout. A valid synthetic frame alone would not have established this GUI result.

The public pure fixture builder now exposes explicit language 7, CarType23/81 and the narrowly reviewed HighPerformanceCar option. Defaults preserve the earlier fixture vectors; unreviewed model/option combinations are rejected. It only prints synthetic bytes and opens no device or socket. Existing country/power/framing regressions and the added software-option checks pass: 35 tests. The field layout is a lab implementation of an observed OEM contract; no extracted configuration table or captured vehicle data is distributed.

## Control without the local capability module: verified

A third fresh N Mode overlay keeps native boot81/HighPerformanceCar1 and removes only the local capability module. The payload contains neither its marker nor its library. Actual Home maps and environment contain neither that module nor the argv adapter. Original Home still displays N Mode, accepts a VNC page swipe and returns to the complete aligned Home menu. A subsequent mouse click on the **original Home N Mode icon** emits 500/5185 from original AppHomeScreen PID1358, followed by original manager requestShow500 and the original N Mode UI. A second native 11/30 return restores Home, and a further page drag remains responsive.

Final Home differs from its initial reference only within the page indicator 610,703–669,712. Four OEM identities plus Weston remain stable in seven health samples, 57 exports verify, no manager AppKill appears, and shutdown is clean. The existing lab frontend/model, timing, input and compositor adaptations remain; only the N Mode capability and argv adapters have been eliminated. Twenty-one textures keep the control isolated, so artwork is still incomplete. Sensor telemetry, audio, full vehicle emulation and a new dedicated ten-minute stability test are not claimed. Earlier frozen Home/Radio, N Mode and Voice references are preserved.

Private evidence checkpoints: native81/option0 N Mode 125925; option1 with adapter 130821; option1 without adapter 131735. A read-only public verifier checks the latter run's native icon caller, arguments, adapter absence, boot frame/checksum, stable process identities, IVI owner, source-image hashes, Home geometry and clean shutdown. It requires the private evidence and Pillow; visual review remains necessary:

```sh
python3 tools/verify_native_bc3n25_evidence.py /path/to/private/completed-run
```

The standalone synthetic fixture can be reproduced without opening hardware:

```sh
python3 tools/bootinfo_fixture.py --country-code 5 --power-code 0 --language-code 7 --car-type-code 81 --high-performance-car
```

Next: enable the previously validated 66 additional original decoded textures in a separate native81 profile with explicit guards, verify complete original artwork and the icon/return cycle, then check Radio compatibility with the new native identity. Do not promote the new profile over the stable Windows Home/Radio launcher before those checks. Voice under native81/option1 remains untested; the earlier option0 failure must not be generalized to every native81 configuration.
