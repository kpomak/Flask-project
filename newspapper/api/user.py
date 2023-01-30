from flask_combo_jsonapi import ResourceList, ResourceDetail

from newspapper.models.database import db
from newspapper.models import CustomUser
from newspapper.schemas import CustomUserSchema


class CustomUserBase:
    schema = CustomUserSchema
    data_layer = {
        "session": db.session,
        "model": CustomUser,
    }


class CustomUserList(CustomUserBase, ResourceList):
    pass


class CustomUserDetail(CustomUserBase, ResourceDetail):
    pass
