from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class OrganizationModel(BaseModel):
    __tablename__ = "organization"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    INN: Mapped[int] = mapped_column(nullable=False)
    OGRN: Mapped[int] = mapped_column(nullable=False)
    address: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(nullable=False)
    license_id: Mapped[int] = mapped_column(ForeignKey("license.id"))

    license = relationship("LicenseModel", back_populates="organization")
