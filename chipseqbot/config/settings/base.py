
"""
Django settings for chipseqbot project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import abspath, basename, join, normpath

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


from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
    """Get the env. variable, or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)


########## EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % PROJECT_NAME

# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'Serverbot <dev@%s>' % PROJECT_DOMAIN
########## END EMAIL CONFIGURATION


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


########## Application definition
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = {
    'authtools',
}

PROJECT_APPS = {
    'apps.accounts',
}

EXTENSION_APPS = {}

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS + EXTENSION_APPS
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


ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'


########## LOGIN/LOGOUT CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = '/'

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = '/login/'

# https://docs.djangoproject.com/en/dev/ref/settings/#logout-url
LOGOUT_URL = '/logout/'
########## END LOGIN/LOGOUT CONFIGURATION

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


########## MEDIA CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

########## STATIC FILE CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'public'))

STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(PROJECT_ROOT, 'static')),
)

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'pipeline.finders.CachedFileFinder',
)
########## END STATIC FILE CONFIGURATION