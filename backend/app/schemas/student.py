from pydantic import BaseModel
from typing import Optional
from datetime import date


# Schema used when creating a student profile
class StudentCreate(BaseModel):
    user_id: int
    student_code: str
    full_name: str
    department: str
    semester: int
    dob: Optional[date] = None
    gender: Optional[str] = None
    cgpa: Optional[float] = 0.0


# Schema used when returning student data
class StudentRead(BaseModel):
    id: int
    user_id: int
    student_code: str
    full_name: str
    department: str
    semester: int
    dob: Optional[date] = None
    gender: Optional[str] = None
    cgpa: float

    class Config:
        from_attributes = True