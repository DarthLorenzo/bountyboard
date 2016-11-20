from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length

from app import controller


class NewBountyForm(Form):
    title = StringField('Overview', validators=[DataRequired(), Length(1, 64)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(0, 2000)])
    project = SelectField('Project', coerce=int)
    bounty_amount = IntegerField('Bounty Offered', validators=[DataRequired()])
    submit_bounty = SubmitField("Save Bounty")


class SlapOnBountyForm(Form):
    bounty_addition = IntegerField('Bounty Offered', validators=[DataRequired()])
    bounty_id = IntegerField('Bounty ID', validators=[DataRequired(), Length(2, 16)])
    slap_on_bounty = SubmitField("Slap It On")


class SortBountyForm(Form):
    sort_options = [(k, v['label']) for k, v, in controller.sort_options_dict.items()]
    sort_by = SelectField('Sort By', choices=sort_options)


class NewTagForm(Form):
    new_tag = StringField('New tag', validators=[DataRequired(), Length(2, 16)])
    new_tag_project_id = IntegerField(validators=[DataRequired()])
    submit_new_tag = SubmitField("Add Tag")


class RemoveTagForm(Form):
    remove_tag = StringField(validators=[DataRequired()])
    remove_tag_project = StringField(validators=[DataRequired()])
    submit_remove_tag = SubmitField("Remove Tag")


class NewProjectForm(Form):
    new_project_name = StringField('Project Name', validators=[DataRequired(), Length(1, 32)])
    new_project_description = TextAreaField('Description', validators=[Length(0, 255)])
    new_project_github_url = StringField('Github Url', validators=[Length(0, 128)])
    submit_project = SubmitField("Save Project")


class FilterProjectsForm(Form):
    require_tags = SelectMultipleField(coerce=int)
    exclude_tags = SelectMultipleField(coerce=int)
    do_filter = SubmitField("Filter by Tags")


class FilterBountiesForm(Form):
    require_projects = SelectMultipleField(coerce=int)
    exclude_projects = SelectMultipleField(coerce=int)
    require_tags = SelectMultipleField(coerce=int)
    exclude_tags = SelectMultipleField(coerce=int)
    project_filter = SelectMultipleField('Project')
    tag_filter = SelectMultipleField("Languages")
    do_filter = SubmitField("Filter Bounties")


class NewCommentForm(Form):
    new_comment = TextAreaField('New Comment', validators=[DataRequired(), Length(0, 2000)])
    submit_new_comment = SubmitField("Add Comment")


class NewUserForm(Form):
    name = StringField('Full Name', validators=[DataRequired(), Length(1, 64)])
    user_name = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email', validators=[DataRequired(), Length(0, 128)])
    register_user = SubmitField("Register")


class ForgotUsnernameForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(1,64)])
    find_username = SubmitField("Find Username")
    

class LoginForm(Form):
    user_name = StringField('Username', validators=[DataRequired(), Length(0, 64)])
    email = StringField('Email', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    do_login = SubmitField("Login")