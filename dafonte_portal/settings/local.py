from __future__ import absolute_import

import socket

from os.path import join
from os.path import normpath

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", ]