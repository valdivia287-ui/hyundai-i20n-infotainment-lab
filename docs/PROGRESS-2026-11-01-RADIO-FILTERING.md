# Radio launcher filtering and modular simulation — 1 November 2026

## Runtime evidence from the private laboratory

The original Home Radio item4 sends `(304,70,32,1,0)` to the original ApplicationManager. A return value of255 alone does not classify the outcome. In the observed trials, Home remained the drawn application and no independent Radio process was present.

| Private run | Controlled change | Observed result |
| --- | --- | --- |
| `20261101T102157Z-21973-1` | AppEURadio added to launcher group3 | Group3 contained zero accepted applications |
| `20261101T102919Z-31265-1` | AppEURadio moved to group4 | Group4 contained zero accepted applications |
| `20261101T103814Z-9844-1` | Original AppOSDManager in group3, AppEURadio in group4; short startup observation | Group3 accepted AppOSDManager ID22; group4 still empty |

The last result rules out an empty preceding group as the sole explanation. The test ended before evaluating AppOSDManager functionality. It does not demonstrate a working Radio application.

## Static analysis and open questions

The original launcher has an AppEURadio entry with ID77. Home's ID70 request therefore must not be treated as proof that AppEURadio itself has ID70. Loader code looks up the application name and then applies an application eligibility predicate; the ID77 path examines a startup configuration byte. Its source and semantics still need runtime confirmation. Do not force eligibility or invent an undocumented vehicle response merely to report progress.

A subsequent bounded startup trace (`20261101T135745Z-23759-1`) observed three authentic `AskSysBootinfo` calls to original MICOM, each logged as `NoReply`; AppLauncher then logged fallback defaults including `Country=Korea`. This is an upstream startup failure, not proof of the final reason Radio is filtered. Next: test the existing deterministic UART boot-info fixture against original MICOM in this integrated launcher profile, then map the eligibility field before choosing regional data. Preserve the original MICOM service where practical.

## Functional reference retained

The genuine original Confirm→Home→page1 flow remains demonstrated by `20261101T095842Z-17749-1`. It requires the experimental Standby timer extension10000→45000ms and the separate compositor Home foreground repair. Neither original timing fidelity nor a fully stable independent Radio launch is established. Private firmware and reference overlays remain separate from this repository.

## Simulation scope

Modules are opt-in and validated separately: QEMU/Linux; Weston/graphics; OEM applications; OEM AppLauncher/ApplicationManager; original MICOM with synthetic physical input; future virtual GNSS; future modem/SIM/connectivity adapter; lab D-Bus services; navigation/maps; Windows launcher; diagnostics. Synthetic inputs must have a deterministic fixture, provenance, observed contract and recorded OEM response. No Hyundai account, cloud subscription or credential impersonation is permitted.

GNSS, modem and navigation contracts are still pending investigation. A fixed synthetic position is a future first test; it does not establish map loading or route calculation. Offline service dependencies must be checked independently.

## Publication

No OEM files, raw private logs, new screenshots, maps or credentials accompany this report. The three previously owner-approved Confirm/Home captures retain their existing authorization. Participants obtain compatible BC3N Gen5W_L materials independently through the [official Hyundai portal](https://update.hyundai.com/EU/ES/home) and [official search](https://update.hyundai.com/EU/ES/search).

## Verified regional input through original MICOM

A matched control `20261101T140116Z-28293-1` answered one observed UART boot-info request with an explicitly synthetic 36-byte payload (byte1=2, remaining bytes zero). Original MICOM processed it and original AppLauncher logged Country0/Korea without the previous three boot-info NoReply errors. AppEURadio remained excluded.

In `20261101T140338Z-23977-1`, only payload byte4 changed from0 to5 (plus the XOR checksum). Original AppLauncher logged **Country5/Europe** and admitted **AppEURadio77 into group4, count1**. This validates that field and its effect on the original loader. It does not yet prove an AppEURadio process, display, audio, tuner or return-to-Home interaction. The complete integrated profile with this input is the next validation.

`tools/bootinfo_fixture.py` independently constructs the two synthetic control/Europe frames, labels its JSON as synthetic, and opens no device or socket. `tests/test_bootinfo_fixture.py` checks the recorded synthetic vector, isolated byte/checksum change and unsupported input rejection. Neither frame is captured vehicle data. This is a partial diagnostic model; most boot fields remain zero and must not be interpreted as a coherent complete car configuration.

## Full launch attempt and power-state limitation

`20261101T140539Z-30883-1` did launch original AppEURadio and obtain native registration for ID77. The compositor observed original Radio IVI clients. The trial also had an AppEURadio crash/restart and manager-directed restarts of OSD/Home; Confirm was not visible and no click was sent. Its inherited synthetic power byte2 produced manager power16, incompatible with the previously working Home profile. Registration is therefore established; interactive stable Radio is not.

The existing private power mapping must be retained: payload byte1 values1→manager17, 2→16, 4→0, other values→1. A short power1 trial merely reconfirmed known mapping and should not be repeated. The next integrated validation uses country5 and power-byte0 (expected manager1), omits OSD and adds only Radio in group3.

Static inventory located LocationManager, Tms applications and NaviUpdateApp in the private base. LocationManager references its own D-Bus service, GNSS and HippoReader. The receiver protocol, modem contract, navigation runtime and map availability remain unverified. Updater executables were inventoried, not executed. Absence of AppNavi/AppGPS under that base's `/app/bin` alone does not establish absence from other firmware mounts.

## Keeping the virtual UART endpoint available

The first single-response Europe/power0 trial reverted to boot-info NoReply and Korea defaults. In bounded control `20261101T141858Z-6188-1`, the lab adapter kept its UART socket connection available and answered only observed boot-info requests with the same Europe/power0 frame. OEM AppLauncher logged Country5/Europe and accepted AppEURadio77 in group3; OEM manager reported power1. Only one reply was needed in that recorded control. Connection lifetime versus other timing effects still needs isolation, so this is not proof that repeated replies themselves fixed the problem. The full integrated UI validation uses this available-endpoint profile.

The offline fixture constructor now supports `--country-code 5 --power-code 0`. Power1 was observed to produce manager17; diagnostic power2 produces16. Fixtures remain incomplete synthetic boot states, not captured vehicle configurations.

## Original Radio FM is visible; interaction and combined stability pending

`20261101T142059Z-replay-8a6447-1` launched and natively registered AppEURadio77 (PID772) with the Europe/power0 fixture. A private compositor capture shows the original Radio FM interface, Station list and favourites help text. This is evidence of an original Radio UI, not proof of audio, tuning, station discovery or Home-driven launch. No new screenshot is published here.

The previous Confirm brightness detector falsely accepted this Radio screen. The supervisor was safely stopped; its click cannot be credited as a Confirm transition. The private detector now also checks central text brightness against the known Confirm observation. Home underwent repeated manager-directed terminations/restarts in this combined trial. The existing Home/Confirm functional reference is preserved separately.

Next validation: dedicated Radio UI observation with a visual FM guard, one real Station list click, before/after captures and manager/PID checks. Then investigate original service dependencies, preserve Home alongside Radio, and test return. Do not call this a complete emulator or a stable combined profile.

The dedicated UI check `20261101T142646Z-replay-601798-1` found original Standby/Confirm in front of registered Radio. Its visual FM guard rejected that screen and sent no Station list click. This is a negative interaction result, not a Radio failure diagnosis. Home again received manager-directed termination code5 and restarted. The corrected Confirm detector is being evaluated separately before another Home-driven Radio claim.

## Manager-directed Home termination traced

In `20261101T143152Z-replay-edf4f4-1`, the corrected visual Confirm detector admitted the real Confirm screen and its genuine handler emitted the return request, but the combined profile still did not establish a Home-driven Radio transition. Radio77 remained registered; final manager values were power1, standby11, drawn0 and managed10. The screen was partial. Home was restarted repeatedly.

A bounded manager trace in `20261101T143925Z-replay-bb73e0-1` identified the termination sequence: original manager sends `org.freedesktop.DBus.Peer.Ping` to original Home service `com.lge.hkmc.avn.appfunc.AppHomeScreen`, path `/com/lge/hkmc/avn/appfunc/appInterface`; it logs NoReply, increments Home `m_AliveCnt`, then calls AppKill at count6. This establishes the kill mechanism, not the reason Home fails to answer. Next: correlate Home main-thread stacks and D-Bus delivery during those pings. Do not replace the replies with synthetic success or disable liveness checks to claim stability.

The private compositor repair also assumes Home surfaceID1001. Repeated OEM process/surface recreation makes that assumption a limitation to verify before assigning application foreground ownership. Genuine Radio rendering and correct OEM foreground state are distinct evidence.
