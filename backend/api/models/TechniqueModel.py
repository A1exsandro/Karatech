from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Technique(Base):
    __tablename__ = "technique"

    id = Column(Integer, primary_key=True)
    name = Column(String)
