from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api

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


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app=app, plugins=[api_spec_plugin])

    api.route(TagList, "tag_list", "/api/tags/", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>", tag="Tag")

    api.route(CustomUserList, "user_list", "/api/users/", tag="User")
    api.route(CustomUserDetail, "user_detail", "/api/users/<int:id>", tag="User")

    api.route(AuthorList, "author_list", "/api/authors/", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>", tag="Author")

    api.route(ArticleList, "article_list", "/api/articles/", tag="Article")
    api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>", tag="Article")

    return api
