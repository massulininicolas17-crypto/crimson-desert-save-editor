"""Save profile discovery — scans Crimson Desert userdata directories."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

DEFAULT_ROOTS = [
    Path(os.environ.get("USERPROFILE", "")) / "Documents" / "CrimsonDesert" / "SaveGames",
    Path(os.environ.get("LOCALAPPDATA", "")) / "PearlAbyss" / "CrimsonDesert" / "saves",
]


@dataclass(frozen=True)
class SaveProfile:
    slot: int
    path: Path
    size: int
    modified: float


def scan_profiles(roots: List[Path] | None = None) -> List[SaveProfile]:
    profiles: List[SaveProfile] = []
    for root in roots or DEFAULT_ROOTS:
        if not root.is_dir():
            continue
        for f in root.glob("save_*.cdsav"):
            try:
                slot = int(f.stem.split("_")[-1])
            except ValueError:
                continue
            st = f.stat()
            profiles.append(SaveProfile(slot, f, st.st_size, st.st_mtime))
    return sorted(profiles, key=lambda p: p.slot)