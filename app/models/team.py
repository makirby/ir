from app import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)

    img_location = db.Column(db.String)

    icon_location = db.Column(db.String)

    team_text = db.Column(db.String)

    ground_id = db.Column(db.Integer)

    team_type = db.Column(
        db.Enum('domestic', ' international', ' sevens-domestic', ' sevens-international', ' exhibition', ' other'))

    established = db.Column(db.Date)

    season_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            name=self.name,
            img_location=self.img_location,
            icon_location=self.icon_location,
            team_text=self.team_text,
            ground_id=self.ground_id,
            team_type=self.team_type,
            established=self.established.isoformat(),
            season_id=self.season_id,
            id=self.id
        )

    def __repr__(self):
        return '<Team %r>' % (self.id)
