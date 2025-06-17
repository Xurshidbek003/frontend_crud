from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from db import database
from models.students import Students
from functions.students import add_student
from schemas.students import SchemaStudent


student_router = APIRouter()


@student_router.get("/get_students")
def get_students(db: Session = Depends(database)):
    try:
        return db.query(Students).options(joinedload(Students.course)).all()
    except Exception as e:
        return e


@student_router.post("/add_student")
def create_student(form: SchemaStudent, db: Session = Depends(database)):
    try:
        return add_student(form, db)
    except Exception as e:
        return e
