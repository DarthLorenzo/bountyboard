from flask import render_template
from flask.ext.bootstrap import Bootstrap

from app import app, db, models
bootstrap = Bootstrap(app)

@app.route('/index')
@app.route('/')
def index():
    bounties = models.Bounty.query.all()
    projects = models.Project.query.all()
    return render_template('index.html', bounties=bounties, projects=projects)