import dj_database_url

from .base import *

DEBUG = os.environ["DEBUG"] == "True"

# update allowed hosts
ALLOWED_HOSTS = [
    "kelvinamoaba.me",
    "www.kelvinamoaba.me",
    "kelvins-insights.herokuapp.com",
]


# email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ["EMAIL_ADDRESS"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# configuring database for production environment
DATABASES = {"default": {}}

DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# configuring static files for production environment

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.RawMediaCloudinaryStorage"

# cloudinary configuration
CLOUDINARY_STORAGE = {
    "CLOUDINARY_URL": os.environ["CLOUDINARY_URL"],
}

# Django caching framework for production environment
# The cache framework to use will be redis.
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ["REDIS_URL"],
    }
}
