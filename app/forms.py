from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length

class NewBountyForm(Form):

    title = StringField('Overview', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    project = SelectField('Project', coerce=int)
    submit = SubmitField("Save Bounty")


class SortBountyForm(Form):

    sort_options = [(1, "Newest"), (2, "Oldest"), (3, "Biggest Booty")]

    sortBy = SelectField('Sort By', choices=sort_options)
    projectFilter = SelectMultipleField('Project')
    tagFilter = SelectMultipleField("Languages", choices=sort_options)


class NewTagForm(Form):

    tag = StringField('New tag', validators=[DataRequired(), Length(2,15)])
    submit = SubmitField("Add Tag")