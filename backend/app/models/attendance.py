from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
from datetime import datetime
from app.core.database import Base


# SQLAlchemy model for the attendance table
class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    # Student being marked present/absent
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    # Module for which attendance is recorded
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)

    # Attendance status: present, absent, late
    status = Column(String(20), nullable=False)

    # Date of the attendance session
    attendance_date = Column(Date, nullable=False)

    # Faculty/admin user who marked the attendance
    marked_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # When this record was created
    created_at = Column(DateTime, default=datetime.utcnow)