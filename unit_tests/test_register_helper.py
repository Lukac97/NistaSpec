import unittest
from unittest.mock import MagicMock, patch

from python_projekat.register_helper import fct_get_user_by_name, \
    fct_create_new_user
from python_projekat.user_model import User


class TestRegisterHelper(unittest.TestCase):

    def test_get_user_by_name(self):
        obj_return_value = MagicMock(str_username="TestUserName")

        obj_db = MagicMock(
            mtd_get_user_by_name=MagicMock(return_value=obj_return_value)
        )
        self.assertEqual(fct_get_user_by_name(obj_db, ""),
                         obj_return_value)

    @patch("python_projekat.register_helper.User")
    def test_create_new_user(self, clsUser):
        clsUser.return_value = MagicMock(
            spec=User, str_username="TestUserName")

        obj_db = MagicMock(
            mtd_add_new_user=MagicMock()
        )

        obj_return = fct_create_new_user(obj_db, "")

        self.assertIsNotNone(obj_return)
        self.assertEqual(obj_return.str_username, "TestUserName")



if __name__ == '__main__':
    unittest.main()
