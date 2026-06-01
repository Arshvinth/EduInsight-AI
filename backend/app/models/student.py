from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, DateTime
from datetime import datetime
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    student_code = Column(String(50), unique=True, nullable=False, index=True)
    full_name = Column(String(150), nullable=False)
    department = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    dob = Column(Date, nullable=True)
    gender = Column(String(20), nullable=True)
    cgpa = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)