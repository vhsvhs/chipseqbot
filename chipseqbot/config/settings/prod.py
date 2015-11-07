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

########## HOST CONFIGURATION
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = [PROJECT_DOMAIN, 'localhost', '127.0.0.1']
########## END HOST CONFIGURATION

DEBUG = False

########## EMAIL CONFIGURATION
# https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = '%s Team <contact@%s>' % (PROJECT_NAME, PROJECT_DOMAIN)

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.gmail.com'

# https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 587

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')

# https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
########## END EMAIL CONFIGURATION


########## AMAZON S3 CONFIGURATION
# http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
if 'AWS_ACCESS_KEY_ID' in os.environ:
    AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')

    INSTALLED_APPS += (
        'storages',
        'collectfast'
    )

    AWS_S3_SECURE_URLS = True
    AWS_QUERYSTRING_AUTH = False
    AWS_PRELOAD_METADATA = True
    AWS_IS_GZIPPED = True

    AWS_EXPIREY = 60 * 60 * 24 * 7
    AWS_HEADERS = {
        'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIREY, AWS_EXPIREY)
    }

    # Using django-pipeline along with S3 storage for staticfiles
    # https://django-pipeline.readthedocs.org/en/latest/storages.html#using-with-other-storages
    from django.contrib.staticfiles.storage import CachedFilesMixin
    from pipeline.storage import PipelineMixin
    from storages.backends.s3boto import S3BotoStorage

    class S3PipelineCachedStorage(PipelineMixin, CachedFilesMixin, S3BotoStorage):
        pass

    # Separate buckets for static files and media files
    AWS_STATIC_STORAGE_BUCKET_NAME = '%s-static' % PROJECT_NAME.lower()
    AWS_MEDIA_STORAGE_BUCKET_NAME = '%s-media' % PROJECT_NAME.lower()

    STATIC_URL = '//%s.s3.amazonaws.com/' % AWS_STATIC_STORAGE_BUCKET_NAME
    MEDIA_URL = '//%s.s3.amazonaws.com/' % AWS_MEDIA_STORAGE_BUCKET_NAME

    StaticRootS3BotoStorage = lambda: S3PipelineGZIPCachedStorage(bucket=AWS_STATIC_STORAGE_BUCKET_NAME)
    MediaRootS3BotoStorage = lambda: S3BotoStorage(bucket=AWS_MEDIA_STORAGE_BUCKET_NAME)

    STATICFILES_STORAGE = 'config.settings.prod.StaticRootS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'config.settings.prod.MediaRootS3BotoStorage'
########## END AMAZON S3 CONFIGURATION
