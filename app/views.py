from flask import render_template
from flask.ext.bootstrap import Bootstrap

from app import app, db, models
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # Project("bountyboard", "Rosetta.png")
    # bounty = Bounty("Teach Claire to code", "blah blah blah blah, teach claire to code", 200, project)
    bounties = models.Bounty.query.all()
    return render_template('index.html', bounties=bounties)