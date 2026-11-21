"""Core plugin host for the Crimson Desert Save Editor.

Boots the extension registry, resolves the active save profile,
and dispatches commands to registered extension modules.
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import Iterable

from .registry import ExtensionRegistry
from .loader import ExtensionLoader

log = logging.getLogger("cdse.host")


class SaveEditorHost:
    def __init__(self, save_root: Path, plugins_dir: Path) -> None:
        self.save_root = save_root
        self.plugins_dir = plugins_dir
        self.registry = ExtensionRegistry()
        self.loader = ExtensionLoader(self.registry, plugins_dir)

    def boot(self, enabled: Iterable[str] | None = None) -> int:
        loaded = self.loader.discover()
        if enabled is not None:
            allowed = set(enabled)
            loaded = [m for m in loaded if m.name in allowed]
        for mod in loaded:
            self.registry.activate(mod)
        log.info("boot complete: %d extension(s) active", len(self.registry.active()))
        return len(self.registry.active())

    def dispatch(self, command: str, payload: dict) -> dict:
        ext = self.registry.resolve(command)
        if ext is None:
            raise LookupError(f"no extension handles command {command!r}")
        return ext.handle(payload)