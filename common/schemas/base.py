from pydantic import BaseModel as PydanticBaseModel, BaseConfig
from humps.camel import case


class RWModelCamelize(PydanticBaseModel):
    class Config(BaseConfig):
        alias_generator = case
        allow_population_by_field_name = True
        orm_mode = True
