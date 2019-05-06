import unittest
from logging import getLogger
from Services.Movies.MoviesAPI import MoviesAPI
from Tests.API.APITestBase import APITestBase
from Model.Movie import Movie


class MovieAPITest(APITestBase, unittest.TestCase):

    getLogger('Movies API')

    def test_movies_api_all_movies(self):
        movies_api = MoviesAPI(self.MoviesUrl)
        print(movies_api.get_movies())

    def test_movies_api_search_star_wars(self):
        movies_api = MoviesAPI(self.MoviesUrl)
        movies = movies_api.get_movies('star wars')
        for movie in movies:
            print('title:{0}, year:{1}, imdb:{2}, type:{3},'
                  ' image:{4}, description:{5}'.format(movie['title'],
                                                       movie['year'],
                                                       movie['imdb'],
                                                       movie['type'],
                                                       movie['image'],
                                                       movie['description']))

    '''
    This function has not been implemented yet
    Expect a 501...
    '''
    def test_movies_api_post_new_movie(self):
        movies_api = MoviesAPI(self.MoviesUrl)
        response = movies_api.post_movie(Movie(
            imdb='tt0078446',
            title='Up in Smoke',
            type='movie',
            year=1978
        ))
        assert response.status_code == 501

    if __name__ == "__main__":
        unittest.main()
