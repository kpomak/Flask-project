from flask import Flask


app = Flask(__name__)

@app.route("/<name>")
def index(name: str):
    return f"Flask web-application '{name}'"

