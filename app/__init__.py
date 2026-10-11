from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    from app.routes.main import mainBlue
    app.register_blueprint(mainBlue)

    return app