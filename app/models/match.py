from app import db


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    competition_id = db.Column(db.Integer)

    home_match_team_id = db.Column(db.Integer)

    away_match_team_id = db.Column(db.Integer)

    match_text = db.Column(db.String)

    ground_id = db.Column(db.Integer)

    home_score = db.Column(db.Integer)

    away_score = db.Column(db.Integer)

    img_location = db.Column(db.String)

    match_date = db.Column(db.Date)

    match_outcome = db.Column(db.Enum('home_win', ' away_win', ' draw', ' postponed', ' cancelled', ' rescheduled'))

    match_type = db.Column(
        db.Enum('league', ' last32', ' last16', ' quarter_finals', ' semi_finals', ' final', ' bronze_final',
                ' friendly', ' exhibition', ' test'))

    def to_dict(self):
        return dict(
            competition_id=self.competition_id,
            home_match_team_id=self.home_match_team_id,
            away_match_team_id=self.away_match_team_id,
            match_text=self.match_text,
            ground_id=self.ground_id,
            home_score=self.home_score,
            away_score=self.away_score,
            img_location=self.img_location,
            match_date=self.match_date.isoformat(),
            match_outcome=self.match_outcome,
            match_type=self.match_type,
            id=self.id
        )

    def __repr__(self):
        return '<Match %r>' % (self.id)
