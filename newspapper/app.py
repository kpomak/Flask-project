from flask import Flask, render_template
from newspapper.views.users import users_app
from newspapper.views.articles import articles_app
from newspapper.models.database import db


app = Flask(__name__)

app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(articles_app, url_prefix='/articles')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/newspapper.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

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
    return render_template('index.html')
