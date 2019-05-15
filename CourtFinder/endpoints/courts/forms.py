from flask_wtf import FlaskForm
from wtforms import RadioField, BooleanField, SubmitField, StringField, TextAreaField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length


class CourtSearch(FlaskForm):
    type = RadioField('Type', choices=[('1', 'Public'), ('0', 'Private'), ('2', 'All')], default='2')
    distance = RadioField('Distance', choices=[('5', '5'), ('10', '10'), ('15', '15')])
    lights = BooleanField('Lights:', default="checked")
    submit = SubmitField('Submit')


class CourtCreationForm(FlaskForm):
    """docstring for CourtCreationForm."""

    title = StringField('Court Name', validators=[DataRequired(), Length(min=2, max=40)])
    address = StringField('Court Address', validators=[DataRequired()])
    latitude = StringField('Latitude', validators=[DataRequired()])
    longitude = StringField('Longitude', validators=[DataRequired()])
    court_count = IntegerField('Number of Courts', validators=[DataRequired()])
    description = TextAreaField('Court Description', validators=[DataRequired(), Length(max=200)])
    status = RadioField('Court Status', choices=[('1', 'Private'), ('0', 'Public')], validators=[DataRequired()])
    lights = RadioField('Lights', choices=[('1','Lights'),('0','No Lights')], validators=[DataRequired()])
    submit = SubmitField('Create Court')
