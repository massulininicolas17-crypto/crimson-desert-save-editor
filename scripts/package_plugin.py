"""Bundle a Python module as a .cdse_ext extension archive."""
import sys
from pathlib import Path


def bundle(src: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{src.stem}.cdse_ext"
    dest.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return dest


if __name__ == "__main__":
    print(bundle(Path(sys.argv[1]), Path(sys.argv[2])))