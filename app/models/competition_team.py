from app import db


class Competition_team(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    competition_id = db.Column(db.Integer)

    team_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            competition_id=self.competition_id,
            team_id=self.team_id,
            id=self.id
        )

    def __repr__(self):
        return '<Competition_team %r>' % (self.id)
