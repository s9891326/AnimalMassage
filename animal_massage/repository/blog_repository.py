from typing import Optional

from sqlalchemy.orm import Session

from animal_massage.models import Blog
from animal_massage.repository.database import with_session


@with_session
def create_blog(blog: "Blog", session: Session) -> Optional["Blog"]:
    db_blog = Blog(
        title=blog.title,
        sub_title=blog.sub_title,
        content=blog.content,
        user_id=blog.user_id,
    )
    session.add(db_blog)
    return db_blog


@with_session
def find_one_blog(blog_id: int, session: Session) -> Optional["Blog"]:
    return session.query(Blog).filter(Blog.id == blog_id).first()


@with_session
def find_more_blog(
    session: Session, offset: int = 0, limit: int = 100
) -> Optional["Blog"]:
    return session.query(Blog).limit(limit).offset(offset).all()


@with_session
def update_blog(blog_id: int, blog: "Blog", session: Session):
    session.query(Blog).filter(Blog.id == blog_id).update(
        {
            Blog.title: blog.title,
            Blog.sub_title: blog.sub_title,
            Blog.content: blog.content,
        }
    )


@with_session
def delete_blog(blog_id: int, session: Session):
    session.query(Blog).filter(Blog.id == blog_id).delete()


# if __name__ == '__main__':
#     # from animal_massage.repository.user_repository import find_one_user
#     from animal_massage.repository.database import Session as se
#     session = se()
#     # user = find_one_user(user_id=1, session=session)
#     # print(user)
#     _blog = create_blog(Blog(title="aa3", sub_title="bb", content="xx", user_id=1), session=session)
#     print(_blog.user)
