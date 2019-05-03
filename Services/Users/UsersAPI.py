import requests


class UsersAPI:

    def __init__(self, url):
        self.url = url
        self.headers = {'Content-Type': 'application/json', 'accept': 'application/json'}

    def add_user(self, user):
        url = '{0}api/Users'.format(self.url)
        body = user.toJSON()
        response = requests.post(url, headers=self.headers, data=body)
        print(response.content.decode('utf-8'))
        return response

