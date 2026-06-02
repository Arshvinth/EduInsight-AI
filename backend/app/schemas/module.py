from pydantic import BaseModel
from datetime import datetime


# Schema used when creating a module
class ModuleCreate(BaseModel):
    module_code: str
    module_name: str
    credits: int
    department: str
    semester: int


# Schema used when returning module data
class ModuleRead(BaseModel):
    id: int
    module_code: str
    module_name: str
    credits: int
    department: str
    semester: int
    created_at: datetime

    class Config:
        from_attributes = True