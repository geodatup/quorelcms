from quorelcms.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9c5aby$s_9v4wwn0j%go2l-ful)jshlrsc)nx8%bsntz66jyld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.mysql',
	     #'NAME': 'testTemplate',
         #'USER': 'root',
         #'PASSWORD':'mcot',
         #'HOST':'localhost', # Set to empty string for localhost.
         'NAME': 'geodatup$quorelcms',
         'USER': 'geodatup',
         'PASSWORD':'mcot9a9.u',
         'HOST':'geodatup.mysql.pythonanywhere-services.com', # Set to empty string for localhost.
         'PORT':'', # Set to empty string for default.
    }
}

