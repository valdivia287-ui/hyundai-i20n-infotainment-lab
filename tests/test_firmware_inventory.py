#!/usr/bin/env python3
"""Synthetic-only tests for tools/firmware_inventory.py (no OEM inputs)."""
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "firmware_inventory.py"
spec = importlib.util.spec_from_file_location("firmware_inventory", MODULE_PATH)
fw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fw)


class FirmwareInventoryTest(unittest.TestCase):
    def test_elf_architecture(self):
        fake = bytearray(64)
        fake[:6] = b"\x7fELF\x02\x01"
        fake[18:20] = (62).to_bytes(2, "little")
        self.assertEqual(fw.classify(bytes(fake)),
                         {"kind": "ELF", "bits": 64, "machine": "x86_64"})

    def test_known_container_magic(self):
        self.assertEqual(fw.classify(b"\x1f\x8bhello")["kind"], "gzip")
        self.assertEqual(fw.classify(b"hsqs" + b"\0" * 60)["kind"], "SquashFS")
        self.assertEqual(fw.classify(b"\x3a\xff\x26\xed")["kind"], "Android-sparse-image")
        self.assertEqual(fw.classify(b"xyz")["kind"], "unknown")
        self.assertEqual(fw.classify(b"\0" * 1080 + b"\x53\xef")["kind"],
                         "ext2/3/4-image")

    def test_directory_scan_and_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "b.gz").write_bytes(b"\x1f\x8btest")
            (root / "a.bin").write_bytes(b"hello")
            report = fw.scan(root, limit=10, max_hash_bytes=1024)
            self.assertFalse(report["truncated"])
            self.assertEqual([x["path"] for x in report["files"]], ["a.bin", "b.gz"])
            self.assertEqual(report["files"][0]["sha256"],
                             hashlib.sha256(b"hello").hexdigest())
            self.assertEqual(report["files"][1]["kind"], "gzip")
            self.assertFalse(any(str(root) in x["path"] for x in report["files"]))

    def test_large_file_hash_is_skipped_and_limit_applies(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "01.bin").write_bytes(b"abc")
            (root / "02.bin").write_bytes(b"1234")
            report = fw.scan(root, limit=1, max_hash_bytes=2)
            self.assertTrue(report["truncated"])
            self.assertEqual(report["files"][0]["sha256"], None)
            self.assertEqual(report["count"], 1)

    def test_symlink_not_followed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "regular").write_bytes(b"test")
            (root / "link").symlink_to(root / "regular")
            report = fw.scan(root, limit=10, max_hash_bytes=1024)
            links = [x for x in report["files"] if x["path"] == "link"]
            self.assertEqual(len(links), 1)
            self.assertIn("skipped", links[0])
            with self.assertRaises(ValueError):
                fw.scan(root / "link", limit=10, max_hash_bytes=1024)


if __name__ == "__main__":
    unittest.main()
