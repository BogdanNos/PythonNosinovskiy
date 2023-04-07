import logging
import sys
import logging.config
from logging_config import dict_config
logging.config.dictConfig(dict_config)

logger = logging.getLogger("logger.calculate")

def plus(example):
    try:
        logger.debug(f'Начало работы программы плюс {example}')
        result = int(example.split('+')[0]) + int(example.split('+')[1])
        logger.debug(f"Результат плюса: {example} = {result}")
        return result
    except: logger.error(f'Неправильный формат ввода')

def multiplication(example):
    try:
        logger.debug(f'Начало работы программы умножение {example}')
        result = int(example.split('*')[0]) * int(example.split('*')[1])
        logger.debug(f"Результат умножения: {example} = {result}")
        return result
    except: logger.error(f'Неправильный формат ввода')