from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Rimiĝantaj Literoj')
    radikoj = BooleanField('', default=True)
    submit = SubmitField('Rimu')