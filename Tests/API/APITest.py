import unittest
from logging import getLogger
from Services.Movies.MoviesAPI import MoviesAPI
from Tests.API.APITestBase import APITestBase


class APITest(APITestBase, unittest.TestCase):

    getLogger('Movies API')

    def test_movies_api_responses(self):
        movies_api = MoviesAPI(self.ApiUrl)
        print(movies_api.get_movies())
        # movies = movies_api.get_movies()

    def test_movies_api_responses_as_obj(self):
        movies_api = MoviesAPI(self.ApiUrl)
        movies = movies_api.get_movies()
        for movie in movies:
            print('title:{0}, year:{1}, imdb:{2}, type:{3},'
                  ' image:{4}, description:{5}'.format(movie['title'],
                                                       movie['year'],
                                                       movie['imdb'],
                                                       movie['type'],
                                                       movie['image'],
                                                       movie['description']))

    if __name__ == "__main__":
        unittest.main()
