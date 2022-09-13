from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        # for local development, use postgresql
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "kelvins_insights",
        "USER": "postgres",
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": "localhost",
        "PORT": "5433",
    }
}


STATIC_URL = "/static/"
STATICFILES_DIRS = ("staticfiles",)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "kelvinsinsights@gmail.com"
EMAIL_HOST_USER = "kelvinsinsights@gmail.com"
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_PORT = 587


CELERY_BROKER_URL = "redis://localhost:6379"
