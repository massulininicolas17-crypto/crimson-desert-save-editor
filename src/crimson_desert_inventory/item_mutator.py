"""Item mutator extension module (.cdse_ext)."""
from __future__ import annotations

import json

ITEM_SECTION_ID = 0x0010


class InventoryMutator:
    name = "inventory_mutator"
    commands = ["inventory.add", "inventory.remove", "inventory.export"]

    def handle(self, payload: dict) -> dict:
        op = payload.get("op")
        if op == "add":
            return self._add(payload["item_id"], payload.get("qty", 1))
        if op == "remove":
            return self._remove(payload["item_id"], payload.get("qty", 1))
        if op == "export":
            return {"items": self._dump()}
        raise ValueError(f"unsupported inventory op: {op!r}")

    def _add(self, item_id: int, qty: int) -> dict:
        return {"ok": True, "item_id": item_id, "qty": qty, "action": "add"}

    def _remove(self, item_id: int, qty: int) -> dict:
        return {"ok": True, "item_id": item_id, "qty": qty, "action": "remove"}

    def _dump(self) -> list:
        return []