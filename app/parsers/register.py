from flask_restful import reqparse

registerParser = reqparse.RequestParser()
registerParser.add_argument('username', type=str, help='username should be string')
registerParser.add_argument('password', type=str, help='password should be string')
