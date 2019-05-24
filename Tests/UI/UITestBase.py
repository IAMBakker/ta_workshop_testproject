from unittest import TestCase

from coloredlogs import install
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from Resources.ConfigLoader import ConfigLoader


class UITestBase(TestCase):


    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        install()
        url = ConfigLoader.get_config().get('web')['url']

        cls.browser.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        print('-------------Test Finished-------------')
