import json
from pathlib import Path
from typing import Final

import platformdirs

type OptionType = bool | int | str

DEFAULT_SETTINGS: Final[dict[str, OptionType]] = {
    "dark_mode": True,
    "text_size": 12,
}

class Settings:
    settings_dir: Path
    filename: Path
    full_path: Path
    options: dict[str, OptionType]

    def __init__(self) -> None:
        self.settings_dir = Path(platformdirs.user_config_dir(appname="RDVSpoilerLogParser"))
        self.filename = Path("rdvslp-settings.json")
        self.options = {}

        self.full_path = self.settings_dir.joinpath(self.filename)

        if not self.full_path.exists():
            # The file doesn't exist, so we create a default one
            self.create_default_settings()

        try:
            with self.full_path.open(mode="r") as file:
                self.options = json.load(file)
        except json.JSONDecodeError:
            # The file is invalid, so we regenerate it
            self.create_default_settings()
            with self.full_path.open(mode="r") as file:
                self.options = json.load(file)
        finally:
            file.close()

    def create_default_settings(self) -> None:
        print("Creating default settings")
        self.options = DEFAULT_SETTINGS
        self.save_options_to_file()

    def get_option(self, name: str) -> OptionType:
        if name not in self.options:
            if name not in DEFAULT_SETTINGS:
                raise KeyError(f"{name} is not a valid option")
            self.options[name] = DEFAULT_SETTINGS[name]
        return self.options[name]

    def write_option(self, option: str, value: OptionType) -> None:
        self.options[option] = value

    def save_options_to_file(self) -> None:
        if not self.settings_dir.exists():
            Path.mkdir(self.settings_dir, parents=True)

        with self.full_path.open(mode="w") as file:
            json.dump(self.options, file)
            file.close()
