import configparser
from os.path import isfile

# TODO: Make copying the settings file unnecessary
# TODO: Define an schema with default values
class Settings:
    def __init__(self):
        
        self.settings: configparser.ConfigParser = configparser.ConfigParser()
        
        if not isfile("settings.ini"):
            # The file doesn't exist, so we create a default one
            self.create_default_settings()
        
        self.settings.read("settings.ini")
        
    def create_default_settings(self):
        self.settings.add_section('settings')
        self.settings.set('settings', 'dark_mode', "True")
        self.settings.set('settings', 'text_size', "12")
        
        with open("settings.ini", 'w') as file:
            self.settings.write(file)
            file.close()

    def get_options(self) -> dict:
        values = {
            'dark_mode':    self.settings.get('settings', 'dark_mode', fallback="True") == "True",
            'text_size':    int(self.settings.get('settings', 'text_size', fallback=12)),
        }
        return values
    
    def write_option(self,
                     section: str,
                     option: str,
                     value: str):
        self.settings.set(section, option, value)
        
        with open("settings.ini", 'w') as file:
            self.settings.write(file)
            file.close()
