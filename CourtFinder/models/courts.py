from CourtFinder import db, ma


class Court(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(255), unique=True, nullable=False)
    address = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    total_courts = db.Column(db.Integer, default=1)
    total_visits = db.Column(db.Integer, default=0)
    lights = db.Column(db.Boolean)
    membership_required = db.Column(db.Boolean)
    description = db.Column(db.String(200))
    latitude = db.Column(db.Numeric(10, 8))
    longitude = db.Column(db.Numeric(11, 8))

    # One to Many relationships
    reviews = db.relationship('CourtReview', backref='court', lazy=True)
    user_favorite = db.relationship('User', backref='court', lazy=True)
    court_photos = db.relationship('CourtPhoto', backref='court', lazy=True)

    def __repr__(self):
        return '<Court %r>' % self.name


class CourtReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    court_id = db.Column(db.Integer, db.ForeignKey('court.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(40))
    raiting = db.Column(db.Integer)
    review = db.Column(db.String(250))
    date = db.Column(db.DateTime, nullable=False)


class CourtSchema(ma.Schema):
    class Meta:
        fields = ("uid", "address", "name", "total_courts", "total_visits", "lights", "membership_required", "description", "latitude", "longitude")


class CourtReviewSchema(ma.Schema):
    class Meta:
        fields = ("court_id", "user_id", "username", "raiting", "review")
