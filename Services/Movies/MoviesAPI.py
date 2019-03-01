import json
import requests


class MoviesAPI:

    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}

    def get_movies(self):
        api_url = '{0}api/movies'.format(self.url)

        response = requests.get(api_url, self.headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None


