from .base import *
from decouple import config
import django_on_heroku

DEBUG = False

"""ADMINS = (
    ('Magloire Mukendi', 'magmukendi0@gmail.com'),
)"""
"""ALLOWED_HOSTS = ['https://wepo.herokuapp.com/']"""

ALLOWED_HOSTS = ['*']

"""
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'PORT': config('DB_PORT'),
        'HOST': config('DB_HOST'),
    }
}"""

LOGGING = {
    'version': 1,
    'disable_existing_loggers':False,
    'formatters':{
        'verbose':{
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datafmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple':{
            'format':'%(levelname)s %(message)s'
        },
    },
    'handlers':{
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers':{
        'MYAPP':{
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

#okay
STATIC_URL = 'static/'
STATICFILES_DIRS =  [ BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static', 'media-root')

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
DEBUG_PROPAGATE_EXCEPTIONS = True
# Heroku settings
#django_on_heroku.settings(locals(), staticfiles=False)

##del DATABASES['default']['OPTIONS']['sslmode']

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

"""Hello world"""