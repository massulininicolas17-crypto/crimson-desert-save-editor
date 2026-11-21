"""Known item preset IDs collected by the community."""
PRESETS = {
    "abyss_gear": [40112, 40113, 40114],
    "crimson_ore": [50901],
    "mount_rations": [60011, 60012],
}


def resolve_preset(name: str) -> list[int]:
    return PRESETS.get(name, [])