from app import db


class Squad(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    tighthead_id = db.Column(db.Integer)

    loosehead_id = db.Column(db.Integer)

    hooker_id = db.Column(db.Integer)

    lock_4_id = db.Column(db.Integer)

    lock_5_id = db.Column(db.Integer)

    flanker_6_id = db.Column(db.Integer)

    flanker_7_id = db.Column(db.Integer)

    number_8_id = db.Column(db.Integer)

    scrum_half_id = db.Column(db.Integer)

    fly_half_id = db.Column(db.Integer)

    wing_11_id = db.Column(db.Integer)

    inside_centre_id = db.Column(db.Integer)

    outside_centre_id = db.Column(db.Integer)

    wing_14_id = db.Column(db.Integer)

    full_back_id = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            tighthead_id=self.tighthead_id,
            loosehead_id=self.loosehead_id,
            hooker_id=self.hooker_id,
            lock_4_id=self.lock_4_id,
            lock_5_id=self.lock_5_id,
            flanker_6_id=self.flanker_6_id,
            flanker_7_id=self.flanker_7_id,
            number_8_id=self.number_8_id,
            scrum_half_id=self.scrum_half_id,
            fly_half_id=self.fly_half_id,
            wing_11_id=self.wing_11_id,
            inside_centre_id=self.inside_centre_id,
            outside_centre_id=self.outside_centre_id,
            wing_14_id=self.wing_14_id,
            full_back_id=self.full_back_id,
            id=self.id
        )

    def __repr__(self):
        return '<Squad %r>' % (self.id)
