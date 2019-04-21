from flask import Blueprint, render_template, redirect, url_for, request, flash
from CourtFinder import db
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

@courts.route('/CreateCourt', methods=['GET', 'POST'])
def createCourt():
     if request.method == 'GET':
         return render_template('courts/CreateCourt.html')
     elif request.method == 'POST':
         court = Court(
         address=request.form.get('inputCourtAddress'),
         name=request.form.get('inputCourtName'),
         total_courts=request.form.get('inputNumCourts'),
         total_visits=0,
         lights=int(request.form.get('lightsRadios')),
         membership_required =int(request.form.get('publicprivateRadios')),
         description = request.form.get('inputCourtDescription'),
         latitude = request.form.get('xCoordCourt'),
         longitude = request.form.get('yCoordCourt'))
         db.session.add(court)
         db.session.commit()
         #print(court.lights, court.membership_required)
         flash('Court Created!', 'success')
         return redirect(url_for('courts.list_courts'))


@courts.route('/UpdateCourt/<id>', methods=['GET', 'POST'])
def updateCourt(id):
    if request.method == 'POST':
        court = Court.query.filter_by(id=id).first()
        print("hey")
        print(request.form.get('xCoordCourt'), request.form.get('yCoordCourt'))
        court.adress=request.form.get('inputCourtAddress')
        court.name = request.form.get('inputCourtName')
        court.total_courts = request.form.get('inputNumCourts')
        court.total_visits = 0
        court.lights = int(request.form.get('lightsRadios'))
        court.membership_required= int(request.form.get('publicprivateRadios'))
        court.description = request.form.get('inputCourtDescription')
        court.latitude = request.form.get('xCoordCourt')
        court.longitude = request.form.get('yCoordCourt')
        print(court.latitude, court.longitude)
        db.session.commit()
        flash('Your court has been updated!', 'success')
        return redirect(url_for('courts.list_courts'))
    elif request.method == 'GET':
        print("hey get")
        court = Court.query.filter_by(id=id).first()
        print(court, id, "test get")
        return render_template('courts/UpdateCourt.html', court=court)

@courts.route('/DeleteCourt/<id>', methods=['GET'])
def deleteCourt(id):
    if request.method == 'GET':
        court = Court.query.filter_by(id=id).first()
        print(court.id)
        db.session.delete(court)
        db.session.commit()
        flash('Court has been deleted', 'success')
        return redirect(url_for('courts.list_courts'))
