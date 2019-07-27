from CourtFinder import db, ma, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    court_visits = db.Column(db.Integer)
    skill_level = db.Column(db.Integer)
    admin = db.Column(db.Boolean, default=False)
    friend_count = db.Column(db.Integer)
    join_date = db.Column(db.DateTime, nullable=False)

    favorite_court = db.Column(db.Integer, db.ForeignKey('court.id'))

    reviews = db.relationship('CourtReview', backref='user', lazy=True)

    # Friend Request relationships
    friend_requests = db.relationship('Friendship', foreign_keys='Friendship.requester_id', backref='requester', lazy=True)
    friends_requested = db.relationship('Friendship', foreign_keys='Friendship.requested_id', backref='requested', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    requested_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Boolean, default=None)
    date = db.Column(db.DateTime, nullable=False)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("first_name", "last_name", "username", "password", "email", "height", "weight", "court_visits", "skill_level", "admin", "friend_count")


class FriendshipSchema(ma.Schema):
    class Meta:
        fields = ("requester_id", "requester_id", "status")
