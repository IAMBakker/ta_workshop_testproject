from unittest import TestCase
from coloredlogs import install
from Resources.ConfigLoader import ConfigLoader


class APITestBase(TestCase):
    cfg = ConfigLoader.get_config()
    MoviesUrl = cfg.get('movies')['url']
    UsersUrl = cfg.get('users')['url']
    ProxyUrl = cfg.get('proxy')['url']

    @classmethod
    def setUpClass(cls):
        install(level='DEBUG')

    @classmethod
    def tearDownClass(cls):
        print('-------------Test Finished-------------')

