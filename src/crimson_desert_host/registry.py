"""Extension registry mapping command verbs to extension modules."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Protocol, runtime_checkable


@runtime_checkable
class Extension(Protocol):
    name: str
    commands: List[str]
    def handle(self, payload: dict) -> dict: ...


@dataclass
class RegisteredExtension:
    name: str
    commands: List[str]
    module: object
    meta: Dict[str, str] = field(default_factory=dict)


class ExtensionRegistry:
    def __init__(self) -> None:
        self._by_command: Dict[str, RegisteredExtension] = {}
        self._active: List[RegisteredExtension] = []

    def activate(self, ext: Extension) -> None:
        record = RegisteredExtension(
            name=getattr(ext, "name", ext.__class__.__name__),
            commands=list(getattr(ext, "commands", [])),
            module=ext,
            meta={"origin": ext.__class__.__module__},
        )
        for verb in record.commands:
            if verb in self._by_command:
                raise RuntimeError(f"command collision: {verb!r}")
            self._by_command[verb] = record
        self._active.append(record)

    def resolve(self, command: str) -> RegisteredExtension | None:
        return self._by_command.get(command)

    def active(self) -> List[RegisteredExtension]:
        return list(self._active)