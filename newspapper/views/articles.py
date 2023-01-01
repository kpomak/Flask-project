from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound

articles_app = Blueprint("articles_app", __name__)

ARTICLES = [
    "Flask",
    "Django",
    "FastAPI",
]


@articles_app.route("/", endpoint="list")
def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<string:title>/", endpoint="details")
@login_required
def aricle_details(title: str):
    if title in ARTICLES:
        return render_template(
            "articles/details.html",
            article_title=title,
        )
    raise NotFound(f"Article {title} doesn't exists! 😢")
