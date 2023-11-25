#!/usr/bin/python3
""" This module contains the unittests for the State class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ This represents the test_state class """

    def __init__(self, *args, **kwargs):
        """ This method initializes the test_state class """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ This method tests for the state name """
        new = self.value()
        self.assertEqual(type(new.name), str)
