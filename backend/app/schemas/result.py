from pydantic import BaseModel
from datetime import datetime


# Schema used when creating a result
class ResultCreate(BaseModel):
    student_id: int
    module_id: int
    marks: float
    grade: str
    semester: int
    year: int | None = None


# Schema used when returning result data
class ResultRead(BaseModel):
    id: int
    student_id: int
    module_id: int
    marks: float
    grade: str
    semester: int
    year: int | None = None
    entered_by: int
    created_at: datetime

    class Config:
        from_attributes = True