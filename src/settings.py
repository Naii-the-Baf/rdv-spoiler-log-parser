import json
import os
import platformdirs
from pathlib import Path


# TODO: Define an schema with default values
class Settings:
    def __init__(self):
        self.settings_dir: Path = Path(
            platformdirs.user_config_dir(appname="RDVSpoilerLogParser")
        )
        self.settings_file_path: Path = Path("rdvslp-settings.json")
        self.full_path: Path = None
        self.options: dict = dict()

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

    def write_option(self, option: str, value: str):
        self.options[option] = value

    def save_options_to_file(self):
        if not os.path.isdir(self.settings_dir):
            Path.mkdir(self.settings_dir)

        with self.full_path.open(mode="w") as file:
            json.dump(self.options, file)
            file.close()
