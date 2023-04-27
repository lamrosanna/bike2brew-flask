# import requests
# from db import db
# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from models import UserModel
# from models.favorite_brewery import FavoriteBreweryModel
# from passlib.hash import pbkdf2_sha256
# from schemas import BrewerySchema, FavoriteBrewerySchema, UserSchema

# blp = Blueprint("Users", "users", description="Operations on users")

# @blp.route("/register")
# class UserRegistration(MethodView):
#     @blp.arguments(UserSchema)
#     def post(self, user_data):
#         if UserModel.query.filter_by(username = user_data['username']).first():
#             abort(400, message="A user with that username already exists.")
        
#         user = UserModel(
#             username = user_data['username'], 
#             password = pbkdf2_sha256.hash(user_data['password']),
#         )
#         db.session.add(user)
#         db.session.commit()

#         return {"message": "User created successfully."}, 201

# #@blp.route("/login")
# #@blp.route("/logout")

# @blp.route("/user/<string:user_id>")
# class UserFavorites(MethodView):
#     @blp.response(200, BrewerySchema(many = True)) 
#     def get(self, user_id):
#         def get_breweryids(user_id):
#             userfavorite_breweries= FavoriteBreweryModel.query.filter(FavoriteBreweryModel.user == user_id).all()
#             #for each in userfavorite_breweries:
#                 #print(vars(each))
#             if len(userfavorite_breweries) >= 1 :
#                 result = [x.brewery for x in userfavorite_breweries]
#                 return (result)
#             else:
#                 abort(400, message="No breweries has been favorited")
#         def get_breweryinfo(brewerylist):
#             holder = []
#             for each in brewerylist:
#                 #loop through list and consolidate information to return via schema 
#                 brewery_info = requests.get('https://api.openbrewerydb.org/breweries/'+ each).json()
#                 holder.append(brewery_info)
            
#             response = BrewerySchema(many = True)
#             brewery = response.dump(list(holder))
#             return brewery

#         breweryid = get_breweryids(user_id)
#         brewerylist = get_breweryinfo(breweryid)
#         return brewerylist


