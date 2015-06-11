from flask import render_template, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap

from app import app, db, models, forms
import identicon
# from .forms import NewBountyForm, SortBountyForm, NewTagForm
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return redirect(url_for('bounties'))

@app.route('/bounties', methods=['GET', 'POST'])
def bounties():
    bounties = models.Bounty.query.all()
    projects = models.Project.query.all()

    new_bounty_form = forms.NewBountyForm()
    sort_bounty_form = forms.SortBountyForm()

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

@app.route('/bounties/<int:bounty_id>')
def bounty_info(bounty_id):
    bounty = models.Bounty.query.filter_by(id=bounty_id).first()
    return "Info about bounty %s" % bounty.title



@app.route('/projects', methods=['GET', 'POST'])
def projects():
    projects = models.Project.query.all()
    new_tag_form = forms.NewTagForm()
    new_project_form = forms.NewProjectForm()

    if new_tag_form.validate_on_submit():
        return "YAY"

    if new_project_form.validate_on_submit():
        name = new_project_form.data['name'].replace(" ", "")
        image_url = 'projects/%s.png' % name
        temp_image_url = 'app/static/projects/%s.png' % name
        identicon.save_rendered_identicon(name, 24, temp_image_url)

        new_project = models.Project(name=new_project_form.data['name'],
                                     description=new_project_form.data['description'],
                                     github_url=new_project_form.data['github_url'],
                                     img_url=image_url)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('projects'))

    return render_template('projects.html', projects=projects, new_tag_form=new_tag_form, new_project_form=new_project_form)



