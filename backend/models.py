from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AmazonProduct(db.Model):
    __tablename__ = 'amazonproducts'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), unique=False, nullable=False)
    dictionary = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return f'<AmazonProduct {self.product_name}>'

class NewEggProduct(db.Model):
    __tablename__ = 'neweggproducts'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), unique=False, nullable=False)
    dictionary = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return f'<NewEggProduct {self.product_name}>'