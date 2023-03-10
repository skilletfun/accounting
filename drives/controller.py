from sqlalchemy.orm import Session

from common.controller import BaseController
from models.drive import DriveModel


class DriveController(BaseController[DriveModel]):
    def set_to_user(self, db: Session, drive_id: int, user_id: int):
        db.get(self.model, drive_id).user_id = user_id
        db.commit()

    def delete_from_user(self, db: Session, drive_id: int):
        db.get(DriveModel, drive_id).user_id = None
        db.commit()


drive_controller = DriveController(DriveModel)
