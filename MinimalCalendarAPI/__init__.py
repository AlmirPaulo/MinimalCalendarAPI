from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os, logging

#logger set up
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

#app and database instances 
app = Flask(__name__)
db = SQLAlchemy()

#Factory
def create_app():
    from . import views, models, api 

    app.config['SECRET_KEY'] = open('.note_secret_key').read()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    
    db.init_app(app)
    from .models import User, Todo
    create_database(app)
 
    return app

def create_database(app):
    if not os.path.exists('data.db'):
        db.create_all(app=app)


