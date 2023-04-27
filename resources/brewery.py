import requests
import os
from db import db
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from math import sin, cos, sqrt, atan2, radians
from dotenv import load_dotenv


from models import BreweryModel #, FavoriteBreweryModel
from schemas import BrewerySchema #, FavoriteBrewerySchema, UserSchema

from sqlalchemy.exc import SQLAlchemyError

# error msg
USER_NOT_LOCATED = "Your location was not found"
BREWERY_NOT_FOUND = "There was an error locating breweries near you"
UNABLE_TO_GET_DISTANCE = "The distance to {} is unavailable"

# env variables
load_dotenv()
access_key = os.getenv("ACCESS_KEY")
api_key = os.getenv("GG_APIKEY")

blp = Blueprint("breweries", __name__, description="Retrieving breweries")

@blp.route("/")
class breweryList(MethodView):
    @blp.response(200, BrewerySchema(many = True))
    def get(self):
        def get_userLocation():
            try:
                # Get user location 
                location = requests.get('http://api.ipstack.com/check/',params={"access_key":access_key}).json()
                locdict=[str(location['latitude']), str(location['longitude'])]
            except AttributeError:
                abort(500, message='location not located')
            return locdict

        def get_breweries(coordinates):
            try:
                # Testing with specified result
                payload = {"per_page":5}
                # Get Brewery location based off user coordinates
                breweries = requests.get('https://api.openbrewerydb.org/breweries?by_dist='+coordinates[0]+','+coordinates[1], payload).json()
                # Get brewery distance and ride time
                close_breweries = get_breweryDistance(coordinates , breweries)
                bar_response = BrewerySchema(many = True)
                res = bar_response.dump(list(close_breweries))
                
            except Exception:
                abort(500, message ='There was an error in processing your request')

            return res
        
        # get brewery distance from user location
        def get_breweryDistance(userLocation, breweries):
            origin = userLocation[0]+","+userLocation[1]
            for eachBar in breweries:
                destination = eachBar['latitude']+","+eachBar['longitude']
                payload = {"origin":origin, "destination":destination, "mode":"bicycling", "key":api_key}
                try:
                    toBrewery = requests.get('https://maps.googleapis.com/maps/api/directions/json', params=payload).json()
                    distance = toBrewery["routes"][0]["legs"][0]["distance"]["text"]
                    rideTime = toBrewery["routes"][0]["legs"][0]["duration"]["text"]
                    eachBar['distance'] = distance
                    eachBar['rideTime'] = rideTime
                except Exception:
                    print(UNABLE_TO_GET_DISTANCE.format(eachBar["name"]))

            return breweries


        location = get_userLocation()
        breweries = get_breweries(location)

        return breweries

@blp.route("/brewery/<string:brewery_id>")
class Brewery(MethodView):
    @blp.response(200, BrewerySchema)
    def get(self, brewery_id):
        try:
            bar = requests.get('https://api.openbrewerydb.org/breweries/'+ brewery_id).json()
            bar_response = BrewerySchema()
            res = bar_response.dump(bar)
        except Exception:
            abort(404, message="Brewery was not found")

        return res
    #@blp.arguments(BrewerySchema)

    # #@blp.arguments(UserSchema)
    # @blp.response(201, BrewerySchema)
    # def put(self, brewery_id):
    #     #brewery = BreweryModel.query.get(brewery_id)
    #         favbrewery = FavoriteBreweryModel.query.filter(FavoriteBreweryModel.brewery == brewery_id).first()
    #         if favbrewery:
    #             abort(400, message=f"Brewery already added")
    #         else:
    #             favbrewery = FavoriteBreweryModel(user = 1, brewery = brewery_id )
    #             bar = requests.get('https://api.openbrewerydb.org/breweries/'+ brewery_id).json()
    #             bar_response = BrewerySchema()
    #             res = bar_response.dump(bar)
    #             db.session.add(favbrewery)
    #             db.session.commit()
    #             return res

    # def delete(self, brewery_id):
    #     brewery_check = FavoriteBreweryModel.query.filter(FavoriteBreweryModel.brewery==brewery_id, FavoriteBreweryModel.user ==1).first()   
    #     if brewery_check:
    #         db.session.delete(brewery_check)
    #         db.session.commit()
    #         return{"message":"Brewery removed from favorites"}, 200
    #     else:
    #         abort(400, message=f"Brewery not found in favorites")
