from app.models import db
from faker import Faker
from app.models.user import UserModel
from app.models.product import ProductModel
from werkzeug.security import generate_password_hash

fake = Faker()

db.create_all()

product_data = [
    {'id': 1, 'product': 'Computer', 'price': 1000.00, 'user_id': 1}
]

def create_database():
    for i in range(1, 50):
        user = UserModel(username=fake.name(), password=generate_password_hash(fake.password()))
        db.session.add(user)
        db.session.commit()

    for i in product_data:
        product = ProductModel(product=i['product'], price=i['price'], user_id=i['user_id'])
        db.session.add(product)
        db.session.commit()
