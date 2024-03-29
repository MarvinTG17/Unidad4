"""
Django settings for portafolio project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
#from django.contrib.messages import constants as mensajes

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!sq3wixjk#4*0#zi$cu4%6a#ytuu4k1ahk!=qu=*w(@w)yc66)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['unidad4-production.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://unidad4-production.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'proyectos'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'portafolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portafolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#mysql://root:yuGOcn8sRcUBrtHAI1Z2@containers-us-west-128.railway.app:5977/railway

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'railway',
        'USER':'root',
        'PASSWORD':'yuGOcn8sRcUBrtHAI1Z2',
        'HOST':'containers-us-west-128.railway.app',
        'PORT':'5977',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / "archivos"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = "/archivos/"
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"
""" STATICFILES_DIRS = [
    'proyectos/static/'
] """

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

""" MESSAGES_TAGS = {
    mensajes.DEBUG  :"debug",
    mensajes.ERROR  :"danger",
    mensajes.INFO   :"info",
    mensajes.SUCCESS:"success",
    mensajes.WARNING:"warning",
} """



