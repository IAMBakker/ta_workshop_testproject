import unittest
from logging import getLogger

import xmlrunner

from Services.Users.UsersAPI import UsersAPI
from Tests.API.APITestBase import APITestBase
from Model.User import User


class UserAPITest(APITestBase, unittest.TestCase):

    getLogger('User API')

    def test_add_admin_user(self):
        user_api = UsersAPI(self.UsersUrl)
        response = user_api.add_user(User(username='goovert', password='test123', role='admin', active=True))
        print(response)
        assert response.status_code == 201

    if __name__ == "__main__":
        unittest.main()
