from flask import jsonify, request
from flask_restful import Resource
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from app.models import UserModel

class Auth(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        user = UserModel.query.filter_by(username=username).first()
        if user == None:
            return 'Username was not found', 404

        is_username = username != user.username
        is_password = check_password_hash(user.password, password) == False

        if is_username:
            return 'Bad username', 401

        if is_password:
            return 'Bad password', 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
