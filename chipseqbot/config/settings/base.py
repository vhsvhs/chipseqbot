
"""
Django settings for chipseqbot project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import abspath, basename, join, normpath, dirname
from os import listdir, environ
from sys import path

from django.core.exceptions import ImproperlyConfigured
def get_env_variable(var_name):
    """Get the env. variable, or return exception"""
    try:
        return environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)

# URL of the login page.
#LOGIN_URL = '/login/'
from django.core.urlresolvers import reverse_lazy
LOGIN_URL = 'allauth.account.login'

########## PATH CONFIGURATION
# Absolute filesystem path to the config directory:
CONFIG_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the project directory:
PROJECT_ROOT = dirname(CONFIG_ROOT)

# Absolute filesystem path to the django repo directory:
DJANGO_ROOT = dirname(PROJECT_ROOT)

# Project name:
PROJECT_NAME = basename(PROJECT_ROOT).capitalize()

# Project folder:
PROJECT_FOLDER = basename(PROJECT_ROOT)

# Project domain:
PROJECT_DOMAIN = '%s.com' % PROJECT_NAME.lower()

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(CONFIG_ROOT)
########## END PATH CONFIGURATION

########## EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'Serverbot <dev@%s>' % PROJECT_DOMAIN
########## END EMAIL CONFIGURATION

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

########## MANAGER CONFIGURATION
# See https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Dev Team', 'Dev Team <dev@%s>' % PROJECT_DOMAIN),
)

# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("CHIPSEQBOT_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

#AUTH_PROFILE_MODULE = 'phylobot.UserProfile'

########## Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'allauth',
    'allauth.account',
    #'allauth.socialaccount',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.openid',
)

PROJECT_APPS = (
    'csbportal',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS
########## END APP CONFIGURATION

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'csbotdb',                      # Or path to database file if using sqlite3.
                'USER': 'django',
                'PASSWORD': 'csbotpass',
                'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
                'PORT': '5432',                      # Set to empty string for default.
            }
        }

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

#AUTH_USER_MODEL = 'accounts.User'

TEMPLATE_DIRS = []
for aa in PROJECT_APPS:
    dirname = join( join(PROJECT_ROOT, aa), "templates" )
    TEMPLATE_DIRS.append( dirname )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[ join(PROJECT_ROOT, 'templates'), TEMPLATE_DIRS ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
            # Already defined Django-related contexts here
            # `allauth` needs this from django
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            #'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.request',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',            
            ],
        },
     },
]

########## LOGIN/LOGOUT CONFIGURATION
LOGIN_REDIRECT_URL = '/accounts/profile'

LOGIN_URL = '/accounts/login/'

LOGOUT_URL = '/accounts/logout/'
########## END LOGIN/LOGOUT CONFIGURATION

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID=1

########## STATIC FILE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = '/home/ubuntu/chipseqbot/assets'
STATIC_URL = '/static/'

STATICFILES_DIRS = [join(PROJECT_ROOT, 'static')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = join(STATIC_ROOT, 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END STATIC FILE CONFIGURATION
