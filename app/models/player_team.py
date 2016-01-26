from app import db


class Player_team(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    player_id = db.Column(db.Integer)

    team_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            player_id=self.player_id,
            team_id=self.team_id,
            id=self.id
        )

    def __repr__(self):
        return '<Player_team %r>' % (self.id)
