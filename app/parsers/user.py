from flask_restful import reqparse

userParser = reqparse.RequestParser()
userParser.add_argument('username', type=str, help='username should be string')
userParser.add_argument('password', type=str, help='password should be string')
