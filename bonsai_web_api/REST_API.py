from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, abort
)


from .utils import json_response, JSON_MIME_TYPE
from bonsai_web_api.db import get_db
import json

bp = Blueprint('REST_API', __name__)


@bp.route('/rest/products', methods=["GET"])
def products_list():
    db = get_db()
    cursor = db.execute('SELECT id, item, type, year, location FROM product;')
    products = [{
        'id': row[0],
        'item':row[1],
        'type':row[2],
        'year':row[3],
        'location':row[4]
    } for row in cursor.fetchall()]

    return json_response(json.dumps(products))

@bp.route('/rest/products/search_by_id/<int:product_id>', methods=["GET"])
def products_search_by_id(product_id):
    db = get_db()
    cursor = db.execute('SELECT id, item, type, year, location FROM product WHERE product.id='+str(product_id)) 
    products = [{
        'id': row[0],
        'item':row[1],
        'type':row[2],
        'year':row[3],
        'location':row[4]
    } for row in cursor.fetchall()]
    
    if len(products)>0:
        return json_response(json.dumps(products))
    else:
        abort(404)
        
@bp.route('/rest/products/search_by_item/<product_item>', methods=["GET"])
def products_search_by_item(product_item):
    db = get_db()
    cursor = db.execute('SELECT id, item, type, year, location FROM product WHERE item LIKE "%'+product_item+'%"') 
    products = [{
        'id': row[0],
        'item':row[1],
        'type':row[2],
        'year':row[3],
        'location':row[4]
    } for row in cursor.fetchall()]
    
    if len(products)>0:
        return json_response(json.dumps(products))
    else:
        abort(404)
        
@bp.route('/rest/products/search_by_type/<product_type>', methods=["GET"])
def products_search_by_type(product_type):
    db = get_db()
    cursor = db.execute('SELECT id, item, type, year, location FROM product WHERE type LIKE "%'+product_type+'%"') 
    products = [{
        'id': row[0],
        'item':row[1],
        'type':row[2],
        'year':row[3],
        'location':row[4]
    } for row in cursor.fetchall()]
    
    if len(products)>0:
        return json_response(json.dumps(products))
    else:
        abort(404)
        
