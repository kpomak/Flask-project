from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api

from newspapper.api.tag import TagDetail, TagList


def create_api_spec_plugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
        "Tag": "Tag API",
        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_plugin(app)
    api = Api(app=app, plugins=[api_spec_plugin])
    api.route(TagList, "tag_list", "/api/tags/")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/")
    return api
