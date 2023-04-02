from __future__ import absolute_import
import os
from .base import *


ALLOWED_HOSTS = [
    "64.227.15.81", "staging.dafonte.capyba.com",
    "www.dafonteadv.com.br", "dafonteadv.com.br"
]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += ('storages',)
AWS_S3_ENDPOINT_URL = 'https://fra1.digitaloceanspaces.com/'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', '')
AWS_AUTO_CREATE_BUCKET = True
AWS_LOCATION = "staging"
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.digitaloceanspaces.com"
)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

SENTRY_ENVIRONMENT = 'staging'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'mysite/static'),
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_ENDPOINT_URL, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'