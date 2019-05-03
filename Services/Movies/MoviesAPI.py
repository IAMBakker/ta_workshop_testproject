import json
import requests


class MoviesAPI:

    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}

    def get_movies(self, query=''):
        api_url = '{0}api/movies'.format(self.url)

        if not(query.__eq__('')):
            params = {'search': query}
            response = requests.get(api_url, params=params, headers=self.headers)
        else: response = requests.get(api_url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def post_movie(self, movie):
        api_url = '{0}api/movies'.format(self.url)

        body = movie.toJSON()
        print(body)
        return requests.post(api_url, headers=self.headers, json=body)

