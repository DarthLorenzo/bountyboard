from flask import render_template, request, redirect, url_for, abort, flash, g, session, send_from_directory
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, models, forms, lm
import identicon
import os

from app import controller

bootstrap = Bootstrap(app)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/')
@login_required
def index():
    return redirect(url_for('bounties'))


@app.route('/login', methods=['GET', 'POST'])
def login():

    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    login_form = forms.LoginForm()

    if login_form.validate_on_submit():
        user = models.User.query.filter_by(username=login_form.data['user_name']).first()
        if user is None:
            g.loginError=True
            g.loginErrorMessage="Username not found!"
        else:
            if user.email == login_form.data['email']:
                g.user = user
                login_user(g.user)
                next = request.args.get('next') #TODO: This is not working for some reason
                next_str = str(next).replace("/", "")
                if next_str is None or next_str == '':
                    return redirect(url_for('index'))
                elif next_str not in ['bounties', 'projects']:
                    # return "<h1>Page not found %s</h1>" % next_str
                    return abort(500)
                return redirect(url_for(next_str) or url_for('bounties'))
            else:
                g.loginError=True
                g.loginErrorMessage="Email not associated with given Username"
    return render_template('login.html', login_form=login_form)


@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))


@app.route('/forgot-username', methods=['GET', 'POST'])
def forgot_username():
    forgot_username_form = forms.ForgotUsnernameForm()

    if forgot_username_form.validate_on_submit():
        user = models.User.query.filter_by(email=forgot_username_form.data['email']).first()
        if user is None:
            g.forgotUsernameError=True
            g.forgotUsernameErrorMessage="Email not registered!"
        else:
            g.forgot_username_message = "Found user"
            return render_template('login.html')

    return render_template('login.html', forgot_username_form=forgot_username_form)


@app.route('/new-user', methods=['GET', 'POST'])
def new_user():
    new_user_form = forms.NewUserForm()

    if new_user_form.validate_on_submit():
        check_email = models.User.query.filter_by(email=new_user_form.data['email']).first()
        check_username = models.User.query.filter_by(username=new_user_form.data['user_name']).first()
        if check_email is not None or check_username is not None:
            g.registrationError=True
            g.registrationErrorMessage="Username/Email already registered!"
        else:
            name = new_user_form.data['name'].replace(" ", "")
            image_url = 'users/%s.png' % name
            temp_image_url = 'app/static/users/%s.png' % name
            identicon.save_rendered_identicon(name, 24, temp_image_url)

            user = models.User(name=new_user_form.data['name'],
                               email=new_user_form.data['email'],
                               username=new_user_form.data['user_name'],
                               img_url=image_url,
                               budget=1000)
            db.session.add(user)
            db.session.commit()
            g.user = user
            login_user(user)
            return redirect(url_for('index'))

    return render_template('login.html', new_user_form=new_user_form)

@app.route('/logout', methods=['GET'])
def logout():
    g.user = None
    logout_user()
    return redirect(url_for('bounties'))

@app.route('/add-bounty', methods=[ 'POST'])
@login_required
def slap_it_on():
    slap_on_bounty_form = forms.SlapOnBountyForm()
    update_bounty = models.Bounty.query.filter_by(id=slap_on_bounty_form.data['bounty_id']).first()
    update_bounty.pledges.append(models.Pledge(user_id=g.user.id,
                                               bounty_id=slap_on_bounty_form.data['bounty_id'],
                                               amount=slap_on_bounty_form.data['bounty_addition']))
    db.session.commit()
    return redirect(url_for('bounties'))


@app.route('/bounties', methods=['GET', 'POST'])
@login_required
def bounties():
    user = g.user

    new_bounty_form = forms.NewBountyForm()
    if new_bounty_form.submit_bounty.data and new_bounty_form.validate_on_submit():
        new_bounty = models.Bounty(project_id=new_bounty_form.data['project'],
                                   title=new_bounty_form.data['title'],
                                   description=new_bounty_form.data['description'],
                                   state=models.BOUNTY_STATUS['OPEN'])
        db.session.add(new_bounty)
        new_bounty.pledges.append(models.Pledge(user_id=g.user.id,
                                                bounty_id=new_bounty.id,
                                                amount=new_bounty_form.data['bounty_amount']))
        new_bounty.comments.append(models.Comment(user_id=g.user.id,
                                                  bounty_id=new_bounty.id,
                                                  text=new_bounty_form.data['description']))
        db.session.commit()
        return redirect(url_for('bounties'))

    bounties = controller.get_bounties(sort_option=request.args.get('sort_by'))

    projects = models.Project.query.all()
    tags     = models.Tag.query.all()

    sort_bounty_form = forms.SortBountyForm()
    slap_on_bounty_form = forms.SlapOnBountyForm()

    new_bounty_form.project.choices = [(p.id, p.name) for p in projects]

    filter_bounty_form = forms.FilterBountiesForm()
    filter_bounty_form.require_tags.choices = [(t.id, t.label) for t in tags]
    filter_bounty_form.exclude_tags.choices = [(t.id, t.label) for t in tags]
    filter_bounty_form.require_projects.choices = [(p.id, p.name) for p in projects]
    filter_bounty_form.exclude_projects.choices = [(p.id, p.name) for p in projects]
    filter_bounty_form.project_filter.choices = [(p.id, p.name) for p in projects]



    if filter_bounty_form.do_filter.data and filter_bounty_form.validate_on_submit():
        bounties = models.Project.query.filter(models.Project.tags.any(models.Tag.id.in_(filter_bounty_form.data['require_tags'])))

    return render_template('bounties.html', bounties=bounties,
                                            projects=projects,
                                            tags=tags,
                                            new_bounty_form=new_bounty_form,
                                            sort_bounty_form=sort_bounty_form,
                                            filter_bounty_form=filter_bounty_form,
                                            slap_on_bounty_form=slap_on_bounty_form,
                                            user=user,
                                            offset=0)


@app.route('/more_bounties/<int:offset>', methods=['GET'])
@login_required
def more_bounties(offset):
    bounties = controller.get_bounties(offset=offset, sort_option=request.args.get('sort_by'))

    slap_on_bounty_form = forms.SlapOnBountyForm()

    return render_template('bounty_group.html', bounties=bounties,
                                                slap_on_bounty_form=slap_on_bounty_form,
                                                offset=offset)


@app.route('/bounty/<int:bounty_id>', methods=['GET', 'POST'])
@login_required
def bounty_info(bounty_id):
    bounty = models.Bounty.query.filter_by(id=bounty_id).first()

    new_comment_form = forms.NewCommentForm()

    if new_comment_form.validate_on_submit():
        new_comment = models.Comment(user_id=g.user.id,
                                     bounty_id=bounty_id,
                                     text=new_comment_form.data['new_comment'])
        db.session.add(new_comment)
        db.session.commit()
        new_comment_form = forms.NewCommentForm()

    return render_template('bounty_info.html', bounty=bounty, 
                                               bounty_statuses=models.BOUNTY_STATUS, 
                                               new_comment_form=new_comment_form)


@app.route('/projects', methods=['GET', 'POST'])
@login_required
def projects():
    projects = models.Project.query.all()
    tags = models.Tag.query.all()

    new_tag_form = forms.NewTagForm()
    remove_tag_form = forms.RemoveTagForm()
    new_project_form = forms.NewProjectForm()

    filter_projects_form = forms.FilterProjectsForm()
    filter_projects_form.require_tags.choices = [(t.id, t.label) for t in tags]
    filter_projects_form.exclude_tags.choices = [(t.id, t.label) for t in tags]

    if new_tag_form.validate_on_submit():
        tag = models.Tag.query.filter_by(label=new_tag_form.data['new_tag']).first()
        if not tag:
            tag = models.Tag(label=new_tag_form.data['new_tag'])
            db.session.add(tag)
            db.session.commit()
        new_tag_link = models.Tag_Link(tag_id=tag.id, project_id=new_tag_form.data['new_tag_project_id'])

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
        name = new_project_form.data['new_project_name'].replace(" ", "")
        image_url = 'projects/%s.png' % name
        temp_image_url = 'app/static/projects/%s.png' % name
        identicon.save_rendered_identicon(name, 24, temp_image_url)

        new_project = models.Project(name=new_project_form.data['new_project_name'],
                                     description=new_project_form.data['new_project_description'],
                                     github_url=new_project_form.data['new_project_github_url'],
                                     img_url=image_url)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('projects'))

    if filter_projects_form.validate_on_submit():
        required_tags = models.Tag.id.in_(filter_projects_form.data['require_tags'])
        projects = models.Project.query.filter(models.Project.tags.any(require_tags))

    return render_template('projects.html', projects=projects,
                                            tags=tags,
                                            new_tag_form=new_tag_form, 
                                            remove_tag_form=remove_tag_form, 
                                            new_project_form=new_project_form,
                                            filter_projects_form=filter_projects_form)


@app.route('/test')
def under_construction():
    return "<h1>Something will be here shortly!</h1>"


@app.route('/projects/<int:project_id>')
@login_required
def project_info(project_id):
    project = models.Project.query.filter_by(id=project_id).first()
    return "<h1>Project details for %s</h1>" % project.name
    # return render_template('project_info.html', project=project)



