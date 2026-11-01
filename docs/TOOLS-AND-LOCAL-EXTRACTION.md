# Firmware acquisition, decryption toolchain and local reverse-engineering workflow

This document helps other **owners/researchers** inspect independently obtained **Hyundai i20 N BC3N / European Standard Gen5W_L** updates. It documents the toolchain visible in our private experiment notes and provides an original, redistributable **read-only scanner**. **It does not include OEM firmware, decryptor secrets, extracted kernel, or a claim that the full OEM kernel has been decrypted.**

**Important distinction:** *decrypting an update*, *extracting a filesystem*, *disassembling an ELF executable*, and *booting the original Hyundai kernel* are four different achievements. The private QEMU runs verify original Hyundai **userspace applications** with compatible laboratory Linux/QEMU support. Available public evidence does **not** establish that the original Hyundai boot kernel is running unchanged inside QEMU.

## 1. Get your own software from Hyundai

- Official European/Spanish site: https://update.hyundai.com/EU/ES/home
- Search vehicle/version: https://update.hyundai.com/EU/ES/search
- Check **i20 N**, **BC3N**, region **EUR**, `S5W_L`, and the actual vehicle/software identifiers.

Do not upload the downloaded package to this repository. Other Gen5W devices (especially Android-based variants) may have **different package formats, keys and operating systems**.

## 2. Tools: confirmed, external and optional

| Tool / component | Role | Status and provenance |
| --- | --- | --- |
| `update_decryptor` | Decrypt locally obtained supported update packages where the researcher has the lawful prerequisites | **External tool used/tried in private work**; its exact local version/build, key provisioning and command line were not recovered from the published lab notes. Do **not** claim this repository ships a working decryptor. See upstream research link below. |
| Python 3 / custom Bash scripts | Inspect package layouts, rebuild disposable overlays, run repeatable tests | **Observed in our private lab**; the executable scanner below is **new original public code** |
| `file`, `strings`, `readelf`, `nm`, `objdump` | Identify files and architectures, inspect symbols and disassemble **locally** obtained ELF programs | Standard Linux analysis toolchain. Exact invocations vary by target; recommended for reproducing static analysis |
| `debugfs`, `e2fsprogs`, `qemu-img` | Inspect Linux filesystems and virtual disk metadata without changing the original image | **QEMU / debugfs / qemu-img observed** in our lab |
| `gdb`, `strace` | Examine OEM app crash stacks, system calls and IPC inside the isolated guest | **Observed in private runtime traces** |
| QEMU / Weston / Wayland IVI / Mesa software renderer | Controlled graphics and IPC execution of original userspace components | **Observed functional in private tests**, with explicit custom lab modules |
| Ghidra / Binwalk / `unsquashfs` | Optional deeper static analysis, container identification and unpacking where appropriate | **Recommended external tools**; not claimed as actually used for every file in this lab |

Upstream third-party references (link, don't repackage another author's code):

- https://github.com/laralbir/hyundai-kia-gen5w-navi-firmware — EU Standard Gen5W firmware research; its `tools/phase2_decrypt` documents an **external** `update_decryptor` wrapper and `tools/phase4_explore` covers filesystem exploration.
- https://github.com/Helloyunho/gen5w-utils — upstream utilities for some Gen5W firmwares; check license and **variant compatibility** before use.
- https://github.com/cantcs/HKG_Gen5W_ReverseEngineer — primarily different system/variant research; **do not assume its Android partition workflow applies to BC3N Linux S5W_L**.

We do **not** copy external scripts, keys or bundled vendor data into this project.

## 3. Reproduce safe, **read-only** inspection in Ubuntu / WSL

Install common analysis utilities as needed:

```bash
sudo apt update
sudo apt install -y python3 file binutils e2fsprogs qemu-utils gdb strace
# Optional: sudo apt install -y binwalk squashfs-tools
```

After downloading **your own** Hyundai update, take an inventory **without attempting decryption**:

```bash
python3 tools/firmware_inventory.py "/path/to/your/update" \
  --output "/tmp/i20n-fw-inventory-private.json"
```

After extracting or decrypting **locally**, independently and with appropriate authorization, inspect the resulting directory similarly:

```bash
python3 tools/firmware_inventory.py "/path/to/your/extracted-rootfs" \
  --output "/tmp/i20n-rootfs-inventory-private.json"
```

The scanner records local relative paths, sizes, recognizable format headers, limited SHA-256 hashes and basic ELF machine types. It **never** executes, extracts, decrypts, mounts, flashes, modifies or uploads firmware. An unknown header is **not** evidence of encryption, and an ELF file is **not** proof of a bootable kernel.

Useful follow-up commands on independently obtained **local files**:

```bash
file "/path/to/your/file"
readelf -h "/path/to/your/extracted/AppHomeScreen"
readelf -d "/path/to/your/extracted/AppHomeScreen"
nm -D "/path/to/your/extracted/AppHomeScreen" | head -60
objdump -p "/path/to/your/extracted/AppHomeScreen" | head -80
strings -a "/path/to/your/extracted/AppHomeScreen" | head -80

# For an independently obtained local ext-family filesystem image:
debugfs -R 'ls -p /' "/path/to/your/rootfs.ext4"

# For a disposable QEMU disk or copy, query disk metadata:
qemu-img info "/path/to/your/lab-overlay.qcow2"
```

Use `tar -tf` only for **valid, already-decrypted TAR archives**. Encrypted files with `.tar.gz` names may not actually be gzip/tar. Do not mount arbitrary files writable, and do not extract an unknown archive directly into the host filesystem.

## 4. What was (and wasn't) reconstructed from our private project

- Private experiments demonstrably recovered an OEM **userspace** tree containing original `AppHomeScreen`, `AppLauncher`, `ApplicationManager`, Qt 5.4.1 and MICOM-related software, and launched selected components in QEMU.
- The experiments employed disposable qcow2 overlays, `debugfs`, QEMU, GDB, `strace`, Python and Linux binutils/ELF inspection.
- Our local work also involved `update_decryptor`, but the **actual decryptor binary, original wrapper, exact options and cryptographic prerequisites are not present in this public repository**. They cannot honestly be reconstructed from status prose alone.
- OEM **kernel decryption and booting** are **not verified** by the cited public results. The guest's compatible Linux kernel/modules must not be mislabelled as the original head-unit kernel.
- No proprietary filesystem, executable, Hyundai QML, maps, images, decryption secrets, real vehicle bus packets, private core dumps or full traces are included.

### For contributors with the private laboratory checkout

The original lab owner/Codex can add **actual local scripts used for extraction and analysis**, after identifying their provenance and checking for embedded proprietary data, keys and third-party license constraints. Export **newly authored generic wrappers** or clearly licensed upstream dependencies; publish a reproducible `--help`, minimal synthetic test fixture, input/output contract, and exact version for each. Never copy a raw directory from `/home/valdi/i20n-lab/codex-autonomo` into the public Git worktree.

## 5. Security and publication rules

Keep decrypted images, map data, core dumps, private traces, credentials, firmware keys and output manifests outside the Git tree. Report privately discovered command-line arguments in a sanitized form if they would otherwise include user data or secrets. This project supports offline interoperability research, **not** deployment to vehicles or bypassing protections on physical units.

See [firmware source and publication policy](FIRMWARE-SOURCE.md) and [project provenance checklist](../PROVENANCE.md).
