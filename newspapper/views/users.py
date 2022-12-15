from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound
from newspapper.models import CustomUser


users_app = Blueprint('users_app', __name__)


@users_app.route('/', endpoint='list')
def users_list():
    users = CustomUser.query.all()
    return render_template('users/list.html', users=users)


@users_app.route('/<int:user_id>/', endpoint='details')
def user_detail(user_id: int):
    user = CustomUser.query.filter_by(id=user_id).one_or_none()
    if not user:
        raise NotFound(f"User {user_id} doesn't exists! 😢")
    return render_template('users/details.html', user=user)