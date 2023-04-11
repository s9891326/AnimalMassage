import datetime
import re

import sqlalchemy as db
from sqlalchemy import func
from sqlalchemy.orm import relationship, validates

from animal_massage.repository.database import Base

# 報表
# name
# 類型(動物、花精、靈氣)
# 哪張圖片
# 哪個部位
# color
# content

PHONE_REGEX = r"\d{4}-\d{3}-\d{3}"


class Blog(Base):
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    sub_title = db.Column(db.String)
    content = db.Column(db.String)
    create_time = db.Column(db.DateTime, server_default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # image_url

    def __repr__(self):
        return f"Blog id={self.id}, {self.title}, {self.user_id}, {self.create_time}>"


class User(Base):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(16))
    birthday = db.Column(db.Date)
    blog = relationship("Blog", backref="user", lazy="dynamic")

    def __init__(self, name: str, phone: str, birthday: datetime.date):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    @validates("phone")
    def validate_phone(self, _, phone):
        phone_number = re.match(PHONE_REGEX, phone)
        if phone_number:
            return phone_number.group()
        raise ValueError(f"Phone number regex error is not {PHONE_REGEX}")

    def __str__(self):
        return f"User id: {self.id}, name: {self.name}, phone: {self.phone}"


# 創建table
# if __name__ == '__main__':
#     from animal_massage.repository.database import eng
#     print(Base.metadata.tables.values())
#     Base.metadata.create_all(bind=eng)
