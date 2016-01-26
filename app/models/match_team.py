from app import db


class Match_team(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    match_id = db.Column(db.Integer)

    team_id = db.Column(db.Integer)

    squad_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            match_id=self.match_id,
            team_id=self.team_id,
            squad_id=self.squad_id,
            id=self.id
        )

    def __repr__(self):
        return '<Match_team %r>' % (self.id)
