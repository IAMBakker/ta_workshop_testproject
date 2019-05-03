from unittest import TestCase
from coloredlogs import install
import yaml

with open("./../../config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class APITestBase(TestCase):

    @classmethod
    def setUpClass(cls):
        install(level='DEBUG')
        cls.MoviesUrl = cfg.get('movies')['url']
        cls.UsersUrl = cfg.get('users')['url']
        cls.ProxyUrl = cfg.get('proxy')['url']

    @classmethod
    def tearDownClass(cls):
        print('-------------Test Finished-------------')

