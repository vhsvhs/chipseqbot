"""
Django settings for chipseqbot project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from __future__ import absolute_import

from .base import *

import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qm4)r)h-n$%vzl4ob7)q_@+0e$8+iuns9_u0n-bz6v_&c706p^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

########## IN-MEMORY TEST DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'test.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

########## EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
########## END EMAIL CONFIGURATION
