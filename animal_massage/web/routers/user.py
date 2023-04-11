from typing import Union

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from animal_massage.dto import UserRequest, UserResponse
from animal_massage.repository.database import get_db

# isort: off
from animal_massage.repository.user_repository import (
    create_user,
    find_one_user,
    update_user,
)

# isort: on

router = APIRouter()


@router.get("", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return find_one_user(user_id, session=db)


@router.post("")
async def post_user(user: UserRequest, db: Session = Depends(get_db)):
    create_data = user.dict(exclude_unset=True)

    try:
        return create_user(create_data, session=db)
    except ValueError as err:
        return HTTPException(status_code=404, detail=err.args[0])


@router.patch("/{user_id}", response_model=UserResponse)
async def patch_user(user_id: int, user: UserRequest, db: Session = Depends(get_db)):
    user_query = find_one_user(user_id, session=db)

    if not user_query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No user with this id: {user_id}",
        )

    update_data = user.dict(exclude_unset=True)
    update_user(user_id, update_data, session=db)
    db.refresh(user_query)
    return user_query
