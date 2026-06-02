from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_admin_or_faculty
from app.models.user import User
from app.schemas.attendance import AttendanceCreate, AttendanceRead
from app.crud.attendance import get_attendance_record, get_attendance_by_student, create_attendance
from app.crud.student import get_student_by_id, get_student_by_user_id
from app.crud.module import get_module_by_id
from app.crud.enrollment import get_enrollment


# Router for attendance endpoints
router = APIRouter(prefix="/attendance", tags=["Attendance"])


# Faculty/admin marks attendance for a student
@router.post("/", response_model=AttendanceRead)
def mark_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin_or_faculty)
):
    # Check if student exists
    student = get_student_by_id(db, attendance.student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )

    # Check if module exists
    module = get_module_by_id(db, attendance.module_id)
    if not module:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Module not found"
        )

    # Verify student is enrolled in this module
    enrollment = get_enrollment(db, attendance.student_id, attendance.module_id)
    if not enrollment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student is not enrolled in this module"
        )

    # Prevent duplicate attendance for the same date
    existing = get_attendance_record(
        db,
        attendance.student_id,
        attendance.module_id,
        attendance.attendance_date
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Attendance already marked for this student on this date"
        )

    # Save attendance and record who marked it
    new_attendance = create_attendance(db, attendance, marked_by=current_user.id)
    return new_attendance


# Student views own attendance
@router.get("/me", response_model=list[AttendanceRead])
def my_attendance(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Only students can access this endpoint
    if current_user.role != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only students can view their attendance"
        )

    # Find student profile by current user's id
    student = get_student_by_user_id(db, current_user.id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found"
        )

    return get_attendance_by_student(db, student.id)