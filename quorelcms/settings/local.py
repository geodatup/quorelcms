from quorelcms.settings.base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9c5aby$s_9v4wwn0j%go2l-ful)jshlrsc)nx8%bsntz66jyld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition



DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.mysql',
	     'NAME': 'quorelcms',
         'USER': 'root',
         'PASSWORD':'mcot',
         'HOST':'localhost', # Set to empty string for localhost.
         'PORT':'', # Set to empty string for default.
    }
}
