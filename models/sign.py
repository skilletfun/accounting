from sqlalchemy.orm import Mapped, mapped_column

from models.base import BaseModel


class SignModel(BaseModel):
    __tablename__ = "sign"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(nullable=False)
    owner: Mapped[str] = mapped_column(nullable=False)  # relationship?
    given_date: Mapped[str] = mapped_column(nullable=False)
    given_by: Mapped[str] = mapped_column(nullable=False)
    expire_date: Mapped[str] = mapped_column(nullable=False)
