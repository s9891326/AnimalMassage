import datetime
import unittest

from animal_massage.models import User

# isort: off
from animal_massage.repository.user_repository import (
    create_user,
    find_one_user,
    update_user,
)

# isort: on

from tests.base_testcontainer import BasePGTestContainer


class TestUserCRUD(BasePGTestContainer):
    user_id: int = 1
    name: str = "eddy"
    phone: str = "0911-111-111"
    birthday: datetime.date = datetime.date(1977, 1, 1)

    def test_create_user(self):
        user = create_user(
            User(name=self.name, phone=self.phone, birthday=self.birthday),
            session=self.session,
        )
        self.session.commit()
        self.assert_user(user, self.user_id, self.name, self.phone, self.birthday)

    def test_select_user(self):
        user = find_one_user(self.user_id, session=self.session)
        self.assert_user(user, self.user_id, self.name, self.phone, self.birthday)

    def test_update_user(self):
        _name = "eddy2"
        _phone = "0911-111-222"
        _birthday = datetime.date(1999, 1, 1)
        update_user(
            user_id=self.user_id,
            user=User(name=_name, phone=_phone, birthday=_birthday),
            session=self.session,
        )
        user = find_one_user(self.user_id, session=self.session)
        self.assert_user(user, self.user_id, _name, _phone, _birthday)

    def assert_user(
        self, user: User, user_id: int, name: str, phone: str, birthday: datetime.date
    ):
        self.assertEqual(user.id, user_id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.phone, phone)
        self.assertEqual(user.birthday, birthday)


# class TestBlogCRUD(BasePGTestContainer):
#     def test_create_blog(self):
#         pass

if __name__ == "__main__":
    unittest.main()
