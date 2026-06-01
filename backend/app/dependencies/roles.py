from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.models.user import User


# Require the current user to be an admin
def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user


# Require the current user to be either admin or faculty
def require_admin_or_faculty(current_user: User = Depends(get_current_user)):
    if current_user.role not in ["admin", "faculty"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin or faculty access required"
        )
    return current_user