from flask import Blueprint

content = Blueprint('content', __name__, url_prefix = '/', template_folder = 'templates')

from . import routes
