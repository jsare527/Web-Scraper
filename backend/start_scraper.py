from flask import Flask, jsonify, render_template, url_for, request, redirect, Blueprint



scraper = Blueprint('scraper', __name__, template_folder='templates')