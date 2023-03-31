import sys
import string
import logging

#Задание 7
class IsASCII(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        return all(c in string.printable for c in msg)

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        }
    },
    "filters": {
        "ascii_filter": {
            "()": IsASCII
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "when": 'h',
            "interval": 10,
            "backupCount": 1,
            "formatter": "base",
            "filename": "utils.log",
            "filters": ["ascii_filter"]
        }
    },
    "loggers": {
        "logger": {
            "level": "INFO",
            "handlers": ["file"],
        }
    },
}
