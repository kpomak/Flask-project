from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource

from newspapper.models.database import db
from newspapper.models import Article
from newspapper.schemas import ArticleSchema


class ArticleBase:
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}


class ArticleList(ArticleBase, ResourceList):
    events = ArticleListEvents


class ArticleDetail(ArticleBase, ResourceDetail):
    pass
