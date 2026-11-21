"""Skill tree editor extension module (.cdse_ext)."""
from __future__ import annotations

SKILL_SECTION_ID = 0x0020


class SkillTreeEditor:
    name = "skill_tree_editor"
    commands = ["skills.unlock", "skills.respec", "skills.list"]

    def handle(self, payload: dict) -> dict:
        op = payload.get("op")
        if op == "unlock":
            return self._unlock(payload["node_id"])
        if op == "respec":
            return {"ok": True, "refunded_sp": payload.get("sp", 0)}
        if op == "list":
            return {"nodes": self._nodes()}
        raise ValueError(f"unsupported skills op: {op!r}")

    def _unlock(self, node_id: str) -> dict:
        if not node_id.startswith("sk_"):
            raise ValueError(f"invalid skill node id: {node_id!r}")
        return {"ok": True, "node_id": node_id, "unlocked": True}

    def _nodes(self) -> list:
        return []