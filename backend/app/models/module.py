from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base


# SQLAlchemy model for the modules table
class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    module_code = Column(String(50), unique=True, nullable=False, index=True)
    module_name = Column(String(150), nullable=False)
    credits = Column(Integer, nullable=False)
    department = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)