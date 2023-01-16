from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from werkzeug.security import check_password_hash

from newspapper.models import CustomUser

auth_app = Blueprint("auth_app", __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"

__all__ = [
    "login_manager",
    "auth_app",
]


@login_manager.user_loader
def load_user(user_id):
    return CustomUser.query.filter_by(id=user_id).one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_app.login"))


@auth_app.route("/login/", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("users.user_detail", user_id=current_user.id))
        return render_template("auth/login.html")

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return render_template("auth/login.html", error="credentials are passed")
    user = CustomUser.query.filter_by(username=username).one_or_none()
    
    if not user or not check_password_hash(user.password, password):
        flash("Check your login details")
        return render_template("auth/login.html", error=f"Check username and password")
    login_user(user)
    return redirect(url_for("index"))


@auth_app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@auth_app.route("/secret/")
@login_required
def secret_view():
    return "Super secret data"
