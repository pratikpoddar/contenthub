from .settings_base import *

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    ('Ankit Agarwal', 'ankitagarwal24.8@gmail.com')
)

MANAGERS = ADMINS

BASE_URL = 'http://localhost:8000'

FAILED_RUNS_CRONJOB_EMAIL_PREFIX = "[Ankit Local Flip Django - Cron Job] "
EMAIL_SUBJECT_PREFIX = "[Ankit Local Flip Django] "


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ES_HEADER = [{}]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(name)s]- %(levelname)s- %(asctime)s '
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
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': LOG_DIR + "/debug.log",
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'filename': LOG_DIR + "/error.log",
        },
    },
    'loggers': {
        '': {
            'handlers': ['file_debug', 'file_error', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    # MIDDLEWARE_CLASSES += (
    #     'debug_toolbar.middleware.DebugToolbarMiddleware',
    # )

    # INSTALLED_APPS += (
    #     'debug_toolbar',
    # )


    DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

SESSION_COOKIE_DOMAIN = None

