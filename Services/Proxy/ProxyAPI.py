import json
import requests


class ProxyAPI:

    def __init__(self, url, user):
        self.url = url
        self.headers = {'Content-Type': 'application/json'}
        self.token = self.get_token(user)
        self.headers.update({'Authorization': 'Bearer ' + self.token})

    def get_token(self, user):
        token_url = '{0}v1/proxy/tokens/'.format(self.url)
        body = user.toJSON()
        response = requests.post(token_url, headers=self.headers, data=body)
        token = json.loads(response.content.decode('utf-8'))['access_token']
        return token

    def validate_token(self):
        token_url = '{0}v1/proxy/tokens/'.format(self.url)
        response = requests.get(token_url, headers=self.headers)
        print(response.content.decode('utf-8'))
        return response

    def validate_admin_token(self):
        token_url = '{0}v1/proxy/tokens/admin'.format(self.url)
        response = requests.get(token_url, headers=self.headers)
        print(response.content.decode('utf-8'))
        return response

