from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_admin_or_faculty
from app.models.user import User
from app.schemas.student import StudentCreate, StudentRead, StudentUpdate
from app.crud.student import (
    create_student,
    get_student_by_user_id,
    get_student_by_code,
    get_student_by_id,
    update_student
)
from app.models.student import Student


# Router for student endpoints
router = APIRouter(prefix="/students", tags=["Students"])


# Create a student profile
@router.post("/", response_model=StudentRead)
def create_student_profile(
    student: StudentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
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


# Faculty/admin can update any student field except id/user_id
@router.put("/{student_id}", response_model=StudentRead)
def update_student_profile(
    student_id: int,
    update_data: StudentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    student = get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    updated_student = update_student(db, student, update_data)
    return updated_student


# List all students (admin/faculty only)
@router.get("/", response_model=list[StudentRead])
def list_students(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    return db.query(Student).all()


# Get a single student by id (admin/faculty only)
@router.get("/{student_id}", response_model=StudentRead)
def get_student_detail(
    student_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    student = get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return student


# Return a simple student count for dashboards
@router.get("/count", response_model=dict)
def students_count(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    count = db.query(Student).count()
    return {"count": count}