from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from passlib.hash import sha256_crypt

from CourtFinder import db
from CourtFinder.models.users import User
from CourtFinder.endpoints.users.forms import RegistrationForm, UpdateProfileForm
from CourtFinder.endpoints.users.utils import user_exsists, check_username, check_email

from CourtFinder.endpoints.main.routes import *

users = Blueprint('users', __name__)


@users.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template("users/profile.html", user=current_user)
    else:
        return render_template('users/login.html')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')

    else:
        username = request.form.get('username')
        password_candidate = request.form.get('password')

        # Query for a user with the provided username
        result = User.query.filter_by(username=username).first()

        # If a user exsists and passwords match - login
        if result is not None and sha256_crypt.verify(password_candidate, result.password):

            # Init session vars
            login_user(result)
            return render_template('users/profile.html', user=result)

        else:
            flash('Incorrect Login!', 'danger')
            return render_template('users/login.html')


@users.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have logged out!', 'success')
    return redirect(url_for('main.index'))


@users.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    # Uses WTF to check if POST req and form is valid
    if form.validate_on_submit():
        # Create user object to insert into SQL
        hashed_pass = sha256_crypt.encrypt(str(form.password.data))

        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_pass)

        # Insert new user into SQL
        if user_exsists(new_user.username, new_user.email):
            flash('User already exsists!', 'danger')
            return render_template('users/register.html', form=form)
        else:
            db.session.add(new_user)
            db.session.commit()

            # Init session vars
            login_user(new_user)

            return render_template('users/profile.html', user=new_user)

    return render_template('users/register.html', form=form)


@users.route('/account/profile/update', methods=['POST'])
@login_required
def update_profile():
    user = User.query.filter_by(id=current_user.id).first()
    user.first_name = request.form.get('first_name')
    user.last_name = request.form.get('last_name')
    username = request.form.get('username')

    # Validate Username
    if not check_username(username):
        flash('Profile Updated!', 'success')
        user.username = username
    else:
        if username == user.username:
            flash('Username not changed', 'danger')
        else:
            flash('Username is taken, Username was not changed', 'danger')

    db.session.commit()
    return redirect(url_for('users.profile'))


@users.route('/account/password/update', methods=['POST'])
@login_required
def update_password():
    user = User.query.filter_by(id=current_user.id).first()
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    if sha256_crypt.verify(old_password, user.password):
        if new_password == "":
            flash('Password is not long enough!', 'danger')
        elif new_password == confirm_password:
            user.password = sha256_crypt.encrypt(str(new_password))
            flash('Password Updated!', 'success')
            db.session.commit()
        else:
            flash('Passwords dont match!', 'danger')

    else:
        flash('Old Password Incorrect!', 'danger')

    return redirect(url_for('users.profile'))


@users.route('/account/email/update', methods=['POST'])
@login_required
def update_email():
    user = User.query.filter_by(id=current_user.id).first()
    email = request.form.get('email')

    # Validate Email
    if not check_email(email):
        user.email = email
        db.session.commit()
        flash('Email was updated', 'success')
    else:
        if email == user.email:
            flash('Email was not changed', 'danger')
        else:
            flash('Email is taken, Email was not changed', 'danger')

    return redirect(url_for('users.profile'))


@users.route('/DeleteUser', methods=['GET'])
@login_required
def deleteUser():
    if request.method == 'GET':
        user = User.query.filter_by(id=current_user.id).first()
        db.session.delete(user)
        db.session.commit()
        flash('User has been deleted', 'success')
        return redirect(url_for('main.index'))
