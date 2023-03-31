import logging
import sys
from fileHandler import *
logger = logging.getLogger("calculate")
logger.setLevel("DEBUG")

#Задание 3
multi_file_handler = MultiFileHandler()
logger.addHandler(multi_file_handler)

#Задание 1-2
custom_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(custom_handler)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")
custom_handler.setFormatter(formatter)

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