import unittest
from logging import getLogger

from Databases.User.UserDB import UserDB
from Services.Users.UsersAPI import UsersAPI
from Tests.API.APITestBase import APITestBase
from Model.User import User


class UserAPITest(APITestBase, unittest.TestCase):

    getLogger('User API')

    @classmethod
    def setup_class(cls):
        cls.db = UserDB()
        cls.user_api = UsersAPI(APITestBase.UsersUrl)

    def test_add_admin_user(self):
        to_be_added_user = User(username="piet_piraat4", password='test123', role='admin', active=True)
        response = self.user_api.add_user(to_be_added_user)
        assert response.status_code == 201
        users = self.db.query_users()
        added_user = (user for user in users if user['username'] == to_be_added_user.username
                      and user['role'] == to_be_added_user.role
                      and user['active'] == to_be_added_user.active)
        print(added_user)
        assert added_user is not None

    def test_add_user(self):
        to_be_added_user = User(username='jan_de_wannabe_admin', password='test456', role='user', active=True)
        response = self.user_api.add_user(to_be_added_user)
        assert response.status_code == 201
        users = self.db.query_users()
        added_user = (user for user in users if user['username'] == to_be_added_user.username
                      and user['role'] == to_be_added_user.role
                      and user['active'] == to_be_added_user.active)
        print(added_user)
        assert added_user is not None
