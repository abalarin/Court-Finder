from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, send_from_directory
from flask_login import login_required, current_user

from CourtFinder import db
from CourtFinder.models.courts import Court, CourtReview
from CourtFinder.models.users import User

from CourtFinder.endpoints.courts.utils import upload_images, get_images, id_validator, date_now
from CourtFinder.endpoints.courts.forms import CourtSearch, CourtCreationForm, CourtUpdateForm

import json
import uuid

courts = Blueprint("courts", __name__)


@courts.route("/courts", methods=["GET", "POST"])
def list_courts():
    form = CourtSearch()

    if request.method == "GET":
        courts = Court.query.all()

        # Get images for each listing
        for court in courts:
            court.images = get_images(court.id)

        get_images(str('3'))

        return render_template("courts/courts.html", Courts=courts, form=form)


# @courts.route("/images/<id>/<filename>")
# def get_image(id, filename):
#     return send_from_directory("static/images/courts/", id + "/" + filename)


@courts.route("/court/<id>", methods=["GET", "POST"])
def list_court(id):
    if request.method == "GET":

        court = Court.query.filter_by(id=id).first()
        court.images = get_images(court.id)
        reviews = court.reviews

        return render_template("courts/court_profile.html", Court=court, Reviews=reviews)


@courts.route("/court/<id>/review", methods=["POST"])
@login_required
def add_review(id):
    court = Court.query.filter_by(id=id).first()
    review = request.form.get("court_review")

    # Make sure theres a review typed in
    if review == '':
        flash("Please enter a review!", "danger")
        return redirect(url_for("courts.list_court", id=id))

    if len(review) > 250:
        flash("Please enter a review shorter then 250 characters", "danger")
        return redirect(url_for("courts.list_court", id=id))

    add_review = request.form.get("court_review")
    court_review = CourtReview.query.filter_by(user_id=current_user.id).filter_by(court_id=id).first()

    # If a review doesnt exsist already make a new one
    if not court_review:
        court_review = CourtReview(
            court_id=id,
            user_id=current_user.id,
            username=current_user.username,
            review=add_review,
            date=date_now()
        )
    else:
        court_review.review = add_review
        court_review.date = date_now()

    db.session.add(court_review)
    db.session.commit()

    return redirect(url_for("courts.list_court", id=id))


@courts.route("/map")
def map_view():
    courts_query = Court.query.all()
    # This is a list comprehension - it works exactly the same as the for loop below. I went with the for loop for a better readability

    # courts = {court.id :{"name" : court.name, "latlng":{ "lat": float(court.latitude), "lng":float(court.longitude)}} for court in courts}

    courts = {}
    for court in courts_query:
        courts[court.id] = {
            "name": court.name,
            "latlng": {
                "lat": float(court.latitude),
                "lng": float(court.longitude)
            }
        }

    return render_template("courts/map.html", courts=courts)


@courts.route("/create/court", methods=["GET", "POST"])
@login_required
def create_court():
    form = CourtCreationForm()
    if current_user.admin:
        if form.validate_on_submit():
            # Make a unique listing ID
            uid = str(id_validator(uuid.uuid4()))

            court = Court(
                uid=uid,
                address=form.address.data,
                name=form.title.data,
                total_courts=form.court_count.data,
                total_visits=0,
                lights=int(form.lights.data),
                membership_required=int(form.status.data),
                description=form.description.data,
                latitude=form.latitude.data,
                longitude=form.longitude.data)

            db.session.add(court)
            db.session.commit()

            # Upload Images
            court = Court.query.filter_by(uid=uid).first()
            upload_images(request.files.getlist("court_images"), court.id)

            flash("Court Created!", "success")
            return redirect(url_for("courts.list_courts"))
        else:
            return render_template("courts/create_court.html", form=form)
    else:
        return redirect(url_for("main.index"))


@courts.route("/update/court/<id>", methods=["GET", "POST"])
def update_court(id):
    form = CourtUpdateForm()
    if current_user.admin:
        if form.validate_on_submit():
            court = Court.query.filter_by(id=id).first()

            court.adress = form.address.data
            court.name = form.title.data
            court.total_courts = form.court_count.data
            court.total_visits = 0
            court.lights = int(form.lights.data)
            court.membership_required = int(form.status.data)
            court.description = form.description.data
            court.latitude = form.latitude.data
            court.longitude = form.longitude.data

            # Upload Images
            upload_images(request.files.getlist("court_images"), id)

            db.session.commit()
            flash("Your court has been updated!", "success")
            return redirect(url_for("courts.list_courts"))

        else:
            court = Court.query.filter_by(id=id).first()
            form.description.data = court.description
            return render_template("courts/update_court.html", court=court, form=form)
    else:
        return redirect(url_for("main.index"))


@courts.route("/delete/court/<id>", methods=["GET"])
def delete_court(id):

    if current_user.admin:
        if request.method == "GET":
            court = Court.query.filter_by(id=id).first()
            db.session.delete(court)
            db.session.commit()

            flash("Court has been deleted", "success")
            return redirect(url_for("courts.list_courts"))
    else:
        return redirect(url_for("courts.list_courts"))
