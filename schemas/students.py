from pydantic import BaseModel

class SchemaStudent(BaseModel):
    name: str
    age: int
    address: str
