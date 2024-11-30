from sqlalchemy import Column, Integer, String
from database import Base

class Technique(Base):
    __tablename__ = "techniques"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
