from flask_login import UserMixin
from sqlalchemy import Boolean, Column, Integer, String

from newspapper.models.database import db


class CustomUser(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<CustomUser {self.id} {self.username}>"
