from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class DriveModel(BaseModel):
    __tablename__ = "drive"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    number: Mapped[int] = mapped_column(nullable=False)
    given_date: Mapped[str | None] = mapped_column(default=None)
    is_accepted: Mapped[bool] = mapped_column(default=False)
    is_destroyed: Mapped[bool] = mapped_column(default=False)
    destroy_date: Mapped[str | None] = mapped_column(default=None)
    destroy_document: Mapped[str | None] = mapped_column(default=None)

    user = relationship("UserModel", secondary="user_drive", back_populates="drives")
