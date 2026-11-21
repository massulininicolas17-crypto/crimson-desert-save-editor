# Contributing to crimson-desert-save-editor

Thanks for helping out. This is a community save editor for Crimson Desert.

## Layout

- `src/crimson_desert_host/` — plugin host, registry, loader
- `src/crimson_desert_save/` — save container reader/writer
- `src/crimson_desert_inventory/`, `src/crimson_desert_skills/` — built-in extensions
- `src/crimson_desert_ui/` — Tk desktop UI
- `src/crimson_desert_cli/` — headless CLI
- `plugins/` — `.cdse_ext` extension packages
- `tests/` — pytest suite

## Adding an extension

1. Create a module under `src/` exposing a class with `name`, `commands`, `handle`.
2. Drop a `.cdse_ext` shim in `plugins/` that imports the class.
3. Add a test under `tests/`.

## Style

- `pytest` must pass: `python -m pytest -q`
- Keep extension `commands` namespaced (`inventory.add`, `skills.unlock`).
- Back up saves before writing.