from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select

from common.db import get_db
from common.controller import BaseController
from common.schemas import Drives, Drive, DriveBase, DriveUpdate
from models import DriveModel, UserModel
from drives.controller import drive_controller


router = APIRouter(prefix="/drives", tags=["Drives"])


@router.get("", response_model=Drives)
async def get_drives(limit: Optional[int] = 100, offset: Optional[int] = 0, db=Depends(get_db)):
    query = db.scalars(select(DriveModel).offset(offset).limit(limit))
    return Drives(drives=query.unique().all())


@router.get("/{user_id}", response_model=Drives)
async def get_user_drives(user_id: int, db=Depends(get_db)):
    return Drives(drives=db.get(UserModel, user_id).drives)


@router.put("", response_model=Drive)
async def create_drive(drive: DriveBase, db=Depends(get_db)):
    return BaseController._create(db, DriveModel(**drive.dict()))


@router.delete("/{drive_id}")
async def delete_drive(drive_id: int, db=Depends(get_db)):
    return BaseController._delete(db, DriveModel, drive_id)


@router.post("/{drive_id}", response_model=Drive)
async def update_drive(drive_id: int, drive: DriveUpdate, db=Depends(get_db)):
    return BaseController.patch_model(db, DriveModel, drive_id, drive)


@router.post("/user/")
async def set_to_user(drive_id: int = Query(), user_id: int = Query(), db=Depends(get_db)):
    drive_controller.set_to_user(db, drive_id, user_id)


@router.delete("/user/")
async def delete_from_user(drive_id: int = Query(), db=Depends(get_db)):
    drive_controller.delete_from_user(db, drive_id)
