"""Filesystem loader for extension modules (.cdse_ext packages)."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import List

from .registry import Extension


class ExtensionLoader:
    def __init__(self, registry, plugins_dir: Path) -> None:
        self.registry = registry
        self.plugins_dir = plugins_dir

    def discover(self) -> List[Extension]:
        found: List[Extension] = []
        if not self.plugins_dir.is_dir():
            return found
        for entry in sorted(self.plugins_dir.glob("*.cdse_ext")):
            mod = self._load_module(entry)
            for attr in dir(mod):
                obj = getattr(mod, attr)
                if isinstance(obj, type) and getattr(obj, "commands", None):
                    if obj.__module__ == mod.__name__:
                        found.append(obj())
        return found

    def _load_module(self, path: Path):
        name = f"cdse_ext_{path.stem.replace('.', '_')}"
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"cannot load extension: {path}")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
        return mod