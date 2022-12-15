from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound


users_app = Blueprint('users_app', __name__)

USERS = {
    1: 'Ni!',
    2: 'Brian',
    3: 'Shruberry',
    }

@users_app.route('/', endpoint='list')
def users_list():
    return render_template('users/list.html', users=USERS)


@users_app.route('/<int:user_id>/', endpoint='details')
def user_detail(user_id: int):
    try:
        user_name = USERS[user_id]
    except KeyError:
        raise NotFound(f"User {user_id} doesn't exists! 😢")
    return render_template(
        'users/detail.html',
        user_id=user_id,
        user_name=user_name
        )