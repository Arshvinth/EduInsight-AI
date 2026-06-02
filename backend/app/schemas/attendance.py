from pydantic import BaseModel
from datetime import date, datetime


# Schema used when creating attendance
class AttendanceCreate(BaseModel):
    student_id: int
    module_id: int
    status: str
    attendance_date: date


# Schema used when returning attendance records
class AttendanceRead(BaseModel):
    id: int
    student_id: int
    module_id: int
    status: str
    attendance_date: date
    marked_by: int
    created_at: datetime

    class Config:
        from_attributes = True