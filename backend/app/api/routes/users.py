from fastapi import APIRouter, Depends
from app.dependencies.auth import get_current_user
from app.models.user import User


# Router for user-related endpoints
router = APIRouter(prefix="/users", tags=["Users"])


# Get currently logged-in user's info
@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role
    }