from flask_combo_jsonapi import ResourceList, ResourceDetail

from newspapper.models.database import db
from newspapper.models import CustomUser
from newspapper.schemas import CustomUserSchema
from newspapper.api.permissions.user import (
    CustomUserGetPermission,
    CustomUserPatchPermission,
)


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
        "permission_patch": [CustomUserPatchPermission],
        "permission_get": [CustomUserGetPermission],
        "model": CustomUser,
    }
