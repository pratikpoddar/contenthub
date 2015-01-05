from .settings_base import *

BASE_URL = 'http://chub.herokuapp.com'
BASE_URL = 'http://www.chub.com'

DEBUG = False
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'chub.tech@chub.com'
EMAIL_HOST_PASSWORD = 'chub12345'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'chub.tech@chub.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

FAILED_RUNS_CRONJOB_EMAIL_PREFIX = "[Chub Production Django - Cron Job] "
EMAIL_SUBJECT_PREFIX = "[Chub Production Django] "

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = 'xxxxxxxxxxxxxxx'     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = 'chub'


ES_URL = 'https://xxxxxx:xxxxxx@xxxxxx.us-east-1.bonsai.io:443/'
ES_HEADER = [{'host': 'xxxx.xxxxx.bonsai.io', 'port': 443, 'use_ssl': True, 'http_auth': ('xxxxx', 'xxxxxxxx')}]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': 'chub_production - [%(name)s]- %(levelname)s- %(asctime)s '
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

REQUEST_CACHING_SIZE=1024

SESSION_COOKIE_DOMAIN = 'chub.com'
