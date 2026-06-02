from sqlalchemy.orm import Session
from app.models.module import Module
from app.schemas.module import ModuleCreate


# Get a module by its code
def get_module_by_code(db: Session, module_code: str):
    return db.query(Module).filter(Module.module_code == module_code).first()


# Get a module by its ID
def get_module_by_id(db: Session, module_id: int):
    return db.query(Module).filter(Module.id == module_id).first()


# Get all modules
def get_all_modules(db: Session):
    return db.query(Module).all()


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


# Update an existing module
def update_module(db: Session, db_module: Module, module_data: ModuleCreate):
    db_module.module_code = module_data.module_code
    db_module.module_name = module_data.module_name
    db_module.credits = module_data.credits
    db_module.department = module_data.department
    db_module.semester = module_data.semester

    db.commit()
    db.refresh(db_module)
    return db_module