#!/usr/bin/env python3
"""Read-only local inventory of independently obtained firmware artifacts.

No decryption, firmware modification, network access, subprocesses, or extraction.
Output may contain private filenames/hashes: do not commit generated manifests.
"""
import argparse
import hashlib
import json
import os
import stat
from pathlib import Path


def classify(header: bytes) -> dict:
    """Best-effort container/architecture hints; never proof of decryption."""
    result = {"kind": "unknown"}
    if header.startswith(b"\x7fELF"):
        endian = "little" if header[5:6] == b"\x01" else "big"
        machine = int.from_bytes(header[18:20], endian)
        names = {3: "x86", 40: "ARM", 62: "x86_64", 183: "AArch64"}
        result = {"kind": "ELF", "bits": 64 if header[4] == 2 else 32,
                  "machine": names.get(machine, f"unknown({machine})")}
    elif header.startswith(b"\x1f\x8b"):
        result = {"kind": "gzip"}
    elif header.startswith(b"\xfd7zXZ\x00"):
        result = {"kind": "xz"}
    elif header.startswith(b"BZh"):
        result = {"kind": "bzip2"}
    elif header.startswith(b"\x28\xb5\x2f\xfd"):
        result = {"kind": "zstd"}
    elif header.startswith((b"PK\x03\x04", b"PK\x05\x06")):
        result = {"kind": "ZIP"}
    elif header.startswith((b"hsqs", b"sqsh")):
        result = {"kind": "SquashFS"}
    elif header.startswith(b"\x3a\xff\x26\xed"):
        result = {"kind": "Android-sparse-image"}
    elif header[257:262] == b"ustar":
        result = {"kind": "tar"}
    elif header[1080:1082] == b"\x53\xef":
        result = {"kind": "ext2/3/4-image"}
    return result


def scan_file(path: Path, display_name: str, max_hash_bytes: int) -> dict:
    entry = {"path": display_name}
    try:
        meta = path.lstat()
        if not stat.S_ISREG(meta.st_mode):
            entry["skipped"] = "not a regular file (includes symlinks)"
            return entry
        entry["size_bytes"] = meta.st_size
        with path.open("rb") as source:
            head = source.read(4096)
            entry.update(classify(head))
            if meta.st_size <= max_hash_bytes:
                digest = hashlib.sha256()
                digest.update(head)
                while True:
                    part = source.read(1024 * 1024)
                    if not part:
                        break
                    digest.update(part)
                entry["sha256"] = digest.hexdigest()
            else:
                entry["sha256"] = None
                entry["hash_note"] = "size exceeds --max-hash-mib; use sha256sum locally"
    except OSError as exc:
        entry["error"] = f"{type(exc).__name__}: unable to read"
    return entry


def scan(target: Path, limit: int, max_hash_bytes: int) -> dict:
    if not target.exists():
        raise FileNotFoundError(target)
    if target.is_symlink():
        raise ValueError("Symlink input is not allowed")
    if target.is_file():
        files = [scan_file(target, target.name, max_hash_bytes)]
        truncated = False
    elif target.is_dir():
        files = []
        truncated = False
        for root, dirs, names in os.walk(target, followlinks=False):
            dirs[:] = sorted(d for d in dirs if not (Path(root) / d).is_symlink())
            for name in sorted(names):
                if len(files) >= limit:
                    truncated = True
                    break
                path = Path(root) / name
                files.append(scan_file(path, path.relative_to(target).as_posix(), max_hash_bytes))
            if truncated:
                break
    else:
        raise ValueError("Expected regular file or directory")
    return {"schema_version": 1, "source_name": target.name,
            "note": "Local inspection only. File type hints are not decryption proof.",
            "count": len(files), "truncated": truncated, "files": files}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="local firmware file or extracted directory")
    parser.add_argument("--output", type=Path, help="optional LOCAL JSON report (never commit)")
    parser.add_argument("--limit", type=int, default=20000, help="maximum files (default: 20000)")
    parser.add_argument("--max-hash-mib", type=int, default=64,
                        help="hash files up to this size in MiB (default: 64)")
    args = parser.parse_args()
    if args.limit < 1 or args.max_hash_mib < 0:
        parser.error("--limit must be positive and --max-hash-mib nonnegative")
    report = scan(args.path, args.limit, args.max_hash_mib * 1024 * 1024)
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"Wrote local inventory ({report['count']} entries). Keep it private.")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
