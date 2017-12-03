# -*- coding:utf-8 -*-
"""
Django settings for yangyanghuashi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jqj@s4j(%&dv6oh91)pqihe=xh0kc^3$^oe-ume)z^*_poih=l'

# SECURITY WARNING: don't run with debug turned on in production!

STORAGE_BUCKET_NAME = 'media'

TEMPLATE_DIRS = (
    BASE_DIR + '/studio/template',
    BASE_DIR + '/upload/template',
    BASE_DIR + '/register/template',
    BASE_DIR + '/mycomments/template',    
)
#  最好每个APP都有自己存放模版的文件夹

ALLOWED_HOSTS = '*'


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'studio',
    'upload',
    'register',
    'threadedcomments',
    'django_comments',
    'django.contrib.sites',
)

COMMENTS_APP = 'threadedcomments'

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'yangyangstudio.urls'  # 指明配置url的文件

WSGI_APPLICATION = 'yangyangstudio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
# 自己访问自己的时候，打开调试模式，并使用本地sqlite数据库
# 否则，关闭调试模式，使用服务器的mysql
# if socket.gethostname() != 'DELL-EDDIE':
#     import sae.const

#     FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
#     DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'

#     DEBUG = False
#     TEMPLATE_DEBUG = False
    
#     MYSQL_DB = sae.const.MYSQL_DB 
#     MYSQL_USER = sae.const.MYSQL_USER 
#     MYSQL_PASS = sae.const.MYSQL_PASS 
#     MYSQL_HOST_M = sae.const.MYSQL_HOST 
#     MYSQL_HOST_S = sae.const.MYSQL_HOST_S 
#     MYSQL_PORT = sae.const.MYSQL_PORT

#     DATABASES = {
#         'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': MYSQL_DB,
#         'USER': MYSQL_USER,
#         'PASSWORD': MYSQL_PASS,
#         'HOST': MYSQL_HOST_M,
#         'PORT': MYSQL_PORT,
#         }
#     }
# else:
DEBUG = True
TEMPLATE_DEBUG = True
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'testdb.sqlite'),
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

STATIC_URL = '/static/'
#  STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)
#  it's better to use relevant path for possible system change
#  '\\' means \ in windows path

ADMIN = (
    ('Eddie Chiu', 'eddiechiu77@sina.com'),
)
