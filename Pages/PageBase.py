from selenium.webdriver.common.by import By
from selenium.webdriver.support.event_firing_webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Resources.ConfigLoader import ConfigLoader


class PageBase:

    sign_out_selector = (By.CSS_SELECTOR, ".header-menu__item a[href='/logout']")

    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.baseUrl = ConfigLoader.get_config().get('web')['url']
        self.wait = WebDriverWait(self.browser, timeout=25)

    def get_sign_up_button(self):
        return self.browser.find_element_by_css_selector("a[href='/signup']")

    def get_log_in_button(self):
        return self.browser.find_element_by_css_selector("a[href='/login']")

    def get_header_title_text(self):
        return self.browser.find_element_by_class_name("header__title").text

    def get_header_home_button(self):
        return self.browser.find_element_by_class_name("header__logo")

    def get_sign_out_button(self):
        return self.browser.find_element(self.sign_out_selector)

    def wait_until_logged_in_successfully(self):
        self.wait.until(expected_conditions.url_changes)
        self.wait.until(expected_conditions.presence_of_element_located(self.sign_out_selector))
