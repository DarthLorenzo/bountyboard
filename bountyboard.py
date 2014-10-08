from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "herpderp"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.sqlite3"
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Interger, primary_key=True)
    name          = db.Column(db.String(32)
    email         = db.Column(db.String(32)
    budget        = db.Column(db.Interger)
    following     = db.relationship('Follow', secondary="follows")


class Project(db.Model):
    __tablename__ = 'projects'
    id            = db.Column(db.Interger, primary_key=True)
    name          = db.Column(db.String(32), unique=True)
    github_url    = db.Column(db.String(32), unique=True)
    img_url       = db.Column(db.String(32))
    bounties      = db.relationship("Bounty")
    tags          = db.relationship("Tag", secondary="tag_links",
                 backref=db.backref("projects", lazy="dynamic"))

    contributors  = db.relationship("Contributor", secondary="contributors",
                 backref=db.backref("worked_on", lazy="dynamic"))


class Bounty(db.Model):
    __tablename__ = 'bounties'
    id            = db.Column(db.Interger, primary_key=True)
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))
    title         = db.Column(db.String(32), unique=True)
    description   = db.Column(db.String(32))
    active        = db.Column(db.Boolean)
    created_at    = db.Column(db.DateTime)
    updated_at    = db.Column(db.DateTime)
    comments      = db.relationship("Comment")
    pledges       = db.relationship("Pledge")


class Tag(db.Model):
    __tablename__ = 'tags'
    id            = db.Column(db.Interger, primary_key=True)
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))
    label         = db.Column(db.String(32), unique=True)


class Tag_Link(db.Model):
    __tablename__ = "tag_links"
    id            = db.Column(db.Interger, primary_key=True)
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))
    tag_id    = db.Column(db.String(32), db.ForeignKey('tag.id'))


class Follow(db.Model):
    __tablename__ = 'follows'
    id            = db.Column(db.Interger, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))


class Contributor(db.Model):
    __tablename__ = 'contributors'
    id            = db.Column(db.Interger, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))


class Pledge(db.Model):
    __tablename__ = 'pledges'
    id            = db.Column(db.Interger, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    bounty_id     = db.Column(db.String(32), db.ForeignKey('bounties.id'))
    amount        = db.Column(db.Interger)


class Comment(db.Model):
    __tablename__ = 'comments'
    id            = db.Column(db.Interger, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    bounty_id     = db.Column(db.String(32), db.ForeignKey('bounties.id'))
    text          = db.Column(db.String(32))
    created_at    = db.Column(db.DateTime)


@app.route('/')
def index():
    project = Project("bountyboard", "Rosetta.png")
    bounty = Bounty("Teach Claire to code", "blah blah blah blah, teach claire to code", 200, project)
    return render_template('index.html', bounties=[bounty])


if __name__ == '__main__':
    app.run(debug=True)
