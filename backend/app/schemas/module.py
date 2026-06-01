from pydantic import BaseModel
from typing import Optional


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

    class Config:
        from_attributes = True


# defines module input/output shape