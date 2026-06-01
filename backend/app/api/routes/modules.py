from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.roles import require_admin_or_faculty
from app.models.user import User
from app.schemas.module import ModuleCreate, ModuleRead
from app.crud.module import create_module, get_module_by_code


# Router for module endpoints
router = APIRouter(prefix="/modules", tags=["Modules"])


# Create a new module
@router.post("/", response_model=ModuleRead)
def add_module(
    module: ModuleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    # Prevent duplicate module codes
    existing_module = get_module_by_code(db, module.module_code)
    if existing_module:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Module code already exists"
        )

    new_module = create_module(db, module)
    return new_module