from Pages.PageBase import PageBase


class Home(PageBase):

    def get_list_all_movies_button(self):
        buttons = self.browser.find_elements_by_css_selector('button')
        return next(button for button in buttons if (button.text == 'List all movies'))

