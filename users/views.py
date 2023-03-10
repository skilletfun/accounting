from typing import Optional

from fastapi import APIRouter, Depends

from common.db import get_db
from users.controller import user as user_controller
from users.schemas import Users, UserCreate, UserRead, UserBase
from common.schemas import *


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=Users)
async def get_users(limit: Optional[int] = 100, offset: Optional[int] = 0, db=Depends(get_db)):
    users = user_controller.get_many(db=db, skip=offset, limit=limit)
    return Users(users=users)


@router.put("", response_model=UserRead)
async def create_user(user: UserCreate, db=Depends(get_db)):
    return user_controller.create(db=db, user=user)


@router.delete("/{user_id}")
async def delete_user(user_id: int, db=Depends(get_db)):
    return user_controller.delete(db=db, user_id=user_id)


@router.post("/{user_id}")
async def update_user(user_id: int, user: UserBase, db=Depends(get_db)):
    return user_controller.update_user(db=db, id=user_id, user=user)


@router.post("/inn/{inn_id}", response_model=INN)
async def update_inn(inn_id: int, inn: INNBase, db=Depends(get_db)):
    return user_controller.update_inn(db=db, id=inn_id, inn=inn)


@router.post("/snils/{snils_id}", response_model=SNILS)
async def update_snils(snils_id: int, snils: SNILSBase, db=Depends(get_db)):
    return user_controller.update_snils(db=db, id=snils_id, snils=snils)


@router.post("/passport/{passport_id}", response_model=Passport)
async def update_passport(passport_id: int, passport: PassportBase, db=Depends(get_db)):
    return user_controller.update_passport(db=db, id=passport_id, passport=passport)


@router.post("/drive")
async def add_drive(drive_id: int, user_id: int, db=Depends(get_db)):
    return user_controller.add_drive(db, drive_id, user_id)


@router.delete("/drive")
async def add_drive(drive_id: int, user_id: int, db=Depends(get_db)):
    return user_controller.delete_drive(db, drive_id, user_id)
