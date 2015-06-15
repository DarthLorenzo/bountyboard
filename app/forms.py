from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

class NewBountyForm(Form):

    title = StringField('Overview', validators=[DataRequired(), Length(1,64)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(0,255)])
    project = SelectField('Project', coerce=int)
    submit_bounty = SubmitField("Save Bounty")


class SortBountyForm(Form):

    sort_options = [(1, "Newest"), (2, "Oldest"), (3, "Biggest Booty")]

    sort_by = SelectField('Sort By', choices=sort_options)
    project_filter = SelectMultipleField('Project')
    tag_filter = SelectMultipleField("Languages", choices=sort_options)


class NewTagForm(Form):

    new_tag = StringField('New tag', validators=[DataRequired(), Length(2,16)])
    new_tag_project_id = IntegerField(validators=[DataRequired()])
    submit_new_tag = SubmitField("Add Tag")

class RemoveTagForm(Form):

    remove_tag = StringField(validators=[DataRequired()])
    remove_tag_project = StringField(validators=[DataRequired()])
    submit_remove_tag = SubmitField("Remove Tag")


class NewProjectForm(Form):

    name = StringField('Project Name', validators=[DataRequired(), Length(1,32)])
    description = TextAreaField('Description', validators=[Length(0,255)])
    github_url = StringField('Github Url', validators=[Length(0,128)])
    submit_project = SubmitField("Save Bounty")

class FilterTagsForm(Form):

    require_tags = SelectMultipleField(coerce=int)
    exclude_tags = SelectMultipleField(coerce=int)
    do_filter = SubmitField("Filter by Tags")