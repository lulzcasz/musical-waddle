from flask import Flask

def create_app():
    app = Flask(__name__)

    from .blueprints import content as content_bp
    app.register_blueprint(content_bp)

    return app
