from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class CertificateModel(BaseModel):
    __tablename__ = "certificate"

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int] = mapped_column(nullable=False)
    given_date: Mapped[str] = mapped_column(nullable=False)
    expire_date: Mapped[str] = mapped_column(nullable=False)
    # app_id: Mapped[int] = mapped_column(ForeignKey("app.id"))

    app = relationship("AppModel", back_populates="certificate")
