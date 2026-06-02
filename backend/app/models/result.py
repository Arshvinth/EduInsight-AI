from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from datetime import datetime
from app.core.database import Base


# SQLAlchemy model for the results table
class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)

    # Student whose result is being recorded
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    # Module for which the result is recorded
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)

    # Marks obtained by the student
    marks = Column(Float, nullable=False)

    # Letter grade such as A, B, C, etc.
    grade = Column(String(5), nullable=False)

    # Semester number
    semester = Column(Integer, nullable=False)

    # Academic year
    year = Column(Integer, nullable=True)

    # Faculty/admin user who entered the result
    entered_by = Column(Integer, ForeignKey("users.id"), nullable=False)

    # When this result was created
    created_at = Column(DateTime, default=datetime.utcnow)  