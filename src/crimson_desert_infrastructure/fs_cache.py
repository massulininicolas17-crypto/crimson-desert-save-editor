"""On-disk cache for parsed save sections (avoids repeated CRC work)."""
from __future__ import annotations

import hashlib
import pickle
from pathlib import Path

CACHE_ROOT = Path.home() / ".cdse" / "cache"


def cache_key(path: Path) -> str:
    st = path.stat()
    raw = f"{path.resolve()}:{st.st_size}:{st.st_mtime_ns}".encode()
    return hashlib.sha256(raw).hexdigest()[:24]


def load_cached(path: Path) -> dict | None:
    key = cache_key(path)
    f = CACHE_ROOT / f"{key}.pkl"
    if not f.is_file():
        return None
    try:
        return pickle.loads(f.read_bytes())
    except Exception:
        return None


def store_cached(path: Path, data: dict) -> None:
    CACHE_ROOT.mkdir(parents=True, exist_ok=True)
    (CACHE_ROOT / f"{cache_key(path)}.pkl").write_bytes(pickle.dumps(data))