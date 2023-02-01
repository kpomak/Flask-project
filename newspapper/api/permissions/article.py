from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForPatch,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from newspapper.models.user import CustomUser


class ArticlePatchPermission(PermissionMixin):
    """
    Describe permissions for path Article
    """

    ALL_AVAILABLE_FIELDS = [
        "id",
        "title",
        "body",
    ]

    def get(
        self, *args, many=True, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForPatch:
        if not current_user.is_authenticated:
            raise AccessDenied("No access")

        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 15)
        return self.permission_for_patch

    def patch_permission(
        self, *args, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForPatch:

        if not (current_user.is_authenticated and current_user.is_staff):
            raise AccessDenied("You should be an author or an admin")

        self.permission_for_patch.allow_columns = (self.ALL_AVAILABLE_FIELDS, 15)
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
