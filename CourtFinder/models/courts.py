from CourtFinder import db


class Court(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    total_courts = db.Column(db.Integer, default=1)
    total_visits = db.Column(db.Integer, default=0)
    lights = db.Column(db.Boolean)
    membership_required = db.Column(db.Boolean)
    description = db.Column(db.String(200))
    latitude = db.Column(db.Decimal(10, 8))
    longitude = db.Column(db.Decimal(11, 8))

    def __repr__(self):
        return '<Court %r>' % self.name
