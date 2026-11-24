from flask import current_app, jsonify
from autolog.main import main_bp

@main_bp.get("/health")
def health_check():
    return jsonify({"status": "ok", "service": "autolog-api"}), 200

@main_bp.get("/config-check")
def config_check():
    return jsonify(
        {
            "env_name": current_app.config.get("ENV_NAME"),
            "runtime_message": current_app.config.get("RUNTIME_MESSAGE"),
            "database_uri": str(current_app.config.get("SQLALCHEMY_DATABASE_URI")),
        }
    ), 200
