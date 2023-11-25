#!/usr/bin/python3
""" This module contains unittest for the User class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ The represent the test class for the user class """

    def __init__(self, *args, **kwargs):
        """ This method initializes the test class """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ This method tests for the instance firstname """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ This method tests for the instance last name """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ This method tests for the instance email """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ This method tests for the instance password """
        new = self.value()
        self.assertEqual(type(new.password), str)
