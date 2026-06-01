from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine, Base
from app.models.user import User
from app.api.routes.auth import router as auth_router


app = FastAPI(title="EduInsight AI API")


# Test database connection on startup
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


# Root endpoint
@app.get("/")
def root():
    return {"message": "EduInsight AI Backend is running"}


# Include auth routes
app.include_router(auth_router)