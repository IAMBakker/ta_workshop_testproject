import json
import requests
from Model.BackendUser import User


class UsersAPI:

    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json', 'accept': 'application/json'}

    def add_user(self, user):
        url = '{0}api/Users'.format(self.url)

        body = user.toJSON()
        print(body)

        response = requests.post(url, headers=self.headers, data=body)
        return response

