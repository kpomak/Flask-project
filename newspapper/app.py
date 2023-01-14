import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_migrate import Migrate

from newspapper.models.database import db
from newspapper.views.articles import articles_app
from newspapper.views.auth import auth_app, login_manager
from newspapper.views.users import users_app

load_dotenv()

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")

config_name = os.environ.get("CONFIG_NAME") or "ProductionConfig"
app.config.from_object(f"newspapper.config.{config_name}")

db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.cli.command("init-db")
def init_db():
    """
    Run in your terminal:
    flask init-db
    """
    db.create_all()
    print("done!")


@app.cli.command("create-users")
def create_users():
    """
    Run in your terminal:
    flask create-users
    > done! created users: <User #1 'admin'> <User #2 'james'>
    """
    from newspapper.models import CustomUser

    admin = CustomUser(username="admin", is_staff=True)
    user = CustomUser(username="user")
    db.session.add(admin)
    db.session.add(user)
    db.session.commit()
    print("done! created users:", admin, user)


@app.route("/")
def index():
    return render_template("index.html")
