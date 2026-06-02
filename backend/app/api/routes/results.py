from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_admin_or_faculty
from app.models.user import User
from app.schemas.result import ResultCreate, ResultRead
from app.crud.result import (
    get_result_record,
    get_results_by_student,
    create_result,
    update_result
)
from app.crud.student import get_student_by_id, get_student_by_user_id
from app.crud.module import get_module_by_id
from app.crud.enrollment import get_enrollment


# Router for result endpoints
router = APIRouter(prefix="/results", tags=["Results"])


# Faculty/admin creates or updates a result
@router.post("/", response_model=ResultRead)
def save_result(
    result: ResultCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    # Check student exists
    student = get_student_by_id(db, result.student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    # Check module exists
    module = get_module_by_id(db, result.module_id)
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module not found"
        )

    # Verify student is enrolled in the module
    enrollment = get_enrollment(db, result.student_id, result.module_id)
    if not enrollment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student is not enrolled in this module"
        )

    # Check if a result already exists
    existing = get_result_record(db, result.student_id, result.module_id)
    if existing:
        # Update existing result
        return update_result(db, existing, result)

    # Create a new result
    return create_result(db, result, entered_by=current_user.id)


# Student views own results
@router.get("/me", response_model=list[ResultRead])
def my_results(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only students can view their results
    if current_user.role != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only students can view their results"
        )

    # Find student profile
    student = get_student_by_user_id(db, current_user.id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found"
        )

    return get_results_by_student(db, student.id)