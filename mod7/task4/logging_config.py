import sys

from fileHandler import *

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "handlers": {
        "custom_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": sys.stdout
        },

        "multi_file_handler": {
            "()": MultiFileHandler,
            "level": "DEBUG",
            "formatter": "base",
            }
    },
    "loggers": {
        "logger": {
            "level": "DEBUG",
            "handlers": ["custom_handler", "multi_file_handler"],
        }
    },
}
