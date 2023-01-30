from flask_restful import reqparse

productParser = reqparse.RequestParser()
productParser.add_argument('product', type=str, help='product should be string')
productParser.add_argument('price', type=float, help='price should be float')
productParser.add_argument('user_id', type=int, help='user_id should be integer')
