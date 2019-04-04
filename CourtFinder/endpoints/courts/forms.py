from flask_wtf import FlaskForm
from wtforms import RadioField, BooleanField, SubmitField


class CourtSearch(FlaskForm):
    type = RadioField('Type', choices=[('1', 'Public'), ('0', 'Private'), ('2', 'All')], default='2')
    distance = RadioField('Distance', choices=[('5', '5'), ('10', '10'), ('15', '15')])
    lights = BooleanField('Lights:', default="checked")
    submit = SubmitField('Submit')
