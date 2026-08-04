from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.models.user import User
from app.repositories.user_repository import user_repository
from app.schemas.auth import (
    Token,
    UserLogin,
    UserRegister,
)


class AuthService:

    def register_user(
        self,
        db: Session,
        user_data: UserRegister,
    ) -> User:

        existing_user = user_repository.get_user_by_email(
            db=db,
            email=user_data.email,
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered.",
            )

        hashed_password = hash_password(
            user_data.password,
        )

        user_model = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=hashed_password,
        )

        user_repository.create_user(
            db=db,
            user_model=user_model,
        )

        db.commit()
        db.refresh(user_model)

        return user_model

    def login_user(
        self,
        db: Session,
        user_data: UserLogin,
    ) -> Token:

        user = user_repository.get_user_by_email(
            db=db,
            email=user_data.email,
        )

        if (
            user is None
            or not verify_password(
                user_data.password,
                user.password_hash,
            )
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        access_token = create_access_token(
            data={
                "sub": str(user.id),
            }
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
        )


auth_service = AuthService()
