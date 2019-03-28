from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort
from flask_security import login_required 
from bonsai_web_api.db import get_db
from bonsai_web_api.REST_API import products_list, products_search_by_id
import json

bp = Blueprint('web_app', __name__)

@bp.route('/')
def index():
    return render_template('web_app/index.html', products=json.loads(products_list(10).get_data()))

@bp.route('/product_description/')
@bp.route('/product_description/<path:product_uri>')
def get_product_description(product_uri=None):
    if product_uri==None:
        product_uri = "rdf.bonsai.uno/exiobase3_3_17/activities/A_ALUM"
    
    product=products_search_by_id(product_uri).get_data().decode("utf-8") 
    return render_template('web_app/bonsai_pedia.html', product=json.loads(product))




