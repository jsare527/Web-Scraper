from flask import Flask, jsonify, render_template, url_for, request, redirect, Blueprint
from models import AmazonProduct, NewEggProduct, db
import os, re, json


scraper = Blueprint('scraper', __name__, template_folder='templates')
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@scraper.route("/", methods=['POST'])
def handle_form_request():
    if request.method == 'POST':
        product = str(request.form.get("product")).strip()
        website = request.form.get("options")
        os.chdir(__location__)
        os.chdir("scrapy/scraper/scraper")
        safe_filename = "".join([c for c in product if re.match(r'\w', c)])
        print(product)

        data_set = None
        if website == "Amazon" and product != "":
            os.system(f"scrapy crawl amazon_spider -a category='{safe_filename}' -O ../amazon_products/{safe_filename}.json")
            os.chdir("../")
            f = open(f'amazon_products/{safe_filename}.json', 'rb')
            data_set = json.load(f)
            db.session.add(AmazonProduct(product_name=product, dictionary=data_set))
            db.session.commit()

        if website == "NewEgg" and product != "":
            os.system(f"scrapy crawl new_egg_spider -a category='{safe_filename}' -O ../newegg_products/{safe_filename}.json")
            os.chdir("../")
            f = open(f'newegg_products/{safe_filename}.json', 'rb')
            data_set = json.load(f)
            db.session.add(NewEggProduct(product_name=product, dictionary=data_set))
            db.session.commit()

    return render_template('table.html', dictionary=data_set, product_name=product)