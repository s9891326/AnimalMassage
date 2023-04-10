from typing import Optional

from sqlalchemy.orm import Session

from animal_massage.models import Blog
from animal_massage.repository.database import with_session


@with_session
def create_blog(blog: "Blog", session: Session) -> Optional["Blog"]:
    db_blog = Blog(
        title=blog.title, sub_title=blog.sub_title, content=blog.content, user=blog.user
    )
    session.add(db_blog)
    return db_blog
