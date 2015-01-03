from .settings_base import *

BASE_URL = 'http://flip.herokuapp.com'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'flip@flip.com'
EMAIL_HOST_PASSWORD = 'flip12345'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'flip@flip.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

FAILED_RUNS_CRONJOB_EMAIL_PREFIX = "[Flip Staging Django - Cron Job] "
EMAIL_SUBJECT_PREFIX = "[Flip Staging Django] "

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = 'xxxxxxxxxxxxx'     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxx' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = 'flip'

ES_URL = 'https://xxxxxxx:xxxxxxxxx@xxxxxxxxxx.xxxx.bonsai.io:443/'
ES_HEADER = [{'host': 'xxxxxxxxxx.xxxxxxxxx.bonsai.io', 'port': 443, 'use_ssl': True, 'http_auth': ('xxxxxxx', 'xxxxxxxxxx')}]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': 'flip_staging - [%(name)s]- %(levelname)s- %(asctime)s '
                      ' %(filename)s: %(lineno)d - %(message)s',
        },
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard',
        },
        'sys_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'standard',
            'address':('logs2.papertrailapp.com', 000000),
        }
    },
    'loggers': {
        '': {
            'handlers': ['sys_log', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

SESSION_COOKIE_DOMAIN = 'spiral-staging.herokuapp.com'

BASICAUTH_USERNAME = 'flip'
BASICAUTH_PASSWORD = 'staging'

MIDDLEWARE_CLASSES += (
    'spiral_project.middleware.BasicAuthMiddleware',
)
