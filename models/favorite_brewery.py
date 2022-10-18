from db import db
from schemas import UserSchema 

class FavoriteBreweryModel(db.Model):
    __tablename__="favorite_breweries"

    id = db.Column(db.Integer, primary_key = True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    brewery = db.Column(db.String(80))
    