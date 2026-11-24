import os

class BaseConfig:
    SECRET_KEY = os.environ.get("JWT_SECRET", "dev-fallback")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RUNTIME_MESSAGE = os.environ.get("RUNTIME_MESSAGE", "default-runtime-message")

class DevelopmentConfig(BaseConfig):
    ENV_NAME = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///dev.db")

class TestingConfig(BaseConfig):
    ENV_NAME = "testing"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(BaseConfig):
    ENV_NAME = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

config_by_name = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
