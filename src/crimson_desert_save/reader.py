"""Binary save reader for Crimson Desert .cdsav containers."""
from __future__ import annotations

import struct
import zlib
from pathlib import Path
from typing import BinaryIO

MAGIC = b"CDSV"
HEADER_FMT = "<4sHHII"  # magic, version, flags, payload_len, crc32


class SaveFile:
    def __init__(self, path: Path, version: int, flags: int, payload: bytes) -> None:
        self.path = path
        self.version = version
        self.flags = flags
        self.payload = payload

    @classmethod
    def read(cls, path: Path) -> "SaveFile":
        with path.open("rb") as fh:
            return cls._parse(fh, path)

    @classmethod
    def _parse(cls, fh: BinaryIO, path: Path) -> "SaveFile":
        raw = fh.read(struct.calcsize(HEADER_FMT))
        magic, version, flags, length, crc = struct.unpack(HEADER_FMT, raw)
        if magic != MAGIC:
            raise ValueError(f"{path.name}: not a Crimson Desert save (magic={magic!r})")
        body = fh.read(length)
        if zlib.crc32(body) & 0xFFFFFFFF != crc:
            raise ValueError(f"{path.name}: payload CRC mismatch")
        return cls(path, version, flags, body)


def decode_sections(payload: bytes) -> dict:
    # section table: [u16 id][u32 len][bytes]
    out, cursor = {}, 0
    while cursor + 6 <= len(payload):
        sec_id, sec_len = struct.unpack_from("<HI", payload, cursor)
        cursor += 6
        out[sec_id] = payload[cursor : cursor + sec_len]
        cursor += sec_len
    return out