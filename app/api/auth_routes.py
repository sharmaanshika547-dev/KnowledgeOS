from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.auth import (
    UserLogin,
    UserRegister,
    Token,
)
from app.schemas.user import UserResponse
from app.services.auth_service import auth_service


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201,
)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db),
):

    return auth_service.register_user(
        db=db,
        user_data=user_data,
    )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db),
):

    return auth_service.login_user(
        db=db,
        user_data=user_data,
    )
