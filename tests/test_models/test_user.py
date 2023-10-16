#!/usr/bin/python3
"""Defines unittests for models/user.py"""
import os
import models
import unittest
from datetime import datetime
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_unused_args(self):
        us = User(None)
        self.assertNotIn(None, us.__dict__.values())


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        use = User()
        first_updated_at = use.updated_at
        use.save()
        self.assertLess(first_updated_at, use.updated_at)

    def test_save_with_arg(self):
        use = User()
        with self.assertRaises(TypeError):
            use.save(None)


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        use = User()
        self.assertIn("id", use.to_dict())
        self.assertIn("created_at", use.to_dict())
        self.assertIn("updated_at", use.to_dict())
        self.assertIn("__class__", use.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        use = User()
        use_dict = use.to_dict()
        self.assertEqual(str, type(use_dict["id"]))
        self.assertEqual(str, type(use_dict["created_at"]))
        self.assertEqual(str, type(use_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        use = User()
        self.assertNotEqual(use.to_dict(), use.__dict__)


if __name__ == "__main__":
    unittest.main()
