from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from animal_massage.repository.database import Base


class BasePGTestContainer(TestCase):
    container: PostgresContainer = None
    SessionLocal: sessionmaker = None

    @classmethod
    def setUpClass(cls):
        cls.container = PostgresContainer("postgres:14").with_bind_ports(5432, 16888)
        cls.container.start()
        engine = create_engine(cls.container.get_connection_url())
        cls.SessionLocal = sessionmaker(bind=engine)
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        cls.container.stop()

    def test_aa(self):
        self.assertEqual("1", "1")
