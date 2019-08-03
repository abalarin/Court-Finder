from CourtFinder import db
from CourtFinder.models.users import User

import datetime

# Check if username or email are already taken
def user_exsists(username, email):
    try:
        # Get all Users in SQL
        users = User.query.all()

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

    for user in users:
        if username == user.username or email == user.email:
            return True

    # No matching user
    return False


def check_username(username):

    try:
        # Get all Users in SQL
        users = User.query.all()

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

    for user in users:
        if username == user.username:
            return True

    return False


def check_email(email):

    try:
        # Get all Users in SQL
        users = User.query.all()

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

    for user in users:
        if email == user.email:
            return True

    return False


def date_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
