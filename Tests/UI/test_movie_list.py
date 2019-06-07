import time
from logging import getLogger

from selenium.webdriver.support.wait import WebDriverWait

from Databases.User.UserDB import UserDB
from Model.User import User
from Pages.AuthPage import AuthPage
from Pages.Home import Home
from Pages.MovieList import MovieList
from Resources.ConfigLoader import ConfigLoader
from Services.Movies.MoviesAPI import MoviesAPI
from Tests.UI.UITestBase import UITestBase
from delayed_assert import expect, assert_expectations


class MovieListTest(UITestBase):

    getLogger('UI Tests')

    def test_all_movies_listed_match_api_response(self):
        """arrange"""
        homepage = Home(self.browser)
        list_all_movies_button = homepage.get_list_all_movies_button()
        list_all_movies_button.click()
        movie_list_page = MovieList(self.browser)

        """act"""
        movies = movie_list_page.get_movies()
        api_movies = MoviesAPI(ConfigLoader.get_config().get('movies')['url']).get_movies()

        """assert"""
        self._assert_movie_lists_match(movies, api_movies)

    def test_login_as_admin(self):
        """arrange"""
        homepage = Home(self.browser)
        homepage.get_log_in_button().click()
        login_page = AuthPage(self.browser)

        """act"""
        login_page.login('testadmin', 'admin')
        login_page.wait_until_logged_in_successfully()

        """assert"""
        assert homepage.get_header_title_text() == 'All Movies'

    def test_login_as_user(self):
        """arrange"""
        homepage = Home(self.browser)
        homepage.get_log_in_button().click()
        login_page = AuthPage(self.browser)

        """act"""
        login_page.login('testuser', 'user')
        login_page.wait_until_logged_in_successfully()

        """assert"""
        assert homepage.get_header_title_text() == 'All Movies'

    def test_sign_up_as_new_user(self):
        """arrange"""
        to_be_added_user = User(username="Zoetekouw2", password='SalmiakLolly123', role='user', active=True)

        homepage = Home(self.browser)
        homepage.get_sign_up_button().click()
        sign_up_page = AuthPage(self.browser)

        """act"""
        sign_up_page.sign_up(to_be_added_user.username, to_be_added_user.password)

        """assert"""
        assert sign_up_page.sign_up_was_successful()
        users = UserDB().query_users()
        added_user = (user for user in users if user['username'] == to_be_added_user.username
                      and user['role'] == to_be_added_user.role
                      and user['active'] == to_be_added_user.active)
        assert added_user is not None

    def test_movie_filter_functionality(self):
        """arrange"""
        homepage = Home(self.browser)
        homepage.get_log_in_button().click()
        login_page = AuthPage(self.browser)
        login_page.login('testuser', 'user')
        login_page.wait_until_logged_in_successfully()
        assert homepage.get_header_title_text() == 'All Movies'

        """act"""
        movie_list_page = MovieList(self.browser)
        movie_list_page.filter_movies('star')
        api_movies = MoviesAPI(ConfigLoader.get_config().get('movies')['url']).get_movies('star')
        movies = movie_list_page.get_movies()

        """assert"""
        self._assert_movie_lists_match(movies, api_movies)

    def _assert_movie_lists_match(self, movies, api_movies):
        assert len(api_movies) == len(movies)

        iter_api_movies = iter(api_movies)

        for movie in movies:
            api_movie = next(iter_api_movies)
            items = ('title', 'description', 'imdb')
            for item in items:
                expect(movie[item] == api_movie[item], msg=f"{item}: {movie[item]} != {api_movie[item]}")
            if api_movie['image'] == '':
                expect(movie['image'] == f'{self.url}static/img/no-poster.ccba1b0.png',
                       msg='expect this static image to be shown if no image was found')
            else:
                expect(movie['image'] == api_movie['image'], msg=f"image: {movie['image']} != {api_movie['image']}")

        assert_expectations()
