from common.schemas.base import RWModelCamelize


class PassportBase(RWModelCamelize):
    series: int
    number: int
    given_by: str
    register_address: str
    birthday_address: str


class Passport(PassportBase):
    id: int
