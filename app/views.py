from flask import render_template, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap

from app import app, db, models
from .forms import NewBountyForm, SortBountyForm, NewTagForm
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return redirect(url_for('bounties'))

@app.route('/bounties', methods=['GET', 'POST'])
def bounties():
    bounties = models.Bounty.query.all()
    projects = models.Project.query.all()

    new_bounty_form = NewBountyForm()
    sort_bounty_form = SortBountyForm()

    new_bounty_form.project.choices = [(p.id, p.name) for p in projects]
    sort_bounty_form.projectFilter.choices = [(p.id, p.name) for p in projects]

    if new_bounty_form.validate_on_submit():
        new_bounty = models.Bounty(project_id=new_bounty_form.data['project'],
                                   title=new_bounty_form.data['title'],
                                   description=new_bounty_form.data['description'],
                                   active=True)
        db.session.add(new_bounty)
        db.session.commit()
        return redirect(url_for('bounties'))

    return render_template('bounties.html', bounties=bounties, projects=projects, new_bounty_form=new_bounty_form, sort_bounty_form=sort_bounty_form)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    projects = models.Project.query.all()
    new_tag_form = NewTagForm()

    if new_tag_form.validate_on_submit():
        return "YAY"

    return render_template('projects.html', projects=projects, new_tag_form=new_tag_form)



