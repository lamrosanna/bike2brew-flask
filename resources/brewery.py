from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from secretsfile import access_key

from db import db
from models import BreweryModel, FavoriteBreweryModel
from schemas import BrewerySchema, UserSchema, FavoriteBrewerySchema

import requests

blp = Blueprint("breweries", __name__, description="Retrieving breweries")

@blp.route("/brewery")
class breweryList(MethodView):
    @blp.response(200, BrewerySchema(many = True))
    def get(self):
        def get_location():
            try:
                location = requests.get('http://api.ipstack.com/check/',params={"access_key":access_key}).json()
                lat = location['latitude']
                lon = location['longitude']
                locdict={"latitude":lat, "longitude":lon}
            except AttributeError:
                abort(404, message='location not located')
            return locdict

        def get_breweries(coordinates):
            try:
                bar = requests.get('https://api.openbrewerydb.org/breweries?by_dist='+str(coordinates['latitude'])+','+str(coordinates['longitude'])+"'").json()
                bar_response = BrewerySchema(many = True)
                res = bar_response.dump(list(bar))
                
            except Exception:
                abort(404, message ='breweries not located')

            return res

        location = get_location()
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

    #@blp.arguments(UserSchema)
    @blp.response(201, BrewerySchema)
    def put(self, brewery_id):
        #brewery = BreweryModel.query.get(brewery_id)
            favbrewery = FavoriteBreweryModel.query.filter(FavoriteBreweryModel.brewery == brewery_id).first()
            if favbrewery:
                abort(400, message=f"Brewery already added")
            else:
                favbrewery = FavoriteBreweryModel(user = 1, brewery = brewery_id )
                bar = requests.get('https://api.openbrewerydb.org/breweries/'+ brewery_id).json()
                bar_response = BrewerySchema()
                res = bar_response.dump(bar)
                db.session.add(favbrewery)
                db.session.commit()
                return res

    def delete(self, brewery_id):
        brewery_check = FavoriteBreweryModel.query.filter(FavoriteBreweryModel.brewery==brewery_id, FavoriteBreweryModel.user ==1).first()   
        if brewery_check:
            db.session.delete(brewery_check)
            db.session.commit()
            return{"message":"Brewery removed from favorites"}, 200
        else:
            abort(400, message=f"Brewery not found in favorites")