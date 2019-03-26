from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
)
from werkzeug.exceptions import abort

from bonsai_web_api.db import get_db

bp = Blueprint('web_app', __name__)

@bp.route('/')
def index():
    db = get_db()
    products = db.execute(
        'SELECT * FROM product ORDER BY RANDOM() LIMIT 5;'
        #' FROM product p JOIN user u ON p.author_id = u.id'
        #' ORDER BY created DESC'
    ).fetchall()
    return render_template('web_app/index.html', products=products)


