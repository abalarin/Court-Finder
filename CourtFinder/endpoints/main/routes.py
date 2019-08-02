from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user
from passlib.hash import sha256_crypt
import datetime

from CourtFinder import db
from CourtFinder.endpoints.users.forms import RegistrationForm
from CourtFinder.models.users import User
from CourtFinder.endpoints.users.utils import user_exsists, date_now


main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()

    mobile_check = request.user_agent.platform
    if mobile_check == 'iphone' or mobile_check == 'android':
        return redirect("https://m.findthecourt.com/")

    if form.validate_on_submit():
        # Create user object to insert into SQL
        hashed_pass = sha256_crypt.encrypt(str(form.password.data))

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_pass,
            join_date=date_now()
        )

        # Insert new user into SQL
        if user_exsists(new_user.username, new_user.email):
            flash('User already exsists!', 'danger')
            return render_template('index.html', form=form)
        else:
            try:
                db.session.add(new_user)
                db.session.commit()

                # Init session vars
                login_user(new_user)
            except Exception as e:
                flash('There was an issue, plz try again!', 'danger')
                # Clear any in-progress sqlalchemy transactions
                try:
                    db.session.rollback()
                except:
                    pass
                try:
                    db.session.remove()
                except:
                    pass

            return render_template('users/profile.html', user=new_user)

    # -- is a GET request --
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))
    else:
        return render_template('index.html', form=form)


@main.route('/alpha', methods=['GET', 'POST'])
def alpha():
    return render_template('errors/alpha.html')


@main.app_errorhandler(401)
def redirect_login(e):
    return redirect(url_for('users.login'))


@main.app_errorhandler(403)
@main.app_errorhandler(404)
@main.app_errorhandler(405)
@main.app_errorhandler(500)
def error_404(error):
    return render_template('errors/404.html', e=error)
