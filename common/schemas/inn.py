from common.schemas.base import RWModelCamelize


class INNBase(RWModelCamelize):
    series: int
    number: int
    given_by: str


class INN(INNBase):
    id: int
