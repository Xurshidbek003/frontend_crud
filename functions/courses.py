from models.courses import Courses


def add_course(form, db):
    course = Courses(
        name = form.name,
        teacher = form.teacher,
        duration = form.duration,
        price = form.price,
        student_count = 0
    )
    db.add(course)
    db.commit()
    return {"message": "Kurs bazaga qoshildi !"}