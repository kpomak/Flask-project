from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource
from newspapper.models.database import db
from newspapper.models import Author, Article
from newspapper.schemas import AuthorSchema


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {
            "count": Article.query.filter(Article.author_id == kwargs["id"]).count()
        }


class AuthorBase:
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author,
    }


class AuthorList(AuthorBase, ResourceList):
    pass


class AuthorDetail(AuthorBase, ResourceDetail):
    events = AuthorDetailEvents
