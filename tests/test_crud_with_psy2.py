import unittest
import warnings
from functools import wraps

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from animal_massage.models import User
from animal_massage.repository.database import Base
from animal_massage.repository.user_repository import create_user


def db_mask(func):
    @wraps(func)
    def wrapper(*args):
        with PostgresContainer("postgres:9.5") as postgres:
            engine = sqlalchemy.create_engine(postgres.get_connection_url())
            session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            Base.metadata.create_all(bind=engine)

            db = session_local()
            try:
                func(db=db, *args)
            finally:
                print("close db")
                db.close()

    return wrapper


class TestUserCRUD(unittest.TestCase):
    def setUp(self) -> None:
        # 解决ResourceWarning: Enable tracemalloc to get the object allocation traceback
        warnings.simplefilter("ignore", ResourceWarning)

    @db_mask
    def test_create_user(self, db):
        user = create_user(db, User(uid="1", name="eddy", age=18))

        self.assertEqual(user.uid, "1")
        self.assertEqual(user.name, "eddy")
        self.assertEqual(user.age, 18)
        print(user)


if __name__ == "__main__":
    unittest.main()
