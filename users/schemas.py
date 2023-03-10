from common.schemas.base import RWModelCamelize
from common.schemas import *


class UserBase(RWModelCamelize):
    name: str
    surname: str
    patronimic: str
    address: str


class UserCreate(UserBase):
    passport: PassportBase
    INN: INNBase
    SNILS: SNILSBase


class UserRead(UserBase):
    id: int
    drives: list[Drive]
    passport: Passport
    INN: INN
    SNILS: SNILS


class Users(RWModelCamelize):
    users: list[UserRead]
