from flask_restful import fields

resource_product = {
    'id': fields.Integer,
    'product': fields.String,
    'price': fields.Float,
    'user_id': fields.Integer
}
