from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.schemas.attendance import AttendanceCreate


# Get attendance for a student in a module on a specific date
def get_attendance_record(db: Session, student_id: int, module_id: int, attendance_date):
    return (
        db.query(Attendance)
        .filter(
            Attendance.student_id == student_id,
            Attendance.module_id == module_id,
            Attendance.attendance_date == attendance_date
        )
        .first()
    )


# Get all attendance records for a student
def get_attendance_by_student(db: Session, student_id: int):
    return db.query(Attendance).filter(Attendance.student_id == student_id).all()


# Create a new attendance record
def create_attendance(db: Session, attendance_data: AttendanceCreate, marked_by: int):
    db_attendance = Attendance(
        student_id=attendance_data.student_id,
        module_id=attendance_data.module_id,
        status=attendance_data.status,
        attendance_date=attendance_data.attendance_date,
        marked_by=marked_by
    )

    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance