from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_db() -> Session:
    with sessionmaker(create_engine("sqlite:///db.db"))() as db:
        try:
            yield db
        finally:
            db.close_all()
