from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.enrollment import EnrollmentCreate, EnrollmentRead
from app.crud.enrollment import get_enrollment, get_enrollments_by_student, create_enrollment
from app.crud.student import get_student_by_user_id
from app.crud.module import get_module_by_id


# Router for enrollment endpoints
router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


# Student enrolls into a module
@router.post("/", response_model=EnrollmentRead)
def enroll_student(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only students can enroll themselves
    if current_user.role != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only students can enroll in modules"
        )

    # Get the student profile for the current user
    student = get_student_by_user_id(db, current_user.id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found"
        )

    # Get module by ID
    module = get_module_by_id(db, enrollment.module_id)
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module not found"
        )

    # Prevent duplicate enrollments
    existing = get_enrollment(db, student.id, enrollment.module_id)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student is already enrolled in this module"
        )

    # Create enrollment using the logged-in student's ID
    new_enrollment = create_enrollment(
        db,
        student_id=student.id,
        module_id=enrollment.module_id,
        status=enrollment.status
    )
    return new_enrollment


# Get the logged-in student's enrollments
@router.get("/me", response_model=list[EnrollmentRead])
def my_enrollments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only students can view their enrollments
    if current_user.role != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only students can view their enrollments"
        )

    student = get_student_by_user_id(db, current_user.id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found"
        )

    return get_enrollments_by_student(db, student.id)