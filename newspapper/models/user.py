from sqlalchemy import Column, Integer, String, Boolean
from newspapper.models.database import db


class CustomUser(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f"<CustomUser {self.id} {self.username}>"