from flask import Flask
from .extensions import ralidator
from .views import main_views, permission_views


TEST_SECRET_KEY = "test_key"


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["FILTERS_MAP"] = {}
    app.config["RALIDATOR_SETTINGS"] = {
        "user_api_url": "user_api_url",
        "user_api_token": "user_api_token",
        "secret_key": TEST_SECRET_KEY,
    }
    ralidator.init_app(app)
    app.register_blueprint(main_views)
    app.register_blueprint(permission_views)
    return app