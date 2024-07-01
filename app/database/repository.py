from typing import List, Optional
from werkzeug.security import generate_password_hash

from .engine import EngineController
from .models import User


class UserRepository:
    database_controller = EngineController()

    @classmethod
    def get_users(cls) -> List[User]:
        session = cls.database_controller.create_session()
        users = session.query(User).all()
        session.close()
        return users

    @classmethod
    def get_user(cls, user_id: int) -> User:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return user

    @classmethod
    def get_user_by_email(cls, email: str) -> User:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.email == email).first()
        session.close()
        return user

    @classmethod
    def create_user(cls, email: str, password: str) -> None:
        session = cls.database_controller.create_session()
        password = generate_password_hash(password)
        user = User(
            email=email,
            password=password
        )
        session.add(user)
        session.commit()
        session.close()

    @classmethod
    def update_user(
        cls,
        user_id: int,
        email: str,
        password: str
    ) -> Optional[User]:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.email = email
            user.password = generate_password_hash(password)
            session.commit()
        session.close()
        return user

    @classmethod
    def delete_user(cls, user_id: int) -> bool:
        session = cls.database_controller.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            session.close()
            return True
        session.close()
        return False
