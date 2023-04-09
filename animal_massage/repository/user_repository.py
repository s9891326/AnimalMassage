from animal_massage.models import User
from animal_massage.repository.database import with_session


@with_session
def create_user(db, user):
    db_user = User(uid=user.uid, name=user.name, age=user.age)
    db.add(db_user)
    return db_user


if __name__ == "__main__":
    create_user(User(uid="1", name="eddy", age=18))
