import dj_database_url

from .base import *

DEBUG = False

# update allowed hosts
ALLOWED_HOSTS = ["kelvinamoaba.me", "kelvins-insights.herokuapp.com"]


# email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ["EMAIL_ADDRESS"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# configuring database for production environment
DATABASES = {
    "default": {},
}
prod_db = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(prod_db)


# configuring static files for production environment
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# setting default storage to use cloudinary
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.RawMediaCloudinaryStorage"


# cloudinary configuration
CLOUDINARY_STORAGE = {
    "CLOUDINARY_URL": os.environ["CLOUDINARY_URL"],
}
