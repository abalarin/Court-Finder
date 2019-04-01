from flask import Blueprint, render_template

from CourtFinder import db
from CourtFinder.models.courts import Court

main = Blueprint('main', __name__)


@main.route('/')
def index():
    admin = Court(address='244 First Lane, Medford, NJ, 08001', name='Medford Court', lights=True, membership_required=True, description='Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur.')
    # db.create_all()

    db.session.add(admin)
    db.session.commit()
    return render_template('index.html')
