from typing import Generic, Type, TypeVar

from sqlalchemy.orm import declarative_base, Session
from pydantic import BaseModel

from models.base import BaseModel as Model


ModelType = TypeVar("ModelType", bound=declarative_base())


class BaseController(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    @staticmethod
    def _create(db: Session, obj: ModelType) -> ModelType:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def patch_model(db: Session, model: Model, id: int, values: BaseModel):
        obj = db.get(model, id)
        for key, value in values.dict().items():
            if value:
                setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def _delete(db: Session, model: Model, id: int):
        obj = db.get(model, id)
        db.delete(obj)
        db.commit()
        return obj
