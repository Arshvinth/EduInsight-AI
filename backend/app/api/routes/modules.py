from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_admin_or_faculty
from app.models.user import User
from app.schemas.module import ModuleCreate, ModuleRead
from app.crud.module import (
    get_module_by_code,
    get_module_by_id,
    get_all_modules,
    create_module,
    update_module
)
from app.models.module import Module


# Router for module endpoints
router = APIRouter(prefix="/modules", tags=["Modules"])


# Create a module
@router.post("/", response_model=ModuleRead)
def add_module(
    module: ModuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    existing = get_module_by_code(db, module.module_code)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Module code already exists"
        )

    return create_module(db, module)


# Get all modules
@router.get("/", response_model=list[ModuleRead])
def list_modules(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_modules(db)


# Get one module by ID
@router.get("/{module_id}", response_model=ModuleRead)
def read_module(
    module_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    module = get_module_by_id(db, module_id)
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module not found"
        )
    return module


# Update a module
@router.put("/{module_id}", response_model=ModuleRead)
def edit_module(
    module_id: int,
    module_data: ModuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    module = get_module_by_id(db, module_id)
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module not found"
        )

    return update_module(db, module, module_data)


# Simple modules count endpoint for dashboard
@router.get("/count", response_model=dict)
def modules_count(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    count = db.query(Module).count()
    return {"count": count}