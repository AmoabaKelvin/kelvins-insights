from .base import *

DEBUG = False

# update allowed hosts
ALLOWED_HOSTS = ["kelvinamoaba.me", "www.kelvinamoaba.me", "164.92.102.11"]


# email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.environ["EMAIL_ADDRESS"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_PASSWORD"]
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# configuring database for production environment
DATABASES = {
    "default": {}
}

import dj_database_url

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# configuring static files for production environment
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# setting default storage to use cloudinary
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.RawMediaCloudinaryStorage"


# cloudinary configuration
CLOUDINARY_STORAGE = {
    "CLOUDINARY_URL": os.environ["CLOUDINARY_URL"],
}

# Django security settings
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 2592000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
