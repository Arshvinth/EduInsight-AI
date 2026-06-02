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
    year: Optional[int] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    cgpa: Optional[float] = 0.0
    registered_degree: Optional[str] = None
    specialization: Optional[str] = None


# Schema used when returning student data
class StudentRead(BaseModel):
    id: int
    user_id: int
    student_code: str
    full_name: str
    department: str
    registered_degree: Optional[str] = None
    specialization: Optional[str] = None
    semester: int
    year: Optional[int] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    cgpa: float

    class Config:
        from_attributes = True


# Schema used by faculty/admin to update student fields
class StudentUpdate(BaseModel):
    student_code: Optional[str] = None
    full_name: Optional[str] = None
    department: Optional[str] = None
    registered_degree: Optional[str] = None
    specialization: Optional[str] = None
    semester: Optional[int] = None
    year: Optional[int] = None
    dob: Optional[date] = None
    gender: Optional[str] = None
    cgpa: Optional[float] = None

    class Config:
        from_attributes = True