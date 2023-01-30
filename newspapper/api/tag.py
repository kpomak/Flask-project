from flask_combo_jsonapi import ResourceDetail, ResourceList
from newspapper.schemas import TagSchema
from newspapper.models.database import db
from newspapper.models import Tag


class TagBase:
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag,
    }


class TagList(TagBase, ResourceList):
    pass


class TagDetail(TagBase, ResourceDetail):
    pass
