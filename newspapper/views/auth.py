from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from newspapper.forms.user import RegistrationForm
from newspapper.models import CustomUser
from newspapper.models.database import db

auth_app = Blueprint("auth_app", __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_app.login"

__all__ = [
    "login_manager",
    "auth_app",
]


@auth_app.route("/register/", methods=["GET", "POST"], endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    error = None
    form = RegistrationForm(request.form)

    if request.method == "POST" and form.validate_on_submit():
        if CustomUser.query.filter_by(username=form.username.data).count():
            form.username.errors.append("username already exists!")
            return render_template("auth/register.html", form=form)

        if CustomUser.query.filter_by(email=form.email.data).count():
            form.email.errors.append("email already exists!")
            return render_template("auth/register.html", form=form)

        user = CustomUser(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            password=form.password.data,
            email=form.email.data,
            is_staff=False,
        )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create user!")
            error = "Could not create user!"
        else:
            current_app.logger.info(f"Created user {user}")
            login_user(user)
            return redirect(url_for("index"))
    return render_template("auth/register.html", form=form, error=error)


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
