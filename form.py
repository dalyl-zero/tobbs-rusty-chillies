from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class ChilliForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    scoville = IntegerField('Scoville', validators=[DataRequired(), NumberRange(min=0)])
    days_to_germinate = IntegerField('Days to germinate', validators=[DataRequired(), NumberRange(min=0)])
    create = SubmitField('Create')
