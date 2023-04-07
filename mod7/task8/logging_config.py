import sys
import string
import logging

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },

    "handlers": {
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "when": 'h',
            "interval": 10,
            "backupCount": 1,
            "formatter": "base",
            "filename": "utils.log",
        },
        'server': {
            "class": "logging.handlers.HTTPHandler",
            "level": "DEBUG",
            "host": 'localhost:5000',
            'url': '/save_log',
            'method': 'POST',
        }
    },
    "loggers": {
        "logger": {
            "level": "DEBUG",
            "handlers": ["file", 'server'],
        }
    },
}
