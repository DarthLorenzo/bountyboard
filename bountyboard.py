from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

class Project(object):
    def __init__(self, name, logo_url):
        self.name = name
        self.logo_url = logo_url


class Bounty(object):
    def __init__(self, title, description, points, project):
        self.title = title
        self.description = description
        self.points = points
        self.project = project


@app.route('/')
def index():
    project = Project("bountyboard", "Rosetta.png")
    bounty = Bounty("Teach Claire to code", "blah blah blah blah, teach claire to code", 200, project)
    return render_template('index.html', bounties=[bounty])


if __name__ == '__main__':
    app.run(debug=True)
