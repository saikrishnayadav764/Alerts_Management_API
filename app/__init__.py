from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from redis import StrictRedis
from flask_caching import Cache
from config import Config

mongo = PyMongo()
redis_client = StrictRedis.from_url(Config.REDIS_URL)
jwt = JWTManager()
cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    jwt.init_app(app)

    cache.init_app(app)

    from . import routes, auth, alerts
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(alerts.alerts_bp)

    return app
