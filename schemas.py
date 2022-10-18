from marshmallow import Schema, fields

class BrewerySchema(Schema):
    b_id = fields.Str(dump_only=True, data_key="id")#
    name = fields.Str(required=True)
    brewery_type = fields.Str()
    street = fields.Str(required=True)
    state = fields.Str(required=True)
    postal_code = fields.Str()
    website_url = fields.Url()
    phone = fields.Str()

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str(load_only = True)
    favorite_brewery = fields.List(fields.Nested(BrewerySchema()), dump_only=True)
    

#class UserList(UserSchema):
class FavoriteBrewerySchema(Schema):
    brewery = fields.Str()

class Brewery_by_user(BrewerySchema):
    user = fields.List(fields.Nested(UserSchema()), dump_only = True)
