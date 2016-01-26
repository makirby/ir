from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    name = db.Column(db.String)
    
    date_of_birth = db.Column(db.Date)
    
    height = db.Column(db.Integer)
    
    weight = db.Column(db.Integer)
    
    player_text = db.Column(db.String)
    
    retired = db.Column(db.Boolean)
    
    user_created = db.Column(db.Boolean)
    
    image_location = db.Column(db.String)
    
    icon_location = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            name = self.name,
            date_of_birth = self.date_of_birth.isoformat(),
            height = self.height,
            weight = self.weight,
            player_text = self.player_text,
            retired = self.retired,
            user_created = self.user_created,
            image_location = self.image_location,
            icon_location = self.icon_location,
            id = self.id
        )

    def __repr__(self):
        return '<Player %r>' % (self.id)
