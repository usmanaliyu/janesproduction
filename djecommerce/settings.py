import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lyyn2(19s^2-^frpynybngc=$w97-$d7b1-%n*bd5pheo@#*_*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG:
    EMAIL_BACKEND = 'django.core.mai.backends.dummy.EmailBackend'


ALLOWED_HOSTS = ['127.0.0.1', '52.188.123.44']

# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'sorl.thumbnail',
    'core',
    'paystack',
    'comments',
    'Account',
    'django_filters',

]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# paystack
# PAYSTACK_PUBLIC_KEY = "pk_live_3b7b32232d4485c95cdc0c50f83acda3b6f523b1"
# PAYSTACK_SECRET_KEY = "sk_live_1c2a919aca68e2a4fb2369cd828972d801a29d80"

PAYSTACK_PUBLIC_KEY = "pk_test_6681e7fc29d2350d6f35f98ae14535747f541783"
PAYSTACK_SECRET_KEY = "sk_test_eb983647781b4cdca3ba3be945637e1585059f71"
ROOT_URLCONF = 'djecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/Users/usmanaliyu/Desktop/janesproduction/templates'],
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

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
WSGI_APPLICATION = 'djecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': 'db.sqlite3',
      }
  }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'janes',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '3308',
#     }
# }

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'myproject',
#        'USER': 'myprojectuser',
#        'PASSWORD': 'password',
#        'HOST': 'localhost',
#        'PORT': '',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'

# CRISPY FORMS


EMAIL_HOST_PASSWORD = 'sogie2020'


CRISPY_TEMPLATE_PACK = 'bootstrap4'
STRIPE_PUBLIC_KEY = ''
STRIPE_SECRET_KEY = ''

#SITE_ID = 1
#LOGIN_REDIRECT_URL = '/'
#SIGNUP_URL = "signup"


# CRISPY FORMS

#CRISPY_TEMPLATE_PACK = 'bootstrap4'
#STRIPE_PUBLIC_KEY = ''
#STRIPE_SECRET_KEY = ''


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'janesfash@gmail.com'
EMAIL_HOST_PASSWORD = "sogie2020"


PAYSTACK_SUCCESS_URL = 'paystack-success/'
PAYSTACK_FAILED_URL = 'paystack-failed/'


SITE_ID = 1
LOGIN_URL = 'login'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = '/'
