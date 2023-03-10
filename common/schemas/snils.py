from common.schemas.base import RWModelCamelize


class SNILSBase(RWModelCamelize):
    series: int
    number: int
    given_by: str


class SNILS(SNILSBase):
    id: int
