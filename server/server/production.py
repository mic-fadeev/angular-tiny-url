from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tiny_url',
        'USER': 'tiny_url',
        'PASSWORD': 'tiny_url',
        'HOST': '',
        'PORT': '',
    }
}
