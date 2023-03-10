from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    patronimic: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    passport_id: Mapped[int] = mapped_column(ForeignKey("passport.id"))
    INN_id: Mapped[int] = mapped_column(ForeignKey("inn.id"))
    SNILS_id: Mapped[int] = mapped_column(ForeignKey("snils.id"))

    drives = relationship("DriveModel", secondary="user_drive", back_populates="user")
    INN = relationship("INNModel", back_populates="user")
    SNILS = relationship("SNILSModel", back_populates="user")
    passport = relationship("PassportModel", back_populates="user")
