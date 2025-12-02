#Table definitiion for Note model
from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)