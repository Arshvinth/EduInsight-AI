from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.student import StudentCreate, StudentRead
from app.crud.student import create_student, get_student_by_user_id, get_student_by_code


# Router for student endpoints
router = APIRouter(prefix="/students", tags=["Students"])


# Create a student profile
@router.post("/", response_model=StudentRead)
def create_student_profile(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only the user themselves or admin can create student profile later if needed
    existing_student = get_student_by_user_id(db, student.user_id)
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student profile already exists for this user"
        )

    existing_code = get_student_by_code(db, student.student_code)
    if existing_code:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student code already exists"
        )

    new_student = create_student(db, student)
    return new_student


# Get current user's student profile
@router.get("/me", response_model=StudentRead)
def read_my_student_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    student = get_student_by_user_id(db, current_user.id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found"
        )
    return student