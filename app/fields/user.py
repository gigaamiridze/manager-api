from flask_restful import fields

resource_users = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String
}
