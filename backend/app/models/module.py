from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base


# SQLAlchemy model for the modules table
class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)

    # Unique module code like CS101
    module_code = Column(String(50), unique=True, nullable=False, index=True)

    # Full module name
    module_name = Column(String(150), nullable=False)

    # Number of credits for the module
    credits = Column(Integer, nullable=False)

    # Department responsible for the module
    department = Column(String(100), nullable=False)

    # Semester in which the module is offered
    semester = Column(Integer, nullable=False)

    # Time when the module was created
    created_at = Column(DateTime, default=datetime.utcnow)