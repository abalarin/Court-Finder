from CourtFinder import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    favorite_court = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    court_visits = db.Column(db.Integer)
    skill_level = db.Column(db.Integer)
    admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.username
