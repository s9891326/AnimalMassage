import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy.orm import relationship

from animal_massage.repository.database import Base

# 部落格
# image_url
# author

# 報表
# name
# 類型(動物、花精、靈氣)
# 哪張圖片
# 哪個部位
# color
# content


class Blog(Base):
    __tablename__ = "blog"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    title = sa.Column(sa.String)
    sub_title = sa.Column(sa.String)
    content = sa.Column(sa.String)
    create_time = sa.Column(sa.DateTime, server_default=func.now())
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"))
    user = relationship("User", lazy="joined", foreign_keys=[user_id])
    # image_url

    def __repr__(self):
        return f"Blog id={self.id}, {self.user_id}, {self.create_time}>"


class User(Base):
    __tablename__ = "user"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String(100))
    age = sa.Column(sa.Integer)

    def __str__(self):
        return f"User uid: {self.uid}, name: {self.name}, age: {self.age}"


# 創建table
# if __name__ == '__main__':
#     from animal_massage.repository.database import eng
#     print(Base.metadata.tables.values())
#     Base.metadata.create_all(bind=eng)
