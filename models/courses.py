from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base

class Courses(Base):

    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    teacher = Column(String(50), nullable=False)
    duration = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    student_count = Column(Integer, nullable=False)

    student = relationship("Students", back_populates="course")
