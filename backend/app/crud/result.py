from sqlalchemy.orm import Session
from app.models.result import Result
from app.schemas.result import ResultCreate


# Get a result for a student in a module
def get_result_record(db: Session, student_id: int, module_id: int):
    return (
        db.query(Result)
        .filter(Result.student_id == student_id, Result.module_id == module_id)
        .first()
    )


# Get all results for a student
def get_results_by_student(db: Session, student_id: int):
    return db.query(Result).filter(Result.student_id == student_id).all()


# Create a new result record
def create_result(db: Session, result_data: ResultCreate, entered_by: int):
    db_result = Result(
        student_id=result_data.student_id,
        module_id=result_data.module_id,
        marks=result_data.marks,
        grade=result_data.grade,
        semester=result_data.semester,
        year=result_data.year,
        entered_by=entered_by
    )

    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result


# Update an existing result record
def update_result(db: Session, db_result: Result, result_data: ResultCreate):
    db_result.marks = result_data.marks
    db_result.grade = result_data.grade
    db_result.semester = result_data.semester
    db_result.year = result_data.year

    db.commit()
    db.refresh(db_result)
    return db_result