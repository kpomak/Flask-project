from flask import Blueprint, current_app, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from newspapper.forms.article import CreateArticleForm
from newspapper.models import Article, Author, Tag
from newspapper.models.database import db
from newspapper.utils import get_articles_by_api


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
    articles = get_articles_by_api()
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
