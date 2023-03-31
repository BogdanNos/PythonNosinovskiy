import logging
import sys
from utils import *
from fileHandler import *
logger = logging.getLogger("app")

#Задание 3
multi_file_handler = MultiFileHandler()
logger.addHandler(multi_file_handler)

#Задание 1-2
custom_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(custom_handler)
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s")
custom_handler.setFormatter(formatter)

def app():
    choose = input('Выберите: умножение или сложение ')
    example = input("Введите выражение: ")
    if (choose == 'сложение'):
        result = plus(example)
        return f"{example} = {result}"
    elif (choose == 'умножение'):
        result = multiplication(example)
        return f"{example} = {result}"

    logger.error(f'Введите верную операцию')

if(__name__ == '__main__'):
    print(app())