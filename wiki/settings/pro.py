from .base import *
from decouple import config
import django_on_heroku
import dj_database_url

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

#this is th hardest part
##STATICFILES_DIRS =  [ BASE_DIR / "static"]
STATIC_ROOT = os.path.join(BASE_DIR, 'live-static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'live-static', 'media-root')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
DEBUG_PROPAGATE_EXCEPTIONS = True
# Heroku settings
django_on_heroku.settings(locals(), staticfiles=False)



import os, subprocess, dj_database_url

bashCommand = “heroku config:get DATABASE_URL -a magblog” #Use your app_name

output = subprocess.check_output([‘bash’,’-c’, bashCommand]).decode(“utf-8”) # executing the bash command and converting byte to string

DATABASES[‘default’] = dj_database_url.config(default=output,conn_max_age=600, ssl_require=True) #making connection to heroku DB without having to set DATABASE_URL env variable

"""db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
##del DATABASES['default']['OPTIONS']['sslmode']

DATABASES = {
    'default': dj_database_url.config()
}
"""
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True

"""Hello world"""

love= "i love you"