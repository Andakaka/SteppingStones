"""
Django settings for stepping_stones project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import matplotlib

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3lzrlzp12i&!y4-ymzk8z3mwvcr1&=jf5nplr+q_&@kr*tnt!*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'event_tracker.apps.EventTrackerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_bootstrap5',
    'djangoplugins',
    'cobalt_strike_monitor.apps.CobaltStrikeMonitorConfig',
    'background_task',
    'fontawesomefree',
    'taggit',
    'reversion',
    'taggit_bulk',
    'graphical_reports',
    'html_reports',
    'markdown_reports',
    'external_tool_reports',
]

MIDDLEWARE = [
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'event_tracker.middleware.TimezoneMiddleware',
    'event_tracker.middleware.InitialConfigMiddleware',
    'csp.middleware.CSPMiddleware',
    'django_permissions_policy.PermissionsPolicyMiddleware',
]

ROOT_URLCONF = 'stepping_stones.urls'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/event-tracker/1'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'event_tracker.context_processors.theme.apply_theme'
            ],
        },
    },
]

WSGI_APPLICATION = 'stepping_stones.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 20,  # Increase from default of 5 to avoid locked DB errors
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = ['https://*.example.net','http://127.0.0.1']

USE_X_FORWARDED_HOST = True
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]', '.example.net']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

BACKGROUND_TASK_RUN_ASYNC = True
BACKGROUND_TASK_ASYNC_THREADS = 50  # Can't expect to exceed 50 team servers
MAX_RUN_TIME = 60 * 60 * 24 * 365 * 10  # 10 years

TAGGIT_CASE_INSENSITIVE = True

REFERRER_POLICY = "same-origin"

CSP_DEFAULT_SRC = ("'none'",)
CSP_SCRIPT_SRC_ELEM = ("'self'", "cdnjs.cloudflare.com", "cdn.datatables.net", "cdn.jsdelivr.net", "unpkg.com", "api.ipify.org")
CSP_STYLE_SRC_ELEM = ("'self'", "cdnjs.cloudflare.com", "cdn.datatables.net", "cdn.jsdelivr.net", "fonts.googleapis.com",)
CSP_FONT_SRC = ("'self'", "fonts.gstatic.com")
CSP_IMG_SRC = ("'self'", "data:", "cdnjs.cloudflare.com")
CSP_CONNECT_SRC = ("'self'",)
CSP_INCLUDE_NONCE_IN = ['script-src-elem', 'style-src-elem']
CSP_FRAME_ANCESTORS = ("'self'",)
CSP_MANIFEST_SRC = ("'self'",) # Hash of http://127.0.0.1:8000/static/favicons/site.webmanifest generated by https://report-uri.com/home/hash/
CSP_FRAME_SRC = ("'self'",)

PERMISSIONS_POLICY = {
    "accelerometer": [],
    "ambient-light-sensor": [],
    "autoplay": [],
    # "battery": [],
    "camera": [],
    "display-capture": [],
    "document-domain": [],
    "encrypted-media": [],
    "execution-while-not-rendered": [],
    "execution-while-out-of-viewport": [],
    "fullscreen": [],
    "gamepad": [],
    "geolocation": [],
    "gyroscope": [],
    "hid": [],
    "identity-credentials-get": [],
    "idle-detection": [],
    "local-fonts": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "otp-credentials": [],
    "payment": [],
    "picture-in-picture": [],
    # "publickey-credentials-create": [],
    # "publickey-credentials-get": [],
    "screen-wake-lock": [],
    "serial": [],
    "speaker-selection": [],
    "storage-access": [],
    "usb": [],
    "web-share": [],
    "xr-spatial-tracking": [],
}

# Define backend for matplotlib. Ensure a non-interactive backend is chosen to avoid dangling resources
matplotlib.use('agg')
