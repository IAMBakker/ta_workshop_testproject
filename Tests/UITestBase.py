from unittest import TestCase
from coloredlogs import install
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import yaml

with open("./../config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)


class UITestBase(TestCase):

    opts = Options()
    opts.set_headless()
    assert opts.headless
    browser = Firefox(options=opts)

    @classmethod
    def setUpClass(cls):
        install()
        cls.UiUrl = cfg.get('web')['url']

        cls.browser.get('http://127.0.0.1')

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        quit()
        print('-------------Test Finished-------------')
