from flask_restful import Resource, marshal_with
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from app.fields.user import resource_users
from app.parsers.user import userParser
from app.models import UserModel
from app.models import db

class User(Resource):
    @marshal_with(resource_users)
    @jwt_required()
    def get(self, user_id):
        if user_id == 000:
            return UserModel.query.all()
        user = UserModel.query.filter_by(id=user_id).first()
        return user

    @jwt_required()
    def post(self, user_id):
        args = userParser.parse_args()
        password = generate_password_hash(args['password'])
        user = UserModel(username=args['username'], password=password)
        db.session.add(user)
        db.session.commit()
        return f'Created user with ID {user_id}'

    @jwt_required()
    def put(self, user_id):
        args = userParser.parse_args()
        user = UserModel.query.filter_by(id=user_id).first()
        password = generate_password_hash(args['password'])
        if user == None:
            user = UserModel(username=args['username'], password=password)
        else:
            user.username = args['username']
            user.password = password
        db.session.add(user)
        db.session.commit()
        return f'Edited user with ID {user_id}'

    @jwt_required()
    def delete(self, user_id):
        if user_id == None:
            return f"User ID {user_id} doesn't exist"
        user = UserModel.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return f'Deleted user with ID {user_id}'
