from flask import Blueprint, render_template

users = Blueprint('users', __name__)


@users.route('/profile')
def profile():
    username = "Narwhalian"
    return render_template('profile.html', name=username)
