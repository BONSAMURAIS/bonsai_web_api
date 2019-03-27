from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, abort
)


from .utils import json_response, JSON_MIME_TYPE
from bonsai_web_api.db import get_db
import json

bp = Blueprint('REST_API', __name__)

@bp.route('/rest/products/', methods=["GET"])
@bp.route('/rest/products/<int:lim>', methods=["GET"])
def products_list(lim=None):
    db = get_db()
    
    if lim==None:
        cursor = db.execute('SELECT * FROM product;')
        
    else:
        cursor = db.execute('SELECT * FROM product LIMIT '+str(lim)+';')
    products = [{
        'uri': row[0],
        'name':row[1],
        'activity_code_1':row[2],
        'activity_code_2':row[3],
        'introduction':row[4],
        'entityType':row[5],
        'graphdbName':row[6],
        'dataSpace':row[7],
        'abstractField':row[8],
        'creationDate':row[9],
        'sameAs':row[10],
        'industry':row[11],
        'outputOf':row[12],
        'inputOf':row[13],
        'productionVolume':row[14],
        'productionVolumeUnit':row[15],
        'pedigreeMatrix':row[16],
        'imageUrl':row[17]

    } for row in cursor.fetchall()]

    return json_response(json.dumps(products))

@bp.route('/rest/products/search_by_uri/<path:product_uri>', methods=["GET"])
def products_search_by_id(product_uri):

    db = get_db()
    cursor = db.execute('SELECT * FROM product WHERE uri LIKE "%'+product_uri+'%"') 
    products = [{
      'uri': row[0],
        'name':row[1],
        'activity_code_1':row[2],
        'activity_code_2':row[3],
        'introduction':row[4],
        'entityType':row[5],
        'graphdbName':row[6],
        'dataSpace':row[7],
        'abstractField':row[8],
        'creationDate':row[9],
        'sameAs':row[10],
        'industry':row[11],
        'outputOf':row[12],
        'inputOf':row[13],
        'productionVolume':row[14],
        'productionVolumeUnit':row[15],
        'pedigreeMatrix':row[16],
        'imageUrl':row[17]
    } for row in cursor.fetchall()]
    
    if len(products)>0:
        return json_response(json.dumps(products))
    else:
        abort(404)
        
@bp.route('/rest/products/search_by_name/<product_name>', methods=["GET"])
def products_search_by_name(product_name):
    db = get_db()
    cursor = db.execute('SELECT * FROM product WHERE name LIKE "%'+product_name+'%"') 
    products = [{
       'uri': row[0],
        'name':row[1],
        'activity_code_1':row[2],
        'activity_code_2':row[3],
        'introduction':row[4],
        'entityType':row[5],
        'graphdbName':row[6],
        'dataSpace':row[7],
        'abstractField':row[8],
        'creationDate':row[9],
        'sameAs':row[10],
        'industry':row[11],
        'outputOf':row[12],
        'inputOf':row[13],
        'productionVolume':row[14],
        'productionVolumeUnit':row[15],
        'pedigreeMatrix':row[16],
        'imageUrl':row[17]
    } for row in cursor.fetchall()]
    
    if len(products)>0:
        return json_response(json.dumps(products))
    else:
        abort(404)
        
