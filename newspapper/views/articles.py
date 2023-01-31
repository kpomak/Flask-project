import requests
import os

from flask import Blueprint, current_app, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from newspapper.forms.article import CreateArticleForm
from newspapper.models import Article, Author, Tag
from newspapper.models.database import db


articles_app = Blueprint("articles_app", __name__)


# @articles_app.route("/", endpoint="list")
# def articles_list():
#     articles = Article.query.options(joinedload(Article.tags)).all()
#     return render_template("articles/list.html", articles=articles)


@articles_app.route("/", endpoint="list")
def articles_list():
    """
    the dumbest view in the whole world =P
    """
    BASE_URL = os.getenv("BASE_URL")
    articles_url = (
        BASE_URL
        + "/api/articles/?include=author%2Ctags&fields%5Barticle%5D=id,title,body,author,tags&fields%5Bauthor%5D=id,user&fields%5Btag%5D=name,id"
    )
    authors_url = (
        BASE_URL
        + "/api/authors/?include=user%2Carticles&fields%5Bauthor%5D=id,user&fields%5Buser%5D=first_name,id,last_name"
    )
    articles_response = requests.get(articles_url).json()
    authors_response = requests.get(authors_url).json()

    authors_list = {
        author["id"]: author["relationships"]["user"]["data"]["id"]
        for author in authors_response["data"]
    }

    users = {
        user["id"]: {
            "user": {
                "first_name": user["attributes"].get("first_name"),
                "last_name": user["attributes"].get("last_name"),
            }
        }
        for user in authors_response["included"]
    }
    tags = {
        item["id"]: {"name": item["attributes"].get("name")}
        for item in articles_response["included"]
        if item["type"] == "tag"
    }
    articles = [
        {
            "id": item["id"],
            "title": item["attributes"]["title"],
            "body": item["attributes"]["body"],
            "author": users[
                authors_list[item["relationships"]["author"]["data"]["id"]]
            ],
            "tags": [
                tags[tag.get("id")]
                for tag in item.get("relationships").get("tags").get("data")
            ],
        }
        for item in articles_response["data"]
    ]
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/<string:tag_name>/", endpoint="filter")
def articles_list(tag_name: str):
    articles = Article.query.options(joinedload(Article.tags)).filter(
        Article.tags.any(Tag.name.contains(tag_name))
    )
    return render_template("articles/list.html", articles=articles)


@articles_app.route("/<int:article_id>/", endpoint="details")
@login_required
def aricle_details(article_id: int):
    article = (
        Article.query.filter_by(id=article_id)
        .options(joinedload(Article.tags))
        .one_or_none()
    )
    if not article:
        raise NotFound(f"Article doesn't exists! 😢")
    return render_template(
        "articles/details.html",
        article=article,
    )


@articles_app.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():

        article = Article(title=form.title.data.strip(), body=form.body.data)
        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            article.tags.extend(selected_tags)

        if current_user.author:
            # use existing author if present
            article.author_id = current_user.author_id
        else:
            # otherwise create author record
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author_id = author.id

        db.session.add(article)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))
    return render_template("articles/create.html", form=form, error=error)
