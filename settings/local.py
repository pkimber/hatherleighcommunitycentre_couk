# -*- encoding: utf-8 -*-
from .base import *

DEBUG = True
THUMBNAIL_DEBUG = DEBUG
TESTING = False

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# FTP upload 'static' folder
FTP_STATIC_DIR = None
FTP_STATIC_URL = None

# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
MEDIA_ROOT = 'media'

# Django debug toolbar (this is the address of the client not the server)
# INTERNAL_IPS = ('127.0.0.1',)
# DEBUG_TOOLBAR_CONFIG = {
#     'INTERCEPT_REDIRECTS': False,
#     'ENABLE_STACKTRACES': True,
# }

# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT = 'media-private'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#INSTALLED_APPS += (
#    'debug_toolbar',
#)
