from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class AppModel(BaseModel):
    __tablename__ = "app"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    version: Mapped[str] = mapped_column(nullable=False)
    license_number: Mapped[int] = mapped_column(nullable=False)
    license_expire_date: Mapped[str] = mapped_column(nullable=False)
    certificate_id: Mapped[int] = mapped_column(ForeignKey("certificate.id"))

    certificate = relationship("CertificateModel", back_populates="app")
