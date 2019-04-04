from flask import Blueprint, render_template, request
from CourtFinder.models.courts import Court
from CourtFinder.endpoints.courts.forms import CourtSearch
courts = Blueprint('courts', __name__)


@courts.route('/courts', methods=['GET', 'POST'])
def list_courts():
    form = CourtSearch()

    if request.method == 'GET':
        court = Court.query.all()
        return render_template('courts/courts.html', Courts=court, form=form)
    else:
        tpe = form.type.data
        dist = form.distance.data
        lght = form.lights.data
        print(" Type: " + tpe + " dist: " + dist)
        court = Court.query.filter((Court.lights == lght) & (Court.membership_required == tpe)).all()
        return render_template('courts/courts.html', Courts=court, form=form)


