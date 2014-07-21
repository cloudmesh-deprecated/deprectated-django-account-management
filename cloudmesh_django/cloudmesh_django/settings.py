"""
Django settings for cloudmesh_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_ty*jlfdjs1l1i3!uy#8!op6(dmx_sn@8^qncurj=paqs14%pj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudmesh_django',
    'macros',
    'django_jinja',
#    'mongoadmin',
#    'mongoengine.django.mongo_auth',
    'rest_framework',
)

#MONGOADMIN_OVERRIDE_ADMIN = True

#AUTHENTICATION_BACKENDS = ( 
#           'mongoengine.django.auth.MongoEngineBackend',
# )
 
#AUTH_USER_MODEL = 'mongo_auth.MongoUser'
#MONGOENGINE_USER_DOCUMENT = 'mongoengine.django.auth.User'


SESSION_ENGINE = 'mongoengine.django.sessions'
SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'


#
# DO NOT USE MONGO ADMIN
#
#from mongoengine import connect
#MONGO_DATABASE_NAME = 'user'
#MONGO_HOST = 'cannot be set here'
#MONGO_PORT = 27777
#connect('mongodb', port=27777)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cloudmesh_django.urls'

WSGI_APPLICATION = 'cloudmesh_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#from mongoengine import connect
#connect('mongodb')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django_jinja.loaders.AppLoader',
    #'django_jinja.loaders.FileSystemLoader',        
)

#INSTALLED_APPS += ('django_jinja',)

TEMPLATE_DIRS = (
        'templates',
)

STATIC_URL = '/static/'


STATIC_ROOT = 'static/'
