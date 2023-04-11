import datetime
from typing import Optional

from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    phone: Optional[str]
    birthday: Optional[datetime.date]


class UserResponse(BaseModel):
    id: int
    name: str
    phone: Optional[str]
    birthday: Optional[datetime.date]

    class Config:
        orm_mode = True
