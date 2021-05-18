#https://flask-httpauth.readthedocs.io/en/latest/index.html
#https://www.youtube.com/watch?v=VW8qJxy4XcQ
from flask_httpauth import HTTPBasicAuth
from  flask import Blueprint
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
import logging

#Logger Set up
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='server.log', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

#http auth decorator
login_auth = HTTPBasicAuth()
#Blueprint (need to register)
auth = Blueprint('auth', __name__)

#Uma função para criar usuários
def new_user():
    #criar usuário é inserir no db...
    users = {}
    for u in User:
        users.update({User.username:User.password})

#Uma função para verificar usuário? Ou cada rota terá uma?
