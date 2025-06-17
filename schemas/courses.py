from pydantic import BaseModel, Field

class SchemaCourse(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    teacher: str = Field(min_length=3, max_length=30)
    duration: int = Field(gt=0, lt=12)
    price: int = Field(gt=0)
