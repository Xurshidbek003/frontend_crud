from fastapi import FastAPI
from db import Base, engine
from routers.courses import course_router
from routers.students import student_router

app = FastAPI(title="Iteach education")

Base.metadata.create_all(bind=engine)

app.include_router(student_router, tags=["Students"])
app.include_router(course_router, tags=["Courses"])