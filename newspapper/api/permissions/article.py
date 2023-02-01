from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForPatch,
    PermissionForGet,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from newspapper.models.article import Article


class CommonPermission(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
        "id",
        "title",
        "body",
        "dt_craeted",
        "dt_updated",
        "author",
        "tags",
    ]
    FIELDS_FOR_PATCH = [
        "title",
        "body",
    ]


class ArticlePermission(CommonPermission):
    def get(
        self, *args, many=True, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForGet:
        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get

    def patch_permission(
        self, *args, user_permission: PermissionUser = None, **kwargs
    ) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.FIELDS_FOR_PATCH, 10)
        return self.permission_for_patch

    def patch_data(
        self,
        *args,
        data: dict = None,
        obj=None,
        user_permission: PermissionUser = None,
        **kwargs
    ) -> dict:
        if not (
            current_user.is_authenticated
            and (current_user.is_staff or current_user.author == obj.author)
        ):
            raise AccessDenied("You should be an author or an odmen")

        permission_for_patch = user_permission.permission_for_patch_permission(
            model=Article
        )
        return {
            field: data
            for field, data in data.items()
            if field in permission_for_patch.columns
        }
