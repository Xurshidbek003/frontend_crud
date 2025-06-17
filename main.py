from fastapi import FastAPI
from db import Base, engine
from models.students import Students
from routers.students import student_router
from sqladmin import Admin, ModelView
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Iteach education", docs_url='/')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

Base.metadata.create_all(bind=engine)

app.include_router(student_router, tags=["Students"])

class StudentAdmin(ModelView, model=Students):
    column_list = [Students.id, Students.name, Students.age, Students.address]
    column_labels = {"id": "ID", "name": "Ism", "age": "Yosh", "address": "Manzili"}
    name_plural = "Students"
    column_searchable_list = [Students.name, Students.address]
    column_filters = [Students.name, Students.address]
    column_default_sort = (Students.id, True)

admin = Admin(app, engine)
admin.add_view(StudentAdmin)