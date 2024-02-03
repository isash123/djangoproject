
import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY", default="insecure-key-fill-with-your-own")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)
# CSRF_TRUSTED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", "*").split(" ")
ALLOWED_HOSTS = ["*"]
# CORS_ORIGIN_WHITELIST = config("CORS_ORIGIN_WHITELIST", "*").split(" ")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_celery_beat",
    "django_celery_results",
	'authentication',
	'app',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "core.urls"
LOGIN_REDIRECT_URL = "dashboard"   # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [TEMPLATE_DIR],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
			'libraries': {
			# 'custom_tags':'app.template_tags.custom_tags'
			}
		},
	},
]

WSGI_APPLICATION = "core.wsgi.application"

# DATABASE CONFIG
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": config("PGHOST", default="db"),
        "USER": config("PGUSER", default="postgres"),
        "NAME": config("PGDATABASE", default="postgres"),
        "PASSWORD": config("PGPASSWORD", default="postgres"),
        "PORT": config("PGPORT", default=5432),
        "CONN_MAX_AGE": 60,
    }
}

REDIS_URL = f"redis://{config('REDISUSER', default='default')}:{config('REDISPASSWORD', default='')}@{config('REDISHOST', default='redis')}:{config('REDISPORT', default=6379)}"

# CELERY CONFIG
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", default="django-db")
CELERY_BEAT_SCHEDULER = config(
    "CELERY_BEAT_SCHEDULER", default="django_celery_beat.schedulers.DatabaseScheduler"
)

# REDIS CACHE CONFIG
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": REDIS_URL,
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATICFILES (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(CORE_DIR, 'core/staticfiles')
STATICFILES_DIRS = (os.path.join(CORE_DIR, 'core/static'),)

# EMAIL CLIENT
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
