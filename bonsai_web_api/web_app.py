from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from bonsai_web_api.db import get_db
from bonsai_web_api.REST_API import products_list
import json

bp = Blueprint('web_app', __name__)

@bp.route('/')
def index():
    return render_template('web_app/index.html', products=json.loads(products_list(10).get_data()))


