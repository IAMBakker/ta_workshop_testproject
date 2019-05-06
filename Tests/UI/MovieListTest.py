import unittest
import xmlrunner
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

    if __name__ == "__main__":
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output='test-reports')
        )
