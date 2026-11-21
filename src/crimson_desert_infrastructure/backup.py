"""Timestamped save backups before mutation."""
from __future__ import annotations

import shutil
import time
from pathlib import Path

BACKUP_DIR = Path.home() / ".cdse" / "backups"


def backup_save(save_path: Path) -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    dest = BACKUP_DIR / f"{save_path.stem}.{stamp}.cdsav.bak"
    shutil.copy2(save_path, dest)
    return dest