from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine, Base
from app.models.user import User
from app.models.student import Student
from app.api.routes.auth import router as auth_router
from app.api.routes.users import router as users_router
from app.api.routes.students import router as students_router


app = FastAPI(title="EduInsight AI API")


@app.on_event("startup")
def startup_db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connected successfully")

        # Create tables if they do not exist
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully")
    except Exception as e:
        print("Database connection failed:", e)


@app.get("/")
def root():
    return {"message": "EduInsight AI Backend is running"}


# Register routers
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(students_router)