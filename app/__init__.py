import os

from flask import Flask, jsonify
from flask_cors import CORS

from config import config_by_name
from app.database import init_db
from app.routes import api_bp, page_bp


def create_app():
    env_name = os.environ.get("FLASK_ENV", "default")
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(env_name, config_by_name["default"]))

    CORS(app, origins=app.config["CORS_ORIGINS"])

    with app.app_context():
        init_db(app)

    app.register_blueprint(page_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.get("/health")
    def health():
        return jsonify({"basari": True, "durum": "aktif"})

    return app


app = create_app()
