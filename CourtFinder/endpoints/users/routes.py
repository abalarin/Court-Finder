from flask import Blueprint, render_template

users = Blueprint('users', __name__)


@users.route('/profile')
def profile():
    username = "Narwhalian"
    return render_template('profile.html', name=username)


@users.route('/abalarin')
def abalarin_route():
    username = "abalarin"
    return render_template('profile.html', name=username)
