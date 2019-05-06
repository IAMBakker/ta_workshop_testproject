from Pages.PageBase import PageBase


class Home(PageBase):

    def get_list_all_movies_button(self):
        buttons = self.browser.find_elements_by_css_selector('button')
        return next(button for button in buttons if (button.text == 'List all movies'))

    def get_movies(self) -> ():
        movie_tiles = self.browser.find_elements_by_css_selector('main.movies li')
        movies = []
        for movie_tile in movie_tiles:
            movie_dict = {}
            title = movie_tile.find_element_by_css_selector('.movie__details h3')
            description = movie_tile.find_element_by_css_selector('.movie__details p')

            imdb_key_element = movie_tile.find_element_by_css_selector('.movie__image-box a')
            imdb_key_raw = imdb_key_element.get_attribute('href')
            imdb_key = imdb_key_raw.replace('/', '').replace('/movies', '')

            img = movie_tile.find_element_by_css_selector('.movie__image-box a img').get_attribute('src')
            movie_dict['title'] = title.text
            movie_dict['description'] = description.text
            movie_dict['image'] = img
            movie_dict['imdb'] = imdb_key
            print(movie_dict)
            movies.append(movie_dict)
        return movies
