from sqlalchemy.orm import Session
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


# Get a student by user_id
def get_student_by_user_id(db: Session, user_id: int):
    return db.query(Student).filter(Student.user_id == user_id).first()


# Get a student by student code
def get_student_by_code(db: Session, student_code: str):
    return db.query(Student).filter(Student.student_code == student_code).first()


# Get a student by id
def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


# Create a new student profile
def create_student(db: Session, student_data: StudentCreate):
    db_student = Student(
        user_id=student_data.user_id,
        student_code=student_data.student_code,
        full_name=student_data.full_name,
        department=student_data.department,
        semester=student_data.semester,
        year=student_data.year,
        dob=student_data.dob,
        gender=student_data.gender,
        cgpa=student_data.cgpa,
        registered_degree=student_data.registered_degree,
        specialization=student_data.specialization
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# Update student profile fields
def update_student(db: Session, db_student: Student, update_data: StudentUpdate):
    update_dict = update_data.model_dump(exclude_unset=True)

    for field, value in update_dict.items():
        setattr(db_student, field, value)

    db.commit()
    db.refresh(db_student)
    return db_student