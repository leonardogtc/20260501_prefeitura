from .settings import *

import os

DEBUG = True

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = '5nv-t6)v8hfokn6eur#welm=v&*=cty%y9r3^+&(@z9p740a98'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
