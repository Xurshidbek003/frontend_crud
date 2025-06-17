from fastapi import FastAPI
from db import Base, engine
from routers.students import student_router

app = FastAPI(title="Iteach education")

Base.metadata.create_all(bind=engine)

app.include_router(student_router, tags=["Students"])
