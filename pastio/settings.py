import os
import yaml
from .exceptions import NoSettingsFile


class Settings:
    settings_path = os.path.expanduser("~/.config/pastio/")
    options = None

    @classmethod
    def load(cls):
        file_path = os.path.join(cls.settings_path, 'settings.yaml')
        if not os.path.exists(file_path):
            os.mkdir(cls.settings_path)
            raise NoSettingsFile("There is no config file in {}".format(file_path))
        cls.options = yaml.load(open(file_path))

    @classmethod
    def dump(cls):
        pass

    @classmethod
    def get(cls, option, default_value=None):
        if not cls.options:
            cls.load()
        return cls.options.get(option, default_value)
