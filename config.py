from datetime import timedelta

class Config:
    MONGO_URI = 'mongodb+srv://naruto:naruto@cluster0.be644zi.mongodb.net/db'
    JWT_SECRET_KEY = 'secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=90)
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'redis'
    CACHE_KEY_PREFIX = 'prefix'
    REDIS_URL = 'redis://localhost:6379/0'
