from sqlalchemy import func

from animal_massage.repository.database import Base

import sqlalchemy as db


class Blog(Base):
    __tablename__ = "blog"

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    sub_title = db.Column(db.String)
    content = db.Column(db.String)
    create_time = db.Column(db.DateTime, server_default=func.now())

    # image_url
    # author = db.Column(db.String)

    def __repr__(self):
        return f"GoodInfo<{self.id=}, {self.name=}, {self.price=}, {self.stock_state=}>"


class User(Base):
    __tablename__ = "users"

    uid = db.Column(db.String(100), primary_key=True, unique=True, index=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __str__(self):
        return f"User uid: {self.uid}, name: {self.name}, age: {self.age}"
