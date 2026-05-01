import os

from .settings import *

DEBUG = True

# Crie a secret key para seu ambiente de desenvolvimento
SECRET_KEY = 'gz9_-75l#-)pn_60nckxqffa2buldfd=axiyc6&n9ix6$(sz*('

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
