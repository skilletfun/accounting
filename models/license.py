from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import BaseModel


class LicenseModel(BaseModel):
    __tablename__ = "license"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(nullable=False)
    number: Mapped[int] = mapped_column(nullable=False)
    given_date: Mapped[str] = mapped_column(nullable=False)
    given_by: Mapped[str] = mapped_column(nullable=False)
    # organization_id: Mapped[int] = mapped_column(ForeignKey("organization.id"))

    organization = relationship("OrganizationModel", back_populates="license")
