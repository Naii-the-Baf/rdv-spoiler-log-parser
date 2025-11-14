import sys
from pathlib import Path


def get_datas_path() -> Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(getattr(sys, "_MEIPASS"))
    else:
        return Path(__file__).parent


def get_assets_path() -> Path:
    return get_datas_path().joinpath("assets")
