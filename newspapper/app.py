from flask import Flask, render_template
from newspapper.views.users import users_app

app = Flask(__name__)

app.register_blueprint(users_app, url_prefix='/users')

@app.route("/")
def index():
    return render_template('index.html')
