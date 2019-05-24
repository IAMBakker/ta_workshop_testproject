import unittest
from logging import getLogger
from Services.Proxy.ProxyAPI import ProxyAPI
from Tests.API.APITestBase import APITestBase
from Model.User import User


class ProxyAPITest(APITestBase, unittest.TestCase):

    getLogger('Proxy API')

    @classmethod
    def setup_class(cls):
        cls.admin_session = ProxyAPI(APITestBase.ProxyUrl, User(username='testadmin', password='admin', id=1))
        cls.user_session = ProxyAPI(APITestBase.ProxyUrl, User(username='testuser', password='user', id=2))

    def test_proxy_api_validate_admin_token(self):
        response = self.admin_session.validate_token()
        assert response.status_code == 200

    def test_proxy_api_validate_user_token(self):
        response = self.user_session.validate_token()
        assert response.status_code == 200

    def test_proxy_api_validate_admin_has_admin_rights(self):
        response = self.admin_session.validate_admin_token()
        assert response.status_code == 200

    def test_proxy_api_validate_user_has_no_admin_rights(self):
        response = self.user_session.validate_admin_token()
        assert response.status_code == 403

