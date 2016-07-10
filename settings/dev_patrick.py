# -*- encoding: utf-8 -*-
from .local import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_www_hatherleighcommunitycentre_co_uk_patrick',
        'USER': 'patrick',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'temp.db',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
#}
