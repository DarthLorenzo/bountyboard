from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length

class NewBountyForm(Form):

    title = StringField('Overview', validators=[DataRequired(), Length(1,64)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(0,255)])
    project = SelectField('Project', coerce=int)
    submit = SubmitField("Save Bounty")


class SortBountyForm(Form):

    sort_options = [(1, "Newest"), (2, "Oldest"), (3, "Biggest Booty")]

    sortBy = SelectField('Sort By', choices=sort_options)
    projectFilter = SelectMultipleField('Project')
    tagFilter = SelectMultipleField("Languages", choices=sort_options)


class NewTagForm(Form):

    tag = StringField('New tag', validators=[DataRequired(), Length(2,16)])
    submit = SubmitField("Add Tag")


class NewProjectForm(Form):

    name = StringField('Project Name', validators=[DataRequired(), Length(1,32)])
    description = TextAreaField('Description', validators=[Length(0,255)])
    github_url = StringField('Github Url', validators=[Length(0,128)])
    submit = SubmitField("Save Bounty")