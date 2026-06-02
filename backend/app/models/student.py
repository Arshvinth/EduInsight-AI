from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, DateTime
from datetime import datetime
from app.core.database import Base


# SQLAlchemy model for the students table
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    student_code = Column(String(50), unique=True, nullable=False, index=True)
    full_name = Column(String(150), nullable=False)
    department = Column(String(100), nullable=False)
    registered_degree = Column(String(150), nullable=True)
    specialization = Column(String(150), nullable=True)
    semester = Column(Integer, nullable=False)
    year = Column(Integer, nullable=True)   # Updated by faculty/admin
    dob = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)
    cgpa = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)