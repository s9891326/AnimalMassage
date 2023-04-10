from sqlalchemy.orm import Session

from animal_massage.models import User
from animal_massage.repository.database import with_session


@with_session
def create_user(user: User, session: Session):
    db_user = User(name=user.name, phone=user.phone, birthday=user.birthday)
    session.add(db_user)
    print(db_user)
    return db_user


if __name__ == "__main__":
    import datetime

    create_user(
        User(name="eddy", phone="0929-111-123", birthday=datetime.date(1997, 8, 8))
    )
