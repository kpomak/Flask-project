from flask_combo_jsonapi import ResourceList, ResourceDetail

from newspapper.models.database import db
from newspapper.models import Author
from newspapper.schemas import AuthorSchema


class AuthorBase:
    schema = AuthorSchema


class AuthorList(AuthorBase, ResourceList):
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorDetail(AuthorBase, ResourceDetail):
    data_layer = {
        "session": db.session,
        "model": Author,
    }
