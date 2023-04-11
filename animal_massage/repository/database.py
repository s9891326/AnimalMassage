from functools import wraps

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy_utils import create_database, database_exists

from animal_massage import config

eng = create_engine(
    f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@"
    f"{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    pool_size=20,
    max_overflow=0,
    pool_pre_ping=True,
)

# 自動create database
if not database_exists(eng.url):
    create_database(eng.url)

autocommit_engine = eng.execution_options(isolation_level="AUTOCOMMIT")
Session = sessionmaker(bind=autocommit_engine)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def with_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = None
        for arg in args:
            if isinstance(arg, sqlalchemy.orm.Session):
                session = arg
        if "session" not in kwargs and session is None:
            session = Session()
            kwargs["session"] = session
            try:
                result = func(*args, **kwargs)
                session.commit()
                return result
            except Exception:
                session.rollback()
                raise
            finally:
                session.close()
        else:
            return func(*args, **kwargs)

    return wrapper
