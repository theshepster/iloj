from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    query = StringField('Rimiĝantaj Literoj')
    radikoj = BooleanField('Serĉu: ', default=True)
    vokalo = BooleanField('Prifajfu la lastan vokalon, kiun vi tajpis: ', default=True)
    submit = SubmitField('Rimu')