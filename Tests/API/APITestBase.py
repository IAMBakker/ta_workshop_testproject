from unittest import TestCase
from coloredlogs import install
import yaml

with open("./../../config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class APITestBase(TestCase):

    MoviesUrl = cfg.get('movies')['url']
    UsersUrl = cfg.get('users')['url']
    ProxyUrl = cfg.get('proxy')['url']

    @classmethod
    def setUpClass(cls):
        install(level='DEBUG')

    @classmethod
    def tearDownClass(cls):
        print('-------------Test Finished-------------')

