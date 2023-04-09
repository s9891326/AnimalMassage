from functools import wraps

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from animal_massage import config

eng = create_engine(
    f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@"
    f"{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    pool_size=20,
    max_overflow=0,
    pool_pre_ping=True,
)
autocommit_engine = eng.execution_options(isolation_level="AUTOCOMMIT")
SessionLocal = sessionmaker(bind=autocommit_engine)
Base = declarative_base()
Base.metadata.create_all(bind=eng)


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
