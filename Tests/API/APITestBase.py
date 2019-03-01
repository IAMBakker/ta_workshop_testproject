from unittest import TestCase
from coloredlogs import install
import yaml

with open("./../../config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class APITestBase(TestCase):

    @classmethod
    def setUpClass(cls):
        install(level='DEBUG')
        cls.ApiUrl = cfg.get('movies')['url']

    @classmethod
    def tearDownClass(cls):
        print('-------------Test Finished-------------')

