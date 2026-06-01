from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate


# Get a student by user_id
def get_student_by_user_id(db: Session, user_id: int):
    return db.query(Student).filter(Student.user_id == user_id).first()


# Get a student by student code
def get_student_by_code(db: Session, student_code: str):
    return db.query(Student).filter(Student.student_code == student_code).first()


# Create a new student profile
def create_student(db: Session, student_data: StudentCreate):
    db_student = Student(
        user_id=student_data.user_id,
        student_code=student_data.student_code,
        full_name=student_data.full_name,
        department=student_data.department,
        semester=student_data.semester,
        dob=student_data.dob,
        gender=student_data.gender,
        cgpa=student_data.cgpa
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student