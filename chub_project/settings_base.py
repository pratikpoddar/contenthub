"""
Django settings for chub_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
DATABASES = {}
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = os.environ["SECRET_KEY"]

SECRET_KEY = '8mmb3@eb439c2)(3d^pk(q#k-hz7n^cem28u-3!zu8=4e#x*lm'

# SECURITY WARNING: don't run with debug turned on in production!

SPIRALPASSWORD = '!QAZ@WSX1qaz2wsx'

ADMINS = (
    ('Ankit Agarwal', 'ankitagarwal24.8@gmail.com'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']

FAILED_RUNS_CRONJOB_EMAIL_PREFIX = "[Chub Django - Cron Job] "
EMAIL_SUBJECT_PREFIX = "[Chub Django] "

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'chub_db',
#         'USER': 'chub_user',
#         'PASSWORD': '12345678',
#         'HOST': 'localhost',
#         'PORT': '', # Set to empty string for default.
#     }
# }


# SESSION_COOKIE_DOMAIN = None
CSRF_COOKIE_DOMAIN = None
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_COOKIE_AGE = 86400

LOGOUT_TIME = '2014-12-04 13:16:56.758050'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chub',
    'south',
    'widget_tweaks',
    'django.contrib.humanize',
    'storages',
    'mathfilters',
    'pipeline',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'chub_project.middleware.error500Middleware',
    'chub_project.middleware.log_requests_Middleware',
    'chub_project.middleware.logout_all_users'
)

ROOT_URLCONF = 'chub_project.urls'

WSGI_APPLICATION = 'chub_project.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

USE_X_FORWARDED_HOST = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOG_DIR = os.path.join(BASE_DIR, 'chub_log')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


MEDIA_ROOT = os.path.join(BASE_DIR, 'chub/static/chub/media')
MEDIA_URL = '/static/chub/media/'

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'chub/static')
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # os.path.join(BASE_DIR, 'chub/static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

META_SITE_PROTOCOL = 'http'

REQUEST_CACHING_SIZE=0

PIPELINE_YUGLIFY_BINARY = 'vendor/node/bin/node node_modules/yuglify/bin/yuglify'

PIPELINE_CSS = {
    'bootstrapcss': {
        'source_filenames': (
		"chub/css/chub/bootstrap.min.css",
		"chub/css/chub/bootstrap.readable.min.css",
                "chub/css/chub/chosen.bootstrap.css",
 		"chub/css/chub/jquery.fancybox.css",
                "chub/css/chub/fullcalendar.css",
    		"chub/css/chub/datepicker.css",
    		"chub/css/chub/morris-0.5.1.css",
        ),
        'output_filename': 'chub/css/chub/minified-bootstrapcss.css',
    },
}

PIPELINE_JS = {
    'jqueryjs': {
        'source_filenames': (
		"chub/js/chub/jquery.mousewheel-3.0.6.pack.js",
		"chub/js/chub/jquery-ui.js",
		"chub/js/chub/jquery.cookie.js",
		"chub/js/chub/jquery.fancybox.js",
		"chub/js/chub/chosen.jquery.min.js",
		"chub/js/chub/moment.min.js",
		"chub/js/chub/fullcalendar.js",
		"chub/js/chub/raphael-min.js",
		"chub/js/chub/morris-0.5.1.min.js"
        ),
        'output_filename': 'chub/js/chub/minified-jqueryjs.js',
    },
    'bootstrapjs': {
        'source_filenames': (
                "chub/js/chub/bootstrap.js",
                "chub/js/chub/bootstrap-datepicker.js",
        ),
        'output_filename': 'chub/js/chub/minified-bootstrapjs.js',
    },
}

