from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)
    course_id = Column(Integer,  ForeignKey("courses.id"), nullable=False)

    course = relationship("Courses", back_populates="student")
