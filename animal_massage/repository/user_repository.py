from typing import Optional

from sqlalchemy.orm import Session

from animal_massage.models import User
from animal_massage.repository.database import with_session


@with_session
def create_user(user_data: dict, session: Session) -> Optional["User"]:
    db_user = User(**user_data)
    session.add(db_user)
    session.flush()
    return db_user


@with_session
def find_one_user(user_id: int, session: Session) -> Optional["User"]:
    return session.query(User).filter(User.id == user_id).first()


@with_session
def update_user(user_id: int, user_data: dict, session: Session):
    session.query(User).filter(User.id == user_id).update(
        user_data, synchronize_session=False
    )
