from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta

from app.schemas.user import UserCreate, UserRead
from app.schemas.token import Token, UserLogin
from app.schemas.student import StudentCreate
from app.crud.user import create_user, get_user_by_username, get_user_by_email, authenticate_user
from app.crud.student import create_student
from app.core.security import create_access_token
from app.core.config import settings
from app.dependencies.database import get_db


# Router for authentication endpoints
router = APIRouter(prefix="/auth", tags=["Auth"])


# Register a new user
@router.post("/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username already exists
    existing_username = get_user_by_username(db, user.username)
    if existing_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # Check if email already exists
    existing_email = get_user_by_email(db, user.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    # Create user first
    new_user = create_user(db, user)

    # If the user is a student, create a matching student profile automatically
    if new_user.role == "student":
        student_data = StudentCreate(
            user_id=new_user.id,
            student_code=f"STU{new_user.id:04d}",
            full_name=new_user.username,  # temporary default, can be updated later
            department="Not Assigned",
            semester=1,
            dob=None,
            gender=None,
            cgpa=0.0
        )
        create_student(db, student_data)

    return new_user


# Login user and return JWT token
@router.post("/login", response_model=Token)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # Authenticate username and password
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    # Create JWT token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }