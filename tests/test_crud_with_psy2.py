import datetime
import unittest

from animal_massage.models import User
from animal_massage.repository.user_repository import create_user
from tests.base_testcontainer import BasePGTestContainer


class TestUserCRUD(BasePGTestContainer):
    def test_create_user(self):
        name = "eddy"
        phone = "0911-111-111"
        birthday = datetime.date(1977, 1, 1)
        user = create_user(
            User(name=name, phone=phone, birthday=birthday), session=self.session
        )

        self.assertEqual(user.name, name)
        self.assertEqual(user.phone, phone)
        self.assertEqual(user.birthday, birthday)


# class TestBlogCRUD(BasePGTestContainer):
#     def test_create_blog(self):
#         pass

if __name__ == "__main__":
    unittest.main()
