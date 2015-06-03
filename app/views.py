from flask import render_template, request, redirect
from flask.ext.bootstrap import Bootstrap

from app import app, db, models
from .forms import NewBountyForm, SortBountyForm
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    bounties = models.Bounty.query.all()
    projects = models.Project.query.all()

    new_bounty_form = NewBountyForm(projects)
    sort_bounty_form = SortBountyForm(projects)
    if new_bounty_form.validate_on_submit():
    	return "YAY"

    return render_template('index.html', bounties=bounties, projects=projects, new_bounty_form=new_bounty_form, sort_bounty_form=sort_bounty_form)


    