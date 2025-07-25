import json
import os
from pathlib import Path
from typing import Any

import platformdirs


# TODO: Define an schema with default values
class Settings:
    settings_dir: Path
    settings_file_path: Path
    full_path: Path
    options: dict

    def __init__(self):
        self.settings_dir = Path(platformdirs.user_config_dir(appname="RDVSpoilerLogParser"))
        self.settings_file_path = Path("rdvslp-settings.json")
        self.full_path = None
        self.options = {}

        self.full_path = self.settings_dir.joinpath(self.settings_file_path)

        if not self.full_path.exists():
            # The file doesn't exist, so we create a default one
            print("Creating default settings")
            self.create_default_settings()

        with self.full_path.open(mode="r") as file:
            self.options = json.load(file)
            file.close()

    def create_default_settings(self):
        self.options = {
            "dark_mode": True,
            "text_size": 12,
        }

        self.save_options_to_file()

    def get_options(self) -> dict:
        return self.options

    def write_option(self, option: str, value: Any):
        self.options[option] = value

    def save_options_to_file(self):
        if not os.path.isdir(self.settings_dir):
            Path.mkdir(self.settings_dir, parents=True)

        with self.full_path.open(mode="w") as file:
            json.dump(self.options, file)
            file.close()
