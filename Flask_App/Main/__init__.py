from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

from .config import Config

db = SQLAlchemy()

from .Models import *

def create_app():
    #Create the flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    

    #Create/Initialize the Database
    with app.app_context():
        db.create_all()
    
    #Create/Initialize the Blueprints for endpoints
    from .Controllers.sample_controller import api as sample_ns
    blueprint = Blueprint('api', __name__)
    api = Api(blueprint,
          title='Flask REST API',
          version='1.0',
          description='basic template for a flask REST API backend'
        )
    api.add_namespace(sample_ns, path='/sample')
    app.register_blueprint(blueprint)
    return app