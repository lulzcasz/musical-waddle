from flask import render_template

from . import content

@content.route('', methods = ['GET'])
def index():
    return render_template('content/index.html')
