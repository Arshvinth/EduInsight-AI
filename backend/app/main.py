# from fastapi import FastAPI

# app = FastAPI(title="EduInsight AI API")

# @app.get("/")
# def root():
#     return {"message": "EduInsight AI Backend is running"}

from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine

app = FastAPI(title="EduInsight AI API")

@app.on_event("startup")
def startup_db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Database connected successfully")
    except Exception as e:
        print("Database connection failed:", e)

@app.get("/")
def root():
    return {"message": "EduInsight AI Backend is running"}