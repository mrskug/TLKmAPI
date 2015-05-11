"""
Django inställnigar for TLKmAPI projektet.

För mera information om denna fil se
https://docs.djangoproject.com/en/1.7/topics/settings/

För en full förteckning på inställningar och värden se
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SÄKERHETS VARNING: SECRET_KEY värdet som används i produktion
# bör hållas hemligt
SECRET_KEY = 'dettabörvaraenlångalfanumerisksträngmedspecialtecken'

# SÄKERHETS VARNING: Använd inte DEBUG i produktionsmiljö!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.exempel.com',  # Tillåt domän med underdomäner
]


# Applikationens definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TLKdb',
    'TLKrest',
    'rest_framework',
    'corsheaders',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Tillåt Requests från andra domäner
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

REST_FRAMEWORK = {
    # Använd Djangos behörighetsklasser
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    # Autentiserings metoder
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    # Filter
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.DjangoFilterBackend',
    ]
}

# URL definitionsklass
ROOT_URLCONF = 'TLKmAPI.urls'

# WSGI namn
WSGI_APPLICATION = 'TLKmAPI.wsgi.application'


# Databas
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    # Sqlite databas
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    # Exempel för Mysql
    #'mysql': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'OPTIONS': {
    #        'read_default_file': './my.cnf',
    #    },
    #}
}

# Internationalisering
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Statiska filer (CSS, JavaScript, Bilder)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
