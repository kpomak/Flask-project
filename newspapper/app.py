import os

import click
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from newspapper.admin import admin
from newspapper.models.database import db
from newspapper.views.articles import articles_app
from newspapper.views.auth import auth_app, login_manager
from newspapper.views.authors import authors_app
from newspapper.views.users import users_app
from newspapper.api import init_api

load_dotenv()

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app, url_prefix="/authors")

config_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"newspapper.config.{config_name}")

admin.init_app(app)
init_api(app)
db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db, compare_type=True)


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
@click.argument("password")
@click.argument("email")
def create_users(username, password, email):
    """
    Run in your terminal:
    flask create-admin {username} {password} {email}
    """

    from newspapper.models import CustomUser

    admin = CustomUser(
        username=username,
        email=email,
        password=generate_password_hash(password),
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


@app.route("/")
def index():
    return render_template("index.html")
