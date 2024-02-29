import os
from pathlib import Path
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

INSTALLED_APPS = [
    "my_shop",
    'sorl.thumbnail',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

...

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

...

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = BASE_DIR / 'staticfiles'
