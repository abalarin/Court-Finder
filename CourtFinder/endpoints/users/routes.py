from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from passlib.hash import sha256_crypt

from CourtFinder import db
from CourtFinder.models.users import User
from CourtFinder.endpoints.users.forms import RegistrationForm
from CourtFinder.endpoints.users.utils import user_exsists, check_username, check_email

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
<<<<<<< HEAD


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
    if reguest.form.get('inputPassword') == None and request.form.get('inputConfirmPassword') == None:
        flash('Password was not changed', 'danger')
    elif request.form.get('inputPassword') == request.form.get('inputConfirmPassword'):
        hashed_pass = sha256_crypt.encrypt(str(request.form.get('inputPassword')))
        user.password= hashed_pass
        db.session.commit()
    else:
        flash('Passwords dont match', 'danger')

        if not check_username(request.form.get('inputUserName')):
            user.username=request.form.get('inputUserName')
            db.session.commit()
        else:
            flash('Username was taken, Username was not changed', 'danger')
        if not check_email(request.form.get('inputEmail')):
            user.email = request.form.get('inputEmail')
            db.session.commit()
        else:
            flash('Email was taken, Email was not changed', 'danger')
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



=======
>>>>>>> 61f61d4034176a40a003c2c14faec34b8651ec51
