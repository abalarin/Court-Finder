from flask import Blueprint, render_template
from flask import flash
from CourtFinder.models.courts import Court
import jfefna
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
     form = CreateCourtForm()
     if form.validate_on_submit():
         court = Court(address=form.address.data, name=form.courtname.data, total_courts=form.numcourts.data, total_visits=0, lights=form.lights.data, membership_required=form.membership.data, description=form.description.data)
         db.session.add(court)
         db.session.commit()
         flash('Court Created!', 'success')
         return render_template('/index.html')
     return render_template('create.html', title='CreateCourt', form=form, legend='Create Post')

@courts.route('/courts/<int:court_id>/update', methods=['GET', 'POST'])
def updateCourt():
    court = Court.query.get_or_404(id)
         form= CreateCourtForm()
    if form.validate_on_submit():
        court.name = form.courtname.data
        court.address = form.address.data
        court.lights = form.lights.data
        court.membership_required = form.membership.data
        court.description = form.description.data
        db.session.commit()
        flash('Your court has been updated!', 'success')
         return render_template('/index.html')
     elif request.method == 'Get':
        form.description.data = court.description
        form.courtname.data = court.name
        form.address.data = court.address
        form.lights.data = court.lights
        form.membership.data= court.membership_required
        return render_template('create_court.html', title='UpdateCourt', form=form, legend ='Update Post')
