from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment


# Get an enrollment by student and module
def get_enrollment(db: Session, student_id: int, module_id: int):
    return (
        db.query(Enrollment)
        .filter(Enrollment.student_id == student_id, Enrollment.module_id == module_id)
        .first()
    )


# Get all enrollments for a student
def get_enrollments_by_student(db: Session, student_id: int):
    return db.query(Enrollment).filter(Enrollment.student_id == student_id).all()


# Create a new enrollment
def create_enrollment(db: Session, student_id: int, module_id: int, status: str = "enrolled"):
    db_enrollment = Enrollment(
        student_id=student_id,
        module_id=module_id,
        status=status
    )

    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment