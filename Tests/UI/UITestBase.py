from unittest import TestCase
from coloredlogs import install
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from Resources.ConfigLoader import ConfigLoader


class UITestBase(TestCase):

    opts = Options()
    # opts.set_headless()
    # assert opts.headless
    browser = Chrome(options=opts)

    @classmethod
    def setUpClass(cls):
        install()
        url = ConfigLoader.get_config().get('web')['url']

        cls.browser.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        quit()
        print('-------------Test Finished-------------')
