from flask_combo_jsonapi import ResourceList, ResourceDetail

from newspapper.models.database import db
from newspapper.models import Author
from newspapper.schemas import AuthorSchema


class AuthorBase:
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorList(AuthorBase, ResourceList):
    pass


class AuthorDetail(AuthorBase, ResourceDetail):
    pass
