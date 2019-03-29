from flask import Blueprint, render_template
from CourtFinder.models.users import User
users = Blueprint('users', __name__)


@users.route('/profile')
def profile():
    user_name = "Narwhalian"
    user = User.query.filter_by(username=user_name)
    return render_template('users/profile.html', user=user)


@users.route('/abalarin')
def abalarin_route():
    user_name = "abalarin"
    user = User.query.filter_by(username=user_name)
    return render_template('users/profile.html', user=user)


@users.route('/mzacierka')
def mzacierka_route():
    user_name = "mzacierka"
    user = User.query.filter_by(username=user_name)
    return render_template('users/profile.html', user=user)


@users.route('/janedoe')
def janedoe_route():
    user_name = "janedoe"
    user = User.query.filter_by(username=user_name).first()
    return render_template('users/profile.html', user=user)
