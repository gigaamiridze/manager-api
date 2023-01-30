from app.models import db

class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init(self, product, price, user_id):
        self.product = product
        self.price = price
        self.user_id = user_id

    def __repr__(self):
        return f"<Product name is: {self.product}>"
