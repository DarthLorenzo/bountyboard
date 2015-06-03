from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired

class NewBountyForm(Form):

	def __init__(self, projects):

		project_options = [(p.id, p.name) for p in projects]

		title = StringField('Overview', validators=[DataRequired()])
		description = TextAreaField('Description', validators=[DataRequired()])
		project = SelectField('Project', choices=project_options, validators=[DataRequired()])
		
		Form.__init__(self)



class SortBountyForm(Form):

	def __init__(self, projects):

		project_options = [(p.id, p.name) for p in projects]
		sort_options = [(1, "Newest"), (2, "Oldest"), (3, "Biggest Booty")]

		sortBy = SelectField('Sort By', choices=sort_options)
		projectFilter = SelectMultipleField('Project', choices=project_options)
		tagFilter = SelectMultipleField("Languages", choices=sort_options)
		
		Form.__init__(self)