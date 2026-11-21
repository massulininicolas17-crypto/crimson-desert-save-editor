"""Convenience launcher for local development."""
from pathlib import Path
from crimson_desert_host.host import SaveEditorHost
from crimson_desert_ui.main_window import MainWindow

if __name__ == "__main__":
    host = SaveEditorHost(Path("samples"), Path("plugins"))
    host.boot()
    MainWindow(host).mainloop()