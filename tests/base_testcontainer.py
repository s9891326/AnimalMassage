from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from testcontainers.postgres import PostgresContainer

from animal_massage.repository.database import Base


class BasePGTestContainer(TestCase):
    container: PostgresContainer = None
    session: Session = None

    def tearDown(self) -> None:
        super().tearDown()
        if self.session and self.session.is_active:
            self.session.close()

    @classmethod
    def setUpClass(cls):
        cls.container = PostgresContainer("postgres:14").with_bind_ports(5432, 16888)
        cls.container.start()
        engine = create_engine(cls.container.get_connection_url())
        cls.session = sessionmaker(bind=engine)()
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        cls.container.stop()
