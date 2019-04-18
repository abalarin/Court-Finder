from flask import Blueprint, render_template, request
from CourtFinder.models.courts import Court
from CourtFinder.endpoints.courts.forms import CourtSearch

import json

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


@courts.route("/map")
def map_view():
    courts_query = Court.query.all()

    # This is a list comprehension - it works exactly the same as the for loop below. I went with the for loop for a better readability

    # courts = {court.id :{"name" : court.name, "latlng":{ "lat": float(court.latitude), "lng":float(court.longitude)}} for court in courts}

    courts = {}
    for court in courts_query:
        courts[court.id] = {
            "name": court.name,
            "latlng" : {
                "lat" : float(court.latitude),
                "lng" : float(court.longitude)
            }
        }
        
    return render_template('courts/map.html', courts=json.dumps(courts))
