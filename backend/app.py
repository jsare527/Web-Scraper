from flask import Flask, jsonify, render_template, url_for, request, redirect, Blueprint
from start_scraper import scraper
from models import *
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.register_blueprint(scraper, url_prefix='/scraper')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "super_secret_key"
db.init_app(app)



@app.route("/")
def home():
    new_egg_products = NewEggProduct.query.all()
    amazon_products = AmazonProduct.query.all()
    return render_template("home.html", new_egg_products=new_egg_products, amazon_products=amazon_products)


if __name__ == "__main__":
    app.run(debug=True)