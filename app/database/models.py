import sqlalchemy

from sqlalchemy.orm import DeclarativeBase
from flask_login import UserMixin


class Base(DeclarativeBase):
    pass


class User(Base, UserMixin):
    __tablename__ = "users"
    
    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
    
    email = sqlalchemy.Column(
        sqlalchemy.String(256),
        unique=True
    )
    
    password = sqlalchemy.Column(
        sqlalchemy.String(512)
    )
