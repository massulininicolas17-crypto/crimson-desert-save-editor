"""Main Tk window wiring the host, save picker and extension tabs."""
from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from crimson_desert_host.host import SaveEditorHost
from crimson_desert_save.profiles import scan_profiles


class MainWindow(tk.Tk):
    def __init__(self, host: SaveEditorHost) -> None:
        super().__init__()
        self.host = host
        self.title("Crimson Desert Save Editor")
        self.geometry("920x600")
        self._build()

    def _build(self) -> None:
        bar = tk.Frame(self)
        bar.pack(fill="x", padx=8, pady=6)
        tk.Button(bar, text="Open Save…", command=self._pick_save).pack(side="left")
        tk.Button(bar, text="Scan Profiles", command=self._scan).pack(side="left", padx=4)
        self.log = tk.Text(self, height=20)
        self.log.pack(fill="both", expand=True, padx=8, pady=6)

    def _pick_save(self) -> None:
        path = filedialog.askopenfilename(filetypes=[("Crimson Desert save", "*.cdsav")])
        if path:
            self._write(f"selected: {path}")

    def _scan(self) -> None:
        for p in scan_profiles():
            self._write(f"slot {p.slot}: {p.path.name} ({p.size} bytes)")

    def _write(self, msg: str) -> None:
        self.log.insert("end", msg + "\n")
        self.log.see("end")