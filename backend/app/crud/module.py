from sqlalchemy.orm import Session
from app.models.module import Module
from app.schemas.module import ModuleCreate


# Get a module by module code
def get_module_by_code(db: Session, module_code: str):
    return db.query(Module).filter(Module.module_code == module_code).first()


# Create a new module
def create_module(db: Session, module_data: ModuleCreate):
    db_module = Module(
        module_code=module_data.module_code,
        module_name=module_data.module_name,
        credits=module_data.credits,
        department=module_data.department,
        semester=module_data.semester
    )

    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module