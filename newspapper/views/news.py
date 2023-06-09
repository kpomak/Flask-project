from flask import Blueprint, render_template

from newspapper.utils.news import lenta_ru_parser


news_app = Blueprint("news_app", __name__)


@news_app.route("/", endpoint="list")
def news_list():
    news = lenta_ru_parser()
    return render_template("news/list.html", news=news)
