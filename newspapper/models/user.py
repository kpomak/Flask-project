from flask_login import UserMixin
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from newspapper.models.database import db


class CustomUser(db.Model, UserMixin):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(120), unique=False, nullable=True)
    last_name = Column(String(120), unique=False, nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), unique=False, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    author = relationship("Author", uselist=False, back_populates="user")

    def __repr__(self) -> str:
        return f"<CustomUser {self.id} {self.username}>"


class Author(db.Model):

    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("CustomUser", back_populates="author")
    articles = relationship("Article", back_populates="author")

    def __repr__(self) -> str:
        return f"<Author {self.id} {self.user_id}>"
