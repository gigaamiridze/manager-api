from flask_restful import Resource, marshal_with
from flask_jwt_extended import jwt_required
from app.fields.product import resource_product
from app.parsers.product import productParser
from app.models import ProductModel
from app.models import db

class Product(Resource):
    @marshal_with(resource_product)
    @jwt_required()
    def get(self, product_id):
        if product_id == 777:
            return ProductModel.query.all()
        product = ProductModel.query.filter_by(id=product_id).first()
        return product

    @jwt_required()
    def post(self, product_id):
        args = productParser.parse_args()
        product = ProductModel(product=args['product'], price=args['price'], user_id=args['user_id'])
        db.session.add(product)
        db.session.commit()
        return f"Added product with ID {product_id}"

    @jwt_required()
    def put(self, product_id):
        args = productParser.parse_args()
        product =ProductModel.query.filter_by(id=product_id).first()
        if product == None:
            product = ProductModel(product=args['product'], price=args['price'], user_id=args['user_id'])
        else:
            product.product = args['product']
            product.price = args['price']
            product.user_id = args['user_id']
        db.session.add(product)
        db.session.commit()
        return f"Edited product with ID {product_id}"

    @jwt_required()
    def delete(self, product_id):
        if product_id == None:
            return f"Product ID {product_id} doesn't exist"
        product = ProductModel.query.filter_by(id=product_id).first()
        db.session.delete(product)
        db.session.commit()
        return f"Deleted product with ID {product_id}"
