from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database
from functions.courses import add_course
from models.courses import Courses
from schemas.courses import SchemaCourse

course_router = APIRouter()


@course_router.get("/get_course")
def get_courses(db: Session = Depends(database)):
    try:
        return db.query(Courses).all()
    except Exception as e:
        return e


@course_router.post("/add_course")
def create_course(form: SchemaCourse, db: Session = Depends(database)):
    try:
        return add_course(form, db)
    except Exception as e:
        return e