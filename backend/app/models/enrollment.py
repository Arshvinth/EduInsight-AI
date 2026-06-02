from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


# SQLAlchemy model for the enrollments table
class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    # Links the enrollment to a student
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    # Links the enrollment to a module
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=False)

    # Current status of enrollment
    status = Column(String(50), default="enrolled")

    # Time when the student enrolled
    enrolled_at = Column(DateTime, default=datetime.utcnow)