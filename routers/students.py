from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session, joinedload
from db import database
from models.students import Students
from functions.students import add_student, update_student, delete_student
from schemas.students import SchemaStudent


student_router = APIRouter()


@student_router.get("/get_students")
def studentlarni_korish(db: Session = Depends(database)):
    return db.query(Students).options(joinedload(Students.course)).all()


@student_router.post("/add_student")
def student_qoshish(form: SchemaStudent, db: Session = Depends(database)):
    return add_student(form, db)

@student_router.put('/update_student')
def studentni_tahrirlash(ident: int, form: SchemaStudent, db: Session = Depends(database)):
    return update_student(ident, form, db)


@student_router.delete('/delete_student')
def studentni_ochirish(ident: int, db: Session = Depends(database)):
    return delete_student(ident, db)

