from flask import Blueprint
from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.event import EventPlugin
from flask_combo_jsonapi import Api
from combojsonapi.permission import PermissionPlugin

from newspapper.api.tag import TagDetail, TagList
from newspapper.api.article import ArticleDetail, ArticleList
from newspapper.api.author import AuthorDetail, AuthorList
from newspapper.api.user import CustomUserDetail, CustomUserList


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "Author": "Author API",
            "Article": "Article API",
            "User": "User API",
        },
    )
    return api_spec_plugin


def init_api(app, api_blueprint):
    event_plugin = EventPlugin()
    permission_plugin = PermissionPlugin(strict=False)
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app=app, plugins=[api_spec_plugin, event_plugin, permission_plugin])

    api.route(TagList, "tag_list", "/api/tags/", tag="Tag", blueprint=api_blueprint)
    api.route(
        TagDetail,
        "tag_detail",
        "/api/tags/<int:id>",
        tag="Tag",
        blueprint=api_blueprint,
    )

    api.route(
        CustomUserList, "user_list", "/api/users/", tag="User", blueprint=api_blueprint
    )
    api.route(
        CustomUserDetail,
        "user_detail",
        "/api/users/<int:id>",
        tag="User",
        blueprint=api_blueprint,
    )

    api.route(
        AuthorList,
        "author_list",
        "/api/authors/",
        tag="Author",
        blueprint=api_blueprint,
    )
    api.route(
        AuthorDetail,
        "author_detail",
        "/api/authors/<int:id>",
        tag="Author",
        blueprint=api_blueprint,
    )

    api.route(
        ArticleList,
        "article_list",
        "/api/articles/",
        tag="Article",
        blueprint=api_blueprint,
    )
    api.route(
        ArticleDetail,
        "article_detail",
        "/api/articles/<int:id>",
        tag="Article",
        blueprint=api_blueprint,
    )

    return api


api_app = Blueprint("api", __name__)
