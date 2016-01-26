from app import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    event_type = db.Column(
        db.Enum('try', 'conversion', 'penalty', 'missed_conversion', 'missed_penalty', 'drop_goal', 'missed_drop_goal',
                'yellow_card', 'red_card', 'replacement', 'blood_replacment'))

    minute = db.Column(db.Integer)

    player_id = db.Column(db.Integer)

    match_team_id = db.Column(db.Integer)

    event_text = db.Column(db.String)

    def to_dict(self):
        return dict(
            event_type=self.event_type,
            minute=self.minute,
            player_id=self.player_id,
            match_team_id=self.match_team_id,
            event_text=self.event_text,
            id=self.id
        )

    def __repr__(self):
        return '<Event %r>' % (self.id)
