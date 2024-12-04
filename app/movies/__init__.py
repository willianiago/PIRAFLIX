from flask import Blueprint

#cria o blueprint de pets e especifica a pasta de templates
movies = Blueprint('movies', __name__, template_folder='templates')

from . import routes