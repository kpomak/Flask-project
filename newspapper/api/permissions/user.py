from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForGet,
    PermissionForPatch,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from newspapper.models.user import CustomUser


class CustomUserGetPermission(PermissionMixin):
    """
    Describe permissions for get User
    """

    ALL_AVAILABLE_FIELDS = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
    ]

    def get(
        self, *args, many=True, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForGet:
        if not current_user.is_authenticated:
            raise AccessDenied("No access")

        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get


class CustomUserPatchPermission(PermissionMixin):
    """
    Describe permission for patch User.
    """

    PATCH_AVAILABLE_FIELDS = (
        "first_name",
        "last_name",
        "is_staff",
    )

    def patch_permission(
        self, *args, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForPatch:

        if not (current_user.is_authenticated and current_user.is_staff):
            raise AccessDenied("Login first and keep being admin")

        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(
        self,
        *args,
        data=None,
        obj=None,
        user_permission: PermissionUser = None,
        **kwargs
    ) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(
            model=CustomUser
        )
        return {
            field: data
            for field, data in data.items()
            if field in permission_for_patch.columns
        }
