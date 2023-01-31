from flask import Blueprint, render_template
from newspapper.utils import get_articles_count

from newspapper.models import Author

authors_app = Blueprint("authors_app", __name__)


@authors_app.route("/", endpoint="list")
def authors_list():
    authors = Author.query.all()
    for author in authors:
        author.articles_count = get_articles_count(author.id)
    return render_template("authors/list.html", authors=authors)
