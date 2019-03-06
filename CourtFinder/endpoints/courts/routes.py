from flask import Blueprint, render_template

courts = Blueprint('courts', __name__)


@courts.route('/courts')
def list_courts():
    return render_template('courts.html')
