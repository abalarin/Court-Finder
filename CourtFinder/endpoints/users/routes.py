from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from passlib.hash import sha256_crypt

from CourtFinder import db
from CourtFinder.models.users import User
from CourtFinder.endpoints.users.forms import RegistrationForm

users = Blueprint('users', __name__)


@users.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template("users/profile.html", user=current_user)
    else:
        print(current_user)
        return render_template('users/login.html')


@users.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('users/login.html')

    else:
        email = request.form.get('email')
        password_candidate = request.form.get('password')

        # Query for a user with the provided username
        result = User.query.filter_by(email=email).first()

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


@users.route('/UpdateProfile/<id>', methods=['GET','POST'])
def updateProfile(id):
    if request.method == 'POST':
        user = User.query.filter_by(id=id).first()
        user.first_name = request.form.get('inputFirstName')
        user.last_name = request.form.get('inputLastName')
        user.favorite_court = request.form.get('inputFavoriteCourt')
        user.height = request.form.get('inputHeight')
        user.weight = request.form.get('inputWeight')
        user.skill_level = request.form.get('inputSkillLevel')
        db.session.commit()
        if request.form.get('inputPassword') == None:
            flash('Password wasnt changed', 'danger')
        if request.form.get('inputPassword') == request.form.get('inputConfirmPassword'):
            user.password = request.form.get('inputPassword')
            db.session.commit()
        else:
            flash('Passwords dont match', 'danger')

        if not check_username(request.form.get('inputUserName')):
            user.username=request.form.get('inputUserName')
            db.session.commit()
        if not check_email(request.form.get('inputEmail')):
            user.email = request.form.get('inputEmail')
            db.session.commit()
        flash('Profile has been updated!', 'success')
        return render_template('users/profile.html', user=user)

    elif request.method == 'GET':
        user = User.query.filter_by(id=id).first()
        return render_template('users/UpdateProfile.html', user=user)

@users.route('/DeleteUser/<id>', methods=['GET'])
def deleteUser(id):
    if request.method == 'GET':
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        flash('User has been deleted', 'success')
        return render_template('/index.html')


# Check if username or email are already taken


def user_exsists(username, email):
    # Get all Users in SQL
    users = User.query.all()
    for user in users:
        if username == user.username or email == user.email:
            return True

    # No matching user
    return False


def check_username(username):
    users=User.query.all()
    for user in users:
        if username == user.username:
            return True

    return False


def check_email(email):
    users=User.query.all()
    for user in users:
        if email == user.email:
            return True

    return False
