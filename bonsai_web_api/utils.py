
from flask import make_response

JSON_MIME_TYPE = 'application/json'


def search_product(products, product_id):
    for product in products:
        if product['id'] == product_id:
            return product


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)