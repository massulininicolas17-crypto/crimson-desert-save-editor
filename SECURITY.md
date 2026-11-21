# Security Policy

## Scope

crimson-desert-save-editor only touches local save files. It never phones home.

## Reporting

Open a private security advisory on the repository. Do not file public issues
for save-corruption bugs that could wipe user data.

## Guidance

- Always back up `.cdsav` files before mutation (`~/.cdse/backups/`).
- Only load `.cdse_ext` packages from sources you trust — they execute Python.
- Use at your own risk. Corrupting a save is possible if you feed it bad payloads.