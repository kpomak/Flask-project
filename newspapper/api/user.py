from flask_combo_jsonapi import ResourceList, ResourceDetail

from newspapper.models.database import db
from newspapper.models import CustomUser
from newspapper.schemas import CustomUserSchema


class CustomUserBase:
    schema = CustomUserSchema


class CustomUserList(CustomUserBase, ResourceList):
    data_layer = {
        "session": db.session,
        "model": CustomUser,
    }


class CustomUserDetail(CustomUserBase, ResourceDetail):
    data_layer = {
        "session": db.session,
        "model": CustomUser,
    }
