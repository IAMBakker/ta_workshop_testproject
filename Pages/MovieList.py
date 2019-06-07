from selenium.webdriver.support import expected_conditions

from Pages.PageBase import PageBase


class MovieList(PageBase):

    def _get_search_movie_input(self):
        return self.browser.find_element_by_css_selector('input.search-movie__input')

    def search_movie_input_exists(self):
        exists = False
        try:
            self._get_search_movie_input()
            exists = True
        finally:
            return exists

    def filter_movies(self, query):
        movies_before = self.browser.find_element_by_css_selector("main.movies li")
        self._get_search_movie_input().send_keys(query)
        self.wait.until(expected_conditions.staleness_of(movies_before))

    def get_movies(self) -> ():
        movie_tiles = self.browser.find_elements_by_css_selector('main.movies li')
        movies = []
        for movie_tile in movie_tiles:
            movie_dict = {}
            title = movie_tile.find_element_by_css_selector('.movie__details h3')
            description = movie_tile.find_element_by_css_selector('.movie__details p')

            imdb_key_element = movie_tile.find_element_by_css_selector('.movie__image-box a')
            imdb_key_raw = imdb_key_element.get_attribute('href')
            imdb_key = imdb_key_raw.replace(self.baseUrl, '')\
                .replace('/', '')\
                .replace('/movies', '')\
                .replace('movie', '')

            img = movie_tile.find_element_by_css_selector('.movie__image-box a img').get_attribute('src')
            movie_dict['title'] = title.text
            movie_dict['description'] = description.text
            movie_dict['image'] = img
            movie_dict['imdb'] = imdb_key
            print(movie_dict)
            movies.append(movie_dict)
        return movies
