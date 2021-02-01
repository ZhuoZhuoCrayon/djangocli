# -*- coding: utf-8 -*-

from djangocli.conf.default_settings import *   # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
