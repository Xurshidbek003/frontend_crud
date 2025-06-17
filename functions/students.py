from fastapi import HTTPException

from models.courses import Courses
from models.students import Students


def add_student(form, db):

    course = db.query(Courses).filter(Courses.id == form.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Kurs topilmadi !")

    course.student_count += 1

    student = Students(
        name = form.name,
        age = form.age,
        address = form.address,
        course_id = form.course_id
    )
    db.add(student)
    db.commit()
    return {"message": "Student bazaga qoshildi !"}