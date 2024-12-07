import json
import os
import platform
from pathlib import Path

# TODO: Make copying the settings file unnecessary
# TODO: Define an schema with default values
class Settings:
    def __init__(self):
        self.settings_dir: Path = None
        self.settings_filename: str = "rdvslp-settings.json"
        self.full_path: Path = None
        self.options: dict = dict()
        
        match platform.system():
            case "Windows":
                self.settings_dir = Path(f"{os.environ['LOCALAPPDATA']}/RDVSpoilerLogParser")
            case "Linux":
                self.settings_dir = Path.home().joinpath(".RDVSpoilerLogParser/")
            case "Darwin":
                self.settings_dir = Path.home().joinpath("Library/Application Support/RDVSpoilerLogParser/")
        
        self.full_path = self.settings_dir.joinpath(self.settings_filename)
        
        if not self.full_path.exists():
            # The file doesn't exist, so we create a default one
            print("Creating default settings")
            self.create_default_settings()
        
        with self.full_path.open(mode = "r") as file:
            self.options = json.load(file)
            file.close()
        
    def create_default_settings(self):
        self.options = {
            'dark_mode': True,
            'text_size': 12,
        }
        
        self.save_options_to_file()

    def get_options(self) -> dict:
        return self.options
    
    def write_option(self,
                     option: str,
                     value: str):
        self.options[option] = value
        
    def save_options_to_file(self):
        if not os.path.isdir(self.settings_dir):
            Path.mkdir(self.settings_dir)
        
        with self.full_path.open(mode = "w") as file:
            json.dump(self.options, file)
            file.close()
