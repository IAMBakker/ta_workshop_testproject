import yaml
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + "/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

    class ConfigLoader:

        @staticmethod
        def get_config():
            return cfg

