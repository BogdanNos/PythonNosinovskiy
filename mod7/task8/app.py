import logging
import sys
from utils import *
import logging.config
import logging_tree
from logging_config import dict_config

logging.config.dictConfig(dict_config)

logger = logging.getLogger("logger.app")

def app():
    choose = input('Выберите: умножение или сложение ')
    example = input("Введите выражение: ")
    if (choose == 'сложение'):
        result = plus(example)
        return f"{example} = {result}"
    elif (choose == 'умножение'):
        result = multiplication(example)
        return f"{example} = {result}"

    logger.error(f'Enter the correct operation')

if(__name__ == '__main__'):
    print(app())