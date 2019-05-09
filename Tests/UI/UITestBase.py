from unittest import TestCase
from coloredlogs import install
from selenium.webdriver.remote.webdriver import WebDriver

from Resources.ConfigLoader import ConfigLoader


class UITestBase(TestCase):

    browser = WebDriver(ConfigLoader.get_config().get('hub')['url'], "firefox")

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
