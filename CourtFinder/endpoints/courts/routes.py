from flask import Blueprint, redirect, url_for

courts = Blueprint('courts', __name__)


@courts.route('/court')
def list_courts():
    return redirect(url_for('main.index'))
