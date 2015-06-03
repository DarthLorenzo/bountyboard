from flask import render_template
from flask.ext.bootstrap import Bootstrap

from app import app, db, models
from .forms import BountyForm
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    bounty_form = BountyForm()
    # if bounty_form.validate_on_submit():
    # 	return "YAY"
    bounties = models.Bounty.query.all()
    projects = models.Project.query.all()
    bounty_form.project.choices = [(p.id, p.name) for p in projects]
    return render_template('index.html', bounties=bounties, projects=projects, bounty_form=bounty_form)