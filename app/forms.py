from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Rimiĝantaj Literoj', validators=[DataRequired()])
    submit = SubmitField('Rimu')