from flask import Flask, jsonify
from flask_cors import CORS
from flask_talisman import Talisman

from service.routes import accounts_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(test_config or {})
    CORS(app)
    Talisman(
        app,
        force_https=False,
        content_security_policy={"default-src": ["'self'"]},
    )
    app.register_blueprint(accounts_bp)

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app
