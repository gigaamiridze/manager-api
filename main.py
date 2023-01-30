from flask import Flask, redirect
from app.models import db
from flask_restful import Api
from app.resources.register import Register
from app.resources.auth import Auth
from app.resources.user import User
from app.resources.product import Product
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)

    db_name = 'data.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "my-secret-key"

    api = Api(app)
    jwt = JWTManager(app)
    db.init_app(app)

    api.add_resource(Register, '/register')
    api.add_resource(Auth, '/login')
    api.add_resource(User, '/user/<int:user_id>')
    api.add_resource(Product, '/product/<int:product_id>')

    @app.route('/')
    def home():
        return redirect('https://github.com/gigaamiridze/Manager-API')

    @app.before_first_request
    def create_table():
        import seed
        seed.create_database()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=7777)