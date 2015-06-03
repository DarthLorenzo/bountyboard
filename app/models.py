from app import db


class User(db.Model):
    __tablename__ = 'users'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(32))
    email         = db.Column(db.String(32))
    budget        = db.Column(db.Integer)
    following     = db.relationship('Project', secondary="follows")

    def __repr__(self):
        return '<User %r>' % (self.name)


class Project(db.Model):
    __tablename__ = 'projects'
    id            = db.Column(db.Integer, primary_key=True)
    name          = db.Column(db.String(32), unique=True)
    github_url    = db.Column(db.String(32), unique=True)
    img_url       = db.Column(db.String(32))
    bounties      = db.relationship("Bounty", backref=db.backref("project"))
    tags          = db.relationship("Tag", secondary="tag_links",
                 backref=db.backref("projects", lazy="dynamic"))

    contributors  = db.relationship("User", secondary="contributors",
                 backref=db.backref("worked_on", lazy="dynamic"))

    def __repr__(self):
        return '<Project %r>' % (self.name)


class Bounty(db.Model):
    __tablename__ = 'bounties'
    id            = db.Column(db.Integer, primary_key=True)
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))
    title         = db.Column(db.String(32), unique=True)
    description   = db.Column(db.String(32))
    active        = db.Column(db.Boolean)
    created_at    = db.Column(db.DateTime)
    updated_at    = db.Column(db.DateTime)
    comments      = db.relationship("Comment")
    pledges       = db.relationship("Pledge")

    def __repr__(self):
        return '<Bounty %r>' % (self.title)


class Tag(db.Model):
    __tablename__ = 'tags'
    id            = db.Column(db.Integer, primary_key=True)
    label         = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return '<Tag %r >' % (self.label)


class Tag_Link(db.Model):
    __tablename__ = "tag_links"
    id            = db.Column(db.Integer, primary_key=True)
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))
    tag_id    	  = db.Column(db.String(32), db.ForeignKey('tags.id'))

    def __repr__(self):
        return '<Tag_Link %r -> %r>' % (self.tag_id, project_id)


class Follow(db.Model):
    __tablename__ = 'follows'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))


class Contributor(db.Model):
    __tablename__ = 'contributors'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    project_id    = db.Column(db.String(32), db.ForeignKey('projects.id'))


class Pledge(db.Model):
    __tablename__ = 'pledges'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    bounty_id     = db.Column(db.String(32), db.ForeignKey('bounties.id'))
    amount        = db.Column(db.Integer)


class Comment(db.Model):
    __tablename__ = 'comments'
    id            = db.Column(db.Integer, primary_key=True)
    user_id       = db.Column(db.String(32), db.ForeignKey('users.id'))
    bounty_id     = db.Column(db.String(32), db.ForeignKey('bounties.id'))
    text          = db.Column(db.String(32))
    created_at    = db.Column(db.DateTime)