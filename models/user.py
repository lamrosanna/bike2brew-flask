# from db import db
# from models import favorite_brewery 

# class UserModel(db.Model):
#     __tablename__="users"

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique = True, nullable = False)
#     password = db.Column(db.String(100), unique = True, nullable = False)
#     #brewery = db.relationship("BreweryModel", back_populates="user", secondary = "favorite_breweries")



# @classmethod
# def save_to_db(self):
#     db.session.add(self)
#     db.session.commit()