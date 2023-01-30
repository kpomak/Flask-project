from flask_combo_jsonapi import ResourceList, ResourceDetail

from newspapper.models.database import db
from newspapper.models import Article
from newspapper.schemas import ArticleSchema


class ArticleBase:
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleList(ArticleBase, ResourceList):
    pass


class ArticleDetail(ArticleBase, ResourceDetail):
    pass
