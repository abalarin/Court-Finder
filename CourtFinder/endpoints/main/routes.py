from flask import Blueprint, render_template

from CourtFinder import db
from CourtFinder.models.courts import Court

main = Blueprint('main', __name__)


@main.route('/')
def index():

    return render_template('index.html')
