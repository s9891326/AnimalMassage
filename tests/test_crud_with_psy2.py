import datetime
import unittest

from animal_massage.models import Blog, User

# isort: off
from animal_massage.repository.blog_repository import (
    create_blog,
    find_one_blog,
    update_blog,
    find_more_blog,
    delete_blog,
)
from animal_massage.repository.user_repository import (
    create_user,
    find_one_user,
    update_user,
)

# isort: on

from tests.base_testcontainer import BasePGTestContainer


class TestCRUD(BasePGTestContainer):
    user_id: int = 1
    name: str = "eddy"
    phone: str = "0911-111-111"
    birthday: datetime.date = datetime.date(1977, 1, 1)

    blog_id: int = 1
    title: str = "寵物華爾滋"
    sub_title: str = "什麼是寵物按摩?"
    content: str = "xxxx"

    def test_1_create_user(self):
        user = create_user(
            User(name=self.name, phone=self.phone, birthday=self.birthday),
            session=self.session,
        )
        self.session.commit()
        self.assert_user(user, self.user_id, self.name, self.phone, self.birthday)

    def test_2_select_user(self):
        user = find_one_user(self.user_id, session=self.session)
        self.assert_user(user, self.user_id, self.name, self.phone, self.birthday)

    def test_3_update_user(self):
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

    def test_4_create_blog(self):
        blog = create_blog(
            Blog(
                title=self.title,
                sub_title=self.sub_title,
                content=self.content,
                user_id=self.user_id,
            ),
            session=self.session,
        )
        self.session.commit()
        self.assert_blog(
            blog, self.blog_id, self.title, self.sub_title, self.content, self.user_id
        )

    def test_5_select_blog(self):
        blog = find_one_blog(self.blog_id, session=self.session)
        self.assert_blog(
            blog, self.blog_id, self.title, self.sub_title, self.content, self.user_id
        )

    def test_6_update_user(self):
        _title = "222"
        _sub_title = "22222"
        _content = "77777"
        update_blog(
            blog_id=self.blog_id,
            blog=Blog(title=_title, sub_title=_sub_title, content=_content),
            session=self.session,
        )
        blog = find_one_blog(self.blog_id, session=self.session)
        self.assert_blog(blog, self.blog_id, _title, _sub_title, _content, self.user_id)

    def test_7_find_all_blog(self):
        create_blog(
            Blog(
                title=self.title,
                sub_title=self.sub_title,
                content=self.content,
                user_id=self.user_id,
            ),
            session=self.session,
        )
        all_blog = find_more_blog(session=self.session)
        self.assertEqual(len(all_blog), 2)

    def test_8_delete_blog(self):
        blog = find_one_blog(self.blog_id, session=self.session)
        self.assertTrue(blog)
        delete_blog(blog_id=self.blog_id, session=self.session)
        blog = find_one_blog(self.blog_id, session=self.session)
        self.assertIsNone(blog)

    def assert_blog(
        self,
        blog: Blog,
        blog_id: int,
        title: str,
        sub_title: str,
        content: str,
        user_id: int,
    ):
        self.assertEqual(blog.id, blog_id)
        self.assertEqual(blog.title, title)
        self.assertEqual(blog.sub_title, sub_title)
        self.assertEqual(blog.content, content)
        self.assertEqual(blog.user_id, user_id)


if __name__ == "__main__":
    unittest.main()
