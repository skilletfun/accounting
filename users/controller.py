from sqlalchemy import select
from sqlalchemy.orm import Session

from common.controller import BaseController
from common.schemas import *
from models.user import UserModel
from users.schemas import UserCreate, UserBase
from models.passport import PassportModel
from models.inn import INNModel
from models.snils import SNILSModel
from models.drive import DriveModel


class UserController(BaseController[UserModel]):
    def create(self, db: Session, user: UserCreate) -> UserModel:
        inn = INNModel(**user.INN.dict())
        db.add(inn)
        snils = SNILSModel(**user.SNILS.dict())
        db.add(snils)
        passport = PassportModel(**user.passport.dict())
        db.add(passport)
        return self._create(
            db, obj=self.model(
                **UserBase(**user.dict()).dict(),
                INN=inn,
                SNILS=snils,
                passport=passport)
        )

    def delete(self, db: Session, user_id: int):
        obj = db.get(self.model, user_id)
        db.delete(obj)
        inn_obj = db.query(INNModel).get(obj.INN_id)
        db.delete(inn_obj)
        pass_obj = db.get(PassportModel, obj.passport_id)
        db.delete(pass_obj)
        snils_obj = db.get(SNILSModel, obj.SNILS_id)
        db.delete(snils_obj)
        db.commit()

    def get_many(self, db: Session, skip: int, limit: int):
        users_query = db.scalars(select(self.model).offset(skip).limit(limit))
        return users_query.unique().all()

    def update_user(self, db: Session, id: int, user: UserBase):
        return self.patch_model(db=db, model=self.model, id=id, values=user)

    def update_inn(self, db: Session, id: int, inn: INNBase):
        return self.patch_model(db=db, model=INNModel, id=id, values=inn)

    def update_snils(self, db: Session, id: int, snils: SNILSBase):
        return self.patch_model(db=db, model=SNILSModel, id=id, values=snils)

    def update_passport(self, db: Session, id: int, passport: PassportBase):
        return self.patch_model(db=db, model=PassportModel, id=id, values=passport)


user = UserController(UserModel)
