from unittest import TestCase
from coloredlogs import install
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.remote.webdriver import WebDriver

from Resources.ConfigLoader import ConfigLoader


class UITestBase(TestCase):

    browser = WebDriver(browser_profile=FirefoxProfile())

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
