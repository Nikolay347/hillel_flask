from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class StudentReadModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    student_id: int = Field(alias="id")
    name: str
    birth_date: date
    course: Optional[str] = None
    photo_url: Optional[str] = None