from flask import Flask, render_template
from newspapper.views.users import users_app
from newspapper.views.articles import articles_app

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix='/users')
app.register_blueprint(articles_app, url_prefix='/articles')

@app.route("/")
def index():
    return render_template('index.html')
