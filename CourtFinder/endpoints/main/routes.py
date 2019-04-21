from flask import Blueprint, render_template, redirect, url_for

from CourtFinder import db
from CourtFinder.models.courts import Court

main = Blueprint('main', __name__)


@main.route('/')
def index():
    db.create_all()
    return render_template('index.html')


@main.app_errorhandler(401)
def redirect_login(e):
    return redirect(url_for('users.login'))


@main.app_errorhandler(403)
@main.app_errorhandler(404)
@main.app_errorhandler(405)
@main.app_errorhandler(500)
def error_404(error):
    return render_template('404.html', e=error)
