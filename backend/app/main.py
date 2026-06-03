from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine, Base
from app.models.user import User
from app.models.student import Student
from app.models.module import Module
from app.models.enrollment import Enrollment
from app.models.attendance import Attendance
from app.models.result import Result
from app.models.document import Document, DocumentChunk

from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.students import router as students_router
from app.api.routes.modules import router as modules_router
from app.api.routes.enrollments import router as enrollments_router
from app.api.routes.attendance import router as attendance_router
from app.api.routes.results import router as results_router
from app.api.routes.ai import router as ai_router
from app.api.routes.ml import router as ml_router


app = FastAPI(title="EduInsight AI API")


@app.on_event("startup")
def startup_db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connected successfully")

        # Create all missing tables
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully")
    except Exception as e:
        print("Database connection failed:", e)


@app.get("/")
def root():
    return {"message": "EduInsight AI Backend is running"}


# Register all routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(students_router)
app.include_router(modules_router)
app.include_router(enrollments_router)
app.include_router(attendance_router)
app.include_router(results_router)
app.include_router(ai_router)
app.include_router(ml_router)