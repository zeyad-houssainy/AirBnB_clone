#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""

import unittest
from models.base_model import add


class TestCalc(unittest.TestCase):
    """test file base_model file"""

    def test_add(self):
        """Test add function"""
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, 2), 3)


        

