from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length

class CreateCourtForm(FlaskForm):
    courtname = StringField('Courtname', validators=[DataRequired(), Length(min=2, max=40)])
    address = StringField('Address', validators=[DataRequired(), Length(min=10, max=120)])
    membership = BooleanField('Membership required?', validators=[DataRequired()]
    lights = BooleanField('lights', validators=[DataRequired()]
    numcourts = IntegerField('Number of Courts', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Create')
