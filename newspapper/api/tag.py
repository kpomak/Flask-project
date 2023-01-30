from flask_combo_jsonapi import ResourceDetail, ResourceList
from newspapper.schemas import TagSchema
from newspapper.models.database import db
from newspapper.models import Tag


class TagBase:
    schema = TagSchema


class TagList(TagBase, ResourceList):
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagDetail(TagBase, ResourceDetail):
    data_layer = {
        "session": db.session,
        "model": Tag,
    }
