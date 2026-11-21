"""Round-trip sanity check for save reader/writer."""
import struct
import zlib
from pathlib import Path

from crimson_desert_save.reader import SaveFile, MAGIC, HEADER_FMT
from crimson_desert_save.writer import write_save


def _make_save(tmp_path: Path) -> Path:
    payload = struct.pack("<HI", 0x0010, 4) + b"\x01\x02\x03\x04"
    crc = zlib.crc32(payload) & 0xFFFFFFFF
    header = struct.pack(HEADER_FMT, MAGIC, 3, 0, len(payload), crc)
    p = tmp_path / "save_01.cdsav"
    p.write_bytes(header + payload)
    return p


def test_roundtrip(tmp_path):
    src = _make_save(tmp_path)
    save = SaveFile.read(src)
    out = write_save(save, tmp_path / "out.cdsav")
    assert SaveFile.read(out).payload == save.payload