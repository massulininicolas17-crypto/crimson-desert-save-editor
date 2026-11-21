"""cdse CLI entrypoint — mirrors UI commands without a GUI."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from crimson_desert_host.host import SaveEditorHost


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cdse", description="Crimson Desert Save Editor CLI")
    p.add_argument("--plugins", default="plugins", type=Path)
    p.add_argument("--save-root", default=None, type=Path)
    sub = p.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run", help="dispatch an extension command")
    run.add_argument("command")
    run.add_argument("--payload", default="{}")
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    host = SaveEditorHost(args.save_root or Path.cwd(), args.plugins)
    host.boot()
    if args.cmd == "run":
        result = host.dispatch(args.command, json.loads(args.payload))
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())