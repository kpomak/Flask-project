from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource

from newspapper.models.database import db
from newspapper.models import Article
from newspapper.schemas import ArticleSchema


class ArticleBase:
    schema = ArticleSchema


class ArticleListEvents(EventsResource):
    def event_get_count(self):
        return {"count": Article.query.count()}


class ArticleList(ArticleBase, ResourceList):
    events = ArticleListEvents
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ArticleBase, ResourceDetail):
    data_layer = {
        "session": db.session,
        "model": Article,
    }
