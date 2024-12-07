import configparser
from os.path import isfile

# TODO: Make copying the settings file unnecessary
# TODO: Define an schema with default values
class Settings:
    def __init__(self):
        self.settings_filename = "rdvslp-settings.ini"
        self.settings: configparser.ConfigParser = configparser.ConfigParser()
        
        if not isfile(self.settings_filename):
            # The file doesn't exist, so we create a default one
            self.create_default_settings()
        
        self.settings.read(self.settings_filename)
        
    def create_default_settings(self):
        self.settings.add_section('settings')
        self.settings.set('settings', 'dark_mode', "True")
        self.settings.set('settings', 'text_size', "12")
        
        self.save_options_to_file(self)

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
        
    def save_options_to_file(self):
        with open(self.settings_filename, 'w') as file:
            self.settings.write(file)
            file.close()
