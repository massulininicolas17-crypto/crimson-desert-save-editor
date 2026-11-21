"""Save writer — re-packs mutated sections with correct CRC."""
from __future__ import annotations

import struct
import zlib
from pathlib import Path

from .reader import MAGIC, HEADER_FMT, SaveFile


def pack_sections(sections: dict[int, bytes]) -> bytes:
    chunks = []
    for sec_id in sorted(sections):
        body = sections[sec_id]
        chunks.append(struct.pack("<HI", sec_id, len(body)) + body)
    return b"".join(chunks)


def write_save(save: SaveFile, out_path: Path) -> Path:
    payload = pack_sections(save.sections) if hasattr(save, "sections") else save.payload
    crc = zlib.crc32(payload) & 0xFFFFFFFF
    header = struct.pack(HEADER_FMT, MAGIC, save.version, save.flags, len(payload), crc)
    out_path.write_bytes(header + payload)
    return out_path