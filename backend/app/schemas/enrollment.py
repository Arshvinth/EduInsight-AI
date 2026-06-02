from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Schema used when a student enrolls in a module
class EnrollmentCreate(BaseModel):
    module_id: int
    status: Optional[str] = "enrolled"


# Schema used when returning enrollment data
class EnrollmentRead(BaseModel):
    id: int
    student_id: int
    module_id: int
    status: str
    enrolled_at: datetime

    class Config:
        from_attributes = True