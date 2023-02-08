import os

import click
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from newspapper.admin import admin
from newspapper.models.database import db
from newspapper.views.articles import articles_app
from newspapper.views.auth import auth_app, login_manager
from newspapper.views.authors import authors_app
from newspapper.views.users import users_app
from newspapper.views.news import news_app
from newspapper.api import init_api, api_app

load_dotenv()

app = Flask(__name__)

config_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"newspapper.config.{config_name}")
openai.api_key = os.getenv("API_KEY")

admin.init_app(app)

api = init_api(app, api_app)

csrf = CSRFProtect(app)

db.init_app(app)

login_manager.init_app(app)

migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app, url_prefix="/authors")
app.register_blueprint(news_app, url_prefix="/news")
app.register_blueprint(api_app, url_prefix="/")


# @app.cli.command("init-db")
# def init_db():
#     """
#     Run in your terminal:
#     flask init-db
#     """
#     db.create_all()
#     print("done!")


@app.cli.command("create-admin")
@click.argument("username")
@click.argument("email")
def create_users(username, email):
    """
    Run in your terminal:
    flask create-admin {username} {email}
    """

    from newspapper.models import CustomUser

    admin = CustomUser(
        username=username,
        email=email,
        password=generate_password_hash(os.getenv("ADMIN_PASSWORD")),
        is_staff=True,
    )

    db.session.add(admin)
    try:
        db.session.commit()
    except IntegrityError:
        print(f"Current admin with {username=} or {email=} already exists")
    else:
        print("done! admin created")


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from newspapper.models import Tag

    tags = [
        "#flask",
        "#django",
        "#python",
        "#sqlalchemy",
        "#jasvascript",
        "#news",
    ]

    for name in tags:
        tag = Tag(name=name)
        db.session.add(tag)

    db.session.commit()
    print("created tags")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = request.form["request"]
        try:
            response = openai.Completion.create(
                prompt=prompt.capitalize(),
                engine="text-davinci-003",
                max_tokens=1024,
                temperature=0.6,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
        except Exception:
            response = None
            error = "chatGPT is busy now 💀💤\nPlease try again immediately"
        return redirect(
            url_for("index", result=(response.choices[0].text) if response else error)
        )
    result = request.args.get("result")
    if result:
        result = result.split("\n")
    return render_template("index.html", result=result)
