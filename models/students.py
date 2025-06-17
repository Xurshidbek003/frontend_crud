from sqlalchemy import Column, Integer, String
from db import Base


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)

