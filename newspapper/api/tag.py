from flask_combo_jsonapi import ResourceDetail, ResourceList
from newspapper.schemas import TagSchema
from newspapper.models.database import db
from newspapper.models import Tag


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }
