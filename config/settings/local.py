from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "blog",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": 5432,
    }
}


STATIC_URL = "/static/"
STATICFILES_DIRS = ("staticfiles",)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = "admin@localhost"
EMAIL_HOST_USER = "admin@localhost"
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_PORT = 25


CELERY_BROKER_URL = "redis://localhost:6379"
