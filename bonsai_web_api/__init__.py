import os

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'bonsai_web_api.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Register the products blueprint 
    from . import web_app
    app.register_blueprint(web_app.bp)
    
    
    #Register the mySQL database
    from . import db
    db.init_app(app)
    
    #Register the authentification blueprint 
    from . import auth
    app.register_blueprint(auth.bp)
    
    
    
    #Register the products REST blueprint
    from . import REST_API
    app.register_blueprint(REST_API.bp)
    

    return app