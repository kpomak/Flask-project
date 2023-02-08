from flask import Blueprint, render_template


news_app = Blueprint("news_app", __name__)


@news_app.route("/", endpoint="list")
def news_list():
    news = [{"title": "заголовок", "body": "статья"}]
    return render_template("news/list.html", news=news)
