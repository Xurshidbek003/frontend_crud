from models.students import Students

def add_student(form, db):
    student = Students(
        name = form.name,
        age = form.age,
        address = form.address,
    )
    db.add(student)
    db.commit()
    return {"message": "Student bazaga qoshildi !"}

def update_student(ident, form, db):
    student = db.query(Students).get(ident)
    student.name = form.name
    student.age = form.age
    student.address = form.address
    db.commit()
    return {"message": "Student ma'lumotlari tahrirlandi !"}

def delete_student(ident, db):
    student = db.query(Students).get(ident)
    db.delete(student)
    db.commit()
    return {"message": "Student o'chirildi !"}