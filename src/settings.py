import json
import os
import platform
from pathlib import Path

# TODO: Make copying the settings file unnecessary
# TODO: Define an schema with default values
class Settings:
    def __init__(self):
        self.settings_path: Path = None
        self.settings_filename: str = "rdvslp-settings.json"
        self.options: dict = dict()
        
        match platform.system():
            case "Windows":
                self.settings_path = Path(f"{os.environ['LOCALAPPDATA']}\\RDVSpoilerLogParser\\")
            case "Linux":
                self.settings_path = Path.home().joinpath(".RDVSpoilerLogParser/")
            case "Darwin":
                self.settings_path = Path.home().joinpath("Library/Application Support/RDVSpoilerLogParser/")
        
        if not os.path.isfile(self.settings_filename):
            # The file doesn't exist, so we create a default one
            print("Creating default settings")
            self.create_default_settings()
        
        with open(self.settings_path.joinpath(self.settings_filename)) as file:
            self.options = json.load(file)
            file.close()
        
    def create_default_settings(self):
        self.options['dark_mode'] = True
        self.options['text_size'] = 12
        
        self.save_options_to_file()

    def get_options(self) -> dict:
        return self.options
    
    def write_option(self,
                     option: str,
                     value: str):
        self.options[option] = value
        
    def save_options_to_file(self):
        if not os.path.isdir(self.settings_path):
            Path.mkdir(self.settings_path)
        
        with open(self.settings_path.joinpath(self.settings_filename), 'w') as file:
            json.dump(self.options, file)
            file.close()
