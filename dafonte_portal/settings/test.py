from __future__ import absolute_import

import socket

from os.path import join
from os.path import normpath

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["test.dafonte.capyba.com", ]

INSTALLED_APPS += (
	# Amazon Storage
		'storages',
)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'us-east-2')
AWS_AUTO_CREATE_BUCKET = True
AWS_LOCATION = "test"
AWS_S3_CUSTOM_DOMAIN = "s3.{}.amazonaws.com/{}".format(AWS_S3_REGION_NAME, AWS_STORAGE_BUCKET_NAME)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' # <-- here is where we reference it


SENTRY_ENVIRONMENT = 'test'