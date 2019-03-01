from Pages.PageBase import PageBase


class Home(PageBase):

    def get_list_all_movies_button(self):
        buttons = self.browser.find_elements_by_css_selector('button')
        return next(button for button in buttons if (button.text == 'List all movies'))

    def get_movies(self) -> dict:
        movie_tiles = self.browser.find_elements_by_css_selector('main.movies li')
        movie_dict = {}
        for movie_tile in movie_tiles:
            title = movie_tile.find_element_by_css_selector('h3')
            description = movie_tile.find_element_by_css_selector('p')
            movie_dict[title.text] = description.text
        return movie_dict
