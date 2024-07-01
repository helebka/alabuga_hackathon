from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Base


class EngineController:
    def __init__(self) -> None:
        self._engine = create_engine("sqlite:///app/database/test.db", echo=True)
        Base.metadata.create_all(self.engine)
    
    @property
    def engine(self):
        return self._engine
    
    def create_session(self):
        return Session(bind=self.engine)
