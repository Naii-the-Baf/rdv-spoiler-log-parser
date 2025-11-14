import json
from copy import copy
from pathlib import Path
from typing import Final

import platformdirs

from gui.notification_dialog import NotificationDialog

type OptionType = bool | int | str

DEFAULT_SETTINGS: Final[dict[str, OptionType]] = {
    "dark_mode": True,
    "text_size": 12,
    "confirm_map_change": True,
}


class Settings:
    settings_dir: Path
    filename: Path
    full_path: Path
    options: dict[str, OptionType] = {}

    def __init__(self) -> None:
        self.settings_dir = Path(platformdirs.user_config_dir(appname="RDVSpoilerLogParser"))
        self.filename = Path("rdvslp-settings.json")

        self.full_path = self.settings_dir.joinpath(self.filename)

        if not self.full_path.exists():
            # The file doesn't exist, so we create a default one
            self.create_default_settings()
            return

        try:
            with self.full_path.open(mode="r") as file:
                Settings.options = json.load(file)
            file.close()
        except json.JSONDecodeError:
            # The file is invalid, so we replace it with defaults
            self.create_default_settings()

    def create_default_settings(self) -> None:
        print("Creating default settings")
        Settings.options = copy(DEFAULT_SETTINGS)
        self.save_options_to_file()

    def get_option(self, name: str) -> OptionType:
        if name not in Settings.options:
            if name not in DEFAULT_SETTINGS:
                raise KeyError(f"{name} is not a valid option")
            self.write_option(name, DEFAULT_SETTINGS[name])
        return Settings.options[name]

    def write_option(self, option: str, value: OptionType) -> None:
        Settings.options[option] = value

    def save_options_to_file(self) -> None:
        try:
            if not self.settings_dir.exists():
                Path.mkdir(self.settings_dir, parents=True)

            with self.full_path.open(mode="w") as file:
                json.dump(Settings.options, file)
                file.close()
        except Exception:
            NotificationDialog.show("Error", "Could not save settings")
            if "file" in locals():
                file.close()
