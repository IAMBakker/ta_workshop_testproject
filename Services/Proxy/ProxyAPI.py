import json
import requests
from Model import User


class ProxyAPI:

    def __init__(self, url, user):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}
        self.token = self.get_token(user)
        self.headers.update({'Authorization': 'Bearer ' + self.token})

    def get_token(self, user):
        token_url = '{0}v1/proxy/tokens/'.format(self.url)
        body = user.toJSON()
        print(body)
        response = requests.post(token_url, headers=self.headers, json=body)
        print(response)
        return response.json()

    def validate_token(self):
        token_url = '{0}v1/proxy/tokens/'.format(self.url)
        return requests.get(token_url, headers=self.headers)


