from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def create_user(
        self,
        db: Session,
        user_model: User,
    ) -> User:

        db.add(user_model)

        return user_model

    def get_user_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_user_by_id(
        self,
        db: Session,
        user_id: int,
    ) -> User | None:

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )


user_repository = UserRepository()
