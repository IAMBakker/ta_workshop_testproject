import unittest
from logging import getLogger
from Services.Users.UsersAPI import UsersAPI
from Tests.API.APITestBase import APITestBase
from Model.BackendUser import User


class UserAPITest(APITestBase, unittest.TestCase):

    getLogger('User API')

    def test_add_admin_user(self):
        user_api = UsersAPI(self.UsersUrl)
        response = user_api.add_user(User(username='diederik', password='test123', role='admin', active=True))
        print(response)
        assert response.status_code == 200

    if __name__ == "__main__":
        unittest.main()
