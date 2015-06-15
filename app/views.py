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
    sort_bounty_form.project_filter.choices = [(p.id, p.name) for p in projects]

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
    return render_template('bounty_info.html', bounty=bounty)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    projects = models.Project.query.all()
    tags = models.Tag.query.all()

    new_tag_form = forms.NewTagForm()
    remove_tag_form = forms.RemoveTagForm()
    new_project_form = forms.NewProjectForm()

    filter_tags_form = forms.FilterTagsForm()
    filter_tags_form.require_tags.choices = [(t.id, t.label) for t in tags]
    filter_tags_form.exclude_tags.choices = [(t.id, t.label) for t in tags]

    if new_tag_form.validate_on_submit():
        tag = models.Tag.query.filter_by(label=new_tag_form.data['new_tag']).first()
        if not tag:
            tag = models.Tag(label=new_tag_form.data['new_tag'])
            db.session.add(tag)
            db.session.commit()
        new_tag_link = models.Tag_Link(tag_id=tag.id, project_id=new_tag_form.data['project_id'])

        db.session.add(new_tag_link)
        db.session.commit()
        return redirect(url_for('projects'))

    if remove_tag_form.validate_on_submit():
        tag = models.Tag.query.filter_by(label=remove_tag_form.data['remove_tag']).first()
        project = models.Project.query.filter_by(name=remove_tag_form.data['remove_tag_project']).first()
        tag_link = models.Tag_Link.query.filter_by(tag_id=tag.id, project_id=project.id).first()
        db.session.delete(tag_link)
        db.session.commit()
        return redirect(url_for('projects'))


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

    if filter_tags_form.validate_on_submit():
        projects = models.Project.query.filter(models.Project.tags.any(models.Tag.id.in_(filter_tags_form.data['require_tags'])))

    return render_template('projects.html', projects=projects, tags=tags,
                                            new_tag_form=new_tag_form, 
                                            remove_tag_form=remove_tag_form, 
                                            new_project_form=new_project_form,
                                            filter_tags_form=filter_tags_form)

@app.route('/projects/<int:project_id>')
def project_info(project_id):
    project = models.Project.query.filter_by(id=project_id).first()
    return "<h1>Project details for %s</h1>" % project.name
    # return render_template('project_info.html', project=project)



