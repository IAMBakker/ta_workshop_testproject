import unittest
from logging import getLogger
from Pages.Home import Home
from Tests.UI.UITestBase import UITestBase


class MovieListTest(UITestBase, unittest.TestCase):

    getLogger('UI Tests')

    def test_all_movies_listed_match_api_response(self):
        homepage = Home(self.browser)
        list_all_movies_button = homepage.get_list_all_movies_button()
        list_all_movies_button.click()

        movies = homepage.get_movies()

        print(movies)
        # for mov in movies:
        #     print('Key:{0}\nVal:{1}'.format(mov, movies[mov]))

    def test_the_connection_with_wd_hub(self):
        print("it works")
        self.browser.get("http://www.google.com")
        self.browser.get_screenshot_as_file('/Screenshots/google.png')
