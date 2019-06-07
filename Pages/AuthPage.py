from Pages.PageBase import PageBase
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class AuthPage(PageBase):

    def _get_username_field(self):
        return self.browser.find_element_by_class_name("login__username")

    def _get_password_field(self):
        return self.browser.find_element_by_class_name("login__password")

    def _get_submit_button(self):
        return self.browser.find_element_by_class_name("login__submit")

    def _get_repeat_password_field(self):
        return self.browser.find_elements_by_class_name("login__password")[1]

    def login(self, username, password):
        self._get_username_field().send_keys(username)
        self._get_password_field().send_keys(password)
        self._get_submit_button().click()

    def sign_up(self, username, password, repeat_password=None):
        self._get_username_field().send_keys(username)
        self._get_password_field().send_keys(password)
        if repeat_password is None:
            self._get_repeat_password_field().send_keys(password)
        else:
            self._get_repeat_password_field().send_keys(repeat_password)
        self._get_submit_button().click()

    def sign_up_button_is_enabled(self):
        return self._get_submit_button().is_enabled()

    def sign_up_was_successful(self):
        success = False
        try:
            self.wait.until(expected_conditions.url_contains("signupsuccess"))
            success = True
        finally:
            return success
