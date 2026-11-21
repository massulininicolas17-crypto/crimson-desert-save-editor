# Authoring plugins

1. Put implementation under `src/crimson_desert_<your_ext>/`.
2. Add a shim `<your_ext>.cdse_ext` in `plugins/`.
3. Namespace commands: `<domain>.<verb>`.
4. Handle only your section IDs; never rewrite unrelated bytes.
5. Add a `tests/test_<your_ext>.py`.