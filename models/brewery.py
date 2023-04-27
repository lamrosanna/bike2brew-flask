
from db import db

class BreweryModel(db.Model):
    __tablename__="breweries"
    id = db.Column(db.Integer, primary_key = True)
    b_id = db.Column(db.String(80), unique = True)
    name = db.Column(db.String(80))
    brewery_type = db.Column(db.String(20))
    street = db.Column(db.String(80))
    state = db.Column(db.String(50))
    postal_code = db.Column(db.String(15))
    phone = db.Column(db.String(20))
    website_url = db.Column(db.String(80))
    #distance = db.Column(db.Integer)
    #rideTime = db.Column(db.Integer)
    #user = db.relationship("UserModel",back_populates="brewery", secondary = "favorite_breweries")


@classmethod
def find_by_id(cls, id):
    return cls.query.filter_by(b_id=id).first()

# @classmethod
# def save_to_db(self):
#     db.session.add(self)
#     db.session.commit()

# def delete_from_db(self):
#     db.session.delete(self)
#     db.session.commit()

# #need another function to query all flags 
# def favorites(cls):
#     return cls.query.filter(cls.flagged == True)