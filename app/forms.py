from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class BountyForm(Form):
    title = StringField('Overview', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    project = SelectField('Project', validators=[DataRequired()])