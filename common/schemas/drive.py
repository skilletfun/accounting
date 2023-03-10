from common.schemas.base import RWModelCamelize


class DriveBase(RWModelCamelize):
    type: str
    number: int


class DriveUpdate(DriveBase):
    given_date: str | None
    is_accepted: bool | None
    is_destroyed: bool
    destroy_date: str | None
    destroy_document: str | None


class Drive(DriveUpdate):
    id: int


class Drives(RWModelCamelize):
    drives: list[Drive]
