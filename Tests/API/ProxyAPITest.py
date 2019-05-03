import unittest
from logging import getLogger
from Services.Proxy.ProxyAPI import ProxyAPI
from Tests.API.APITestBase import APITestBase
from Model.User import User


class ProxyAPITest(APITestBase, unittest.TestCase):

    getLogger('Proxy API')

    def test_proxy_api_validate_admin_token(self):
        proxy_api = ProxyAPI(self.ProxyUrl, User(username='testadmin', password='admin', id=1))
        proxy_api.validate_token()

    def test_proxy_api_validate_user_token(self):
        proxy_api = ProxyAPI(self.ProxyUrl, User(username='testuser', password='user', id=2))
        proxy_api.validate_token()

    if __name__ == "__main__":
        unittest.main()
