from sqlalchemy import Column, Integer, String, Text
from app.database.db import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(255),nullable=False)
    content = Column(String,nullable=False)
