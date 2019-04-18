from flask import Blueprint, render_template
from flask import flash
from CourtFinder.models.courts import Court
from flask import Blueprint, render_template, redirect, url_for, request, flash
from CourtFinder import db
#from CourtFinder.endpoints.courts.CreateCourtForm import CreateCourtForm

courts = Blueprint('courts', __name__)


@courts.route('/courts')
def list_courts():
    court = Court.query.all()
    return render_template('courts/courts.html', Courts=court)


@courts.route('/map')
def map():
    return render_template('courts/map.html')

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
         description = request.form.get('inputCourtDescription'))
         db.session.add(court)
         db.session.commit()
         #print(court.lights, court.membership_required)
         flash('Court Created!', 'success')
         return redirect(url_for('courts.list_courts'))


# @courts.route('/courts/<int:court_id>/UpdateCourt.html', methods=['GET', 'POST'])
# def updateCourt():
#     court = Court.query.get_or_404(id)
#     form= CreateCourtForm()
#     if request.method == 'POST':
#         court.name = request.form.get('inputCourtName')
#         court.address = request.form.get('inputCourtAddress')
#         court.total_courts = request.form.get('inputNumCourts')
#         court.lights = request.form.get('lightsRadios')
#         court.membership_required = request.form.get('publicprivateRadios')
#         court.description = request.form.get('inputCourtDescription')
#         db.session.commit()
#         flash('Your court has been updated!', 'success')
#         return render_template('/index.html')
#     elif request.method == 'GET':
#         request.form.get('inputCourtDescription') = court.description
#         request.form.get('inputCourtName') = court.name
#         request.form.get('inputCourtAddress') = court.address
#         request.form.get('lightsRadios') = court.lights
#         request.form.get('publicprivateRadios') = court.membership_required
#         return render_template('UpdateCourt.html')
