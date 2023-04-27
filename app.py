import os
from pickle import TRUE
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api
from db import db
from dotenv import load_dotenv


from resources.brewery import blp as BreweryBlueprint
#from resources.user import blp as UserBlueprint

app = Flask(__name__)
load_dotenv()
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Bike to Brew"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"]= TRUE
db.init_app(app)
migrate = Migrate(app,db)

api = Api(app)

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

api.register_blueprint(BreweryBlueprint)
    #api.register_blueprint(UserBlueprint)

if __name__ == '__main__':
    app.run(port=5000)
