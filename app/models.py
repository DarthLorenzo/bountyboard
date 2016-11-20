from app import db
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import select, func

BOUNTY_STATUS = {
    'OPEN': 1,
    'CLOSED': 2,
    'REVIEW': 3
}


class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), unique=True)
    name          = db.Column(db.String(64))
    email         = db.Column(db.String(64), unique=True)
    img_url       = db.Column(db.String(64))
    budget        = db.Column(db.Integer)
    following     = db.relationship('Project', secondary="follows",
                        backref=db.backref("followers", lazy="dynamic"))
    watching      = db.relationship('Bounty', secondary="watches",
                        backref=db.backref("watchers", lazy="dynamic"))

    def __repr__(self):
        return '<User %r>' % (self.name)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

class Project(db.Model):
    __tablename__ = 'projects'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(32), unique=True)
    description   = db.Column(db.String(255))
    github_url    = db.Column(db.String(128), unique=True)
    # deployed_url  = db.Column(db.String(128), unique=True) //TODO
    img_url       = db.Column(db.String(64))
    bounties      = db.relationship("Bounty",
                        backref=db.backref("project"))
    tags          = db.relationship("Tag", secondary="tag_links",
                        backref=db.backref("projects", lazy="dynamic"))

    contributors  = db.relationship("User", secondary="contributors",
                        backref=db.backref("worked_on", lazy="dynamic"))

    def __repr__(self):
        return '<Project %r>' % (self.name)


class Bounty(db.Model):
    __tablename__ = 'bounties'
    id            = db.Column(db.Integer, primary_key=True)
    project_id    = db.Column(db.Integer, db.ForeignKey('projects.id'))
    title         = db.Column(db.String(64), unique=True)
    description   = db.Column(db.String(2000))
    state         = db.Column(db.Integer)
    created_at    = db.Column(db.DateTime, server_default=db.func.now())
    updated_at    = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
    comments      = db.relationship("Comment")
    pledges       = db.relationship("Pledge")
    backers       = db.relationship("User", secondary="pledges")

    @hybrid_property
    def pledge_sum(self):
        return sum(map(lambda x: x.amount, self.pledges))

    @pledge_sum.expression
    def pledge_sum(cls):
        return select([func.sum(-1 * Pledge.amount)]).where(Pledge.bounty_id == cls.id)

    def __repr__(self):
        return '<Bounty %r>' % (self.title)


class Tag(db.Model):
    __tablename__ = 'tags'
    id            = db.Column(db.Integer, primary_key=True)
    label         = db.Column(db.String(16), unique=True)

    def __repr__(self):
        return '<Tag %r >' % (self.label)


class Tag_Link(db.Model):
    __tablename__ = "tag_links"
    id            = db.Column(db.Integer, primary_key=True)
    project_id    = db.Column(db.Integer, db.ForeignKey('projects.id'))
    tag_id    	  = db.Column(db.Integer, db.ForeignKey('tags.id'))

    def __repr__(self):
        return '<Tag_Link %r -> %r>' % (self.tag_id, self.project_id)


class Follow(db.Model):
    __tablename__ = 'follows'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id    = db.Column(db.Integer, db.ForeignKey('projects.id'))

class Watches(db.Model):
    __tablename__ = 'watches'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'))
    bounty_id     = db.Column(db.Integer, db.ForeignKey('bounties.id'))

class Contributor(db.Model):
    __tablename__ = 'contributors'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'))
    project_id    = db.Column(db.Integer, db.ForeignKey('projects.id'))


class Pledge(db.Model):
    __tablename__ = 'pledges'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'))
    bounty_id     = db.Column(db.Integer, db.ForeignKey('bounties.id'))
    amount        = db.Column(db.Integer)


class Comment(db.Model):
    __tablename__ = 'comments'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'))
    bounty_id     = db.Column(db.Integer, db.ForeignKey('bounties.id'))
    text          = db.Column(db.String(2000))
    created_at    = db.Column(db.DateTime, server_default=db.func.now())
    user          = db.relationship("User")
