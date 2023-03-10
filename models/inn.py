from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class INNModel(BaseModel):
    __tablename__ = "inn"

    id: Mapped[int] = mapped_column(primary_key=True)
    series: Mapped[int] = mapped_column(nullable=False)
    number: Mapped[int] = mapped_column(nullable=False)
    given_by: Mapped[str] = mapped_column(nullable=False)

    # user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user = relationship("UserModel", back_populates="INN")
