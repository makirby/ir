from app import db


class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    competition_text = db.Column(db.String)

    img_location = db.Column(db.String)

    icon_location = db.Column(db.String)

    competition_type = db.Column(db.Enum('league', ' knockout', ' league-knockout', ' test-series', ' friendly'))

    created = db.Column(db.Date)

    user_created = db.Column(db.Boolean)

    season_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            name=self.name,
            competition_text=self.competition_text,
            img_location=self.img_location,
            icon_location=self.icon_location,
            competition_type=self.competition_type,
            created=self.created.isoformat(),
            user_created=self.user_created,
            season_id=self.season_id,
            id=self.id
        )

    def __repr__(self):
        return '<Competition %r>' % (self.id)
