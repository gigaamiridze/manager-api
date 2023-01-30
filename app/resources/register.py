from flask_restful import Resource
from werkzeug.security import generate_password_hash
from app.parsers.register import registerParser
from app.models import UserModel
from app.models import db

class Register(Resource):
    def post(self):
        args = registerParser.parse_args()
        user = UserModel(username=args['username'], password=generate_password_hash(args['password']))
        db.session.add(user)
        db.session.commit()
        return 'You are registered', 201
