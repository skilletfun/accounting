from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.base import BaseModel


class UserDriveModel(BaseModel):
    __tablename__ = "user_drive"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    drive_id: Mapped[int] = mapped_column(ForeignKey("drive.id"), unique=True)
