from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory',
    }
}

EMAIL_BACKEND = 'djanog.core.mail.backends.locmem.EmailBackend'