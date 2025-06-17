from pydantic import BaseModel, Field

class SchemaStudent(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    age: int = Field(gt=0, lt=150)
    address: str
    course_id: int