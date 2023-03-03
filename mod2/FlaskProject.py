from flask import Flask
from datetime import datetime
import os
day = ['Хорошего вторника!', 'Хорошей среды!', 'Хорошего четверга!', 'Хорошей пятницы!', 'Хорошей субботы!', 'Хорошего воскременья!']
salary = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/hello-world/<name>')
def hello(name):
    weekday = datetime.today().weekday()
    return f'Привет, {name}. {day[weekday]}'

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    max = 0
    for number in numbers.split('/'):
        try: int(number)
        except: return 'Вы ввели не число'
        if (int(number) > max):
            max = int(number)
    return f'Максимальное число: <i>{max}</i>'

@app.route('/preview/<int:SIZE>/<path:RELATIVE_PATH>')
def relative_preview(SIZE, RELATIVE_PATH):
    abs_path = os.path.join(BASE_DIR, RELATIVE_PATH)
    with open(abs_path) as file:
        file = file.read(SIZE)
        return(f'<b>{RELATIVE_PATH}</b> {SIZE} <br> {file}')

@app.route('/add/<date>/<int:number>')
def addNumber(date, number):
    try:
        salary.setdefault(int(date[0:4]), {}).setdefault(int(date[4:6]), 0)
        salary[int(date[0:4])][int(date[4:6])] += number
    except: return 'Неверный ввод'
    return f'Добавлена информация о трате'

@app.route('/calculate/<int:year>')
def calculateYear(year):
    return str(sum(salary[year].values()))

@app.route('/calculate/<int:year>/<int:month>')
def calculateMounth(year, month):
    return str(salary[year][month])


if __name__ == '__main__':
    app.run(debug=True)