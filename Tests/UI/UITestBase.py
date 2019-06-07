import unittest

import pytest
from coloredlogs import install
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import WebDriver

from Resources.ConfigLoader import ConfigLoader


class UITestBase(unittest.TestCase):

    url = ConfigLoader.get_config().get('web')['url']

    @classmethod
    def setUpClass(cls):
        cls.browser = WebDriver()
        # cls.browser = webdriver.Remote(
        #     command_executor=f"{ConfigLoader.get_config().get('webdriver')['url']}/wd/hub",
        #     desired_capabilities=DesiredCapabilities.FIREFOX.copy())
        install()
        """Required step. Even though we repeat it in the setUp()"""
        cls.browser.get(cls.url)

    def setUp(self):
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.delete_all_cookies()
        self.browser.get(self.url)

    @classmethod
    def tearDownClass(cls):
        # cls.browser.close()
        print('-------------Test Finished-------------')
