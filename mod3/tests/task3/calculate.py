from flask import Flask
import os
salary = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


@app.route('/add/<date>/<int:number>')
def addNumber(date, number):
    try:
        salary.setdefault(int(date[0:4]), {}).setdefault(int(date[4:6]), 0)
        salary[int(date[0:4])][int(date[4:6])] += number
    except: return 'Неверный ввод'
    return f'Добавлена информация о трате'

@app.route('/calculate/<int:year>')
def calculateYear(year):
    try: salary[year]
    except: return 'За данный год не было покупок'
    return str(sum(salary[year].values()))

@app.route('/calculate/<int:year>/<int:month>')
def calculateMounth(year, month):
    try: salary[year][month]
    except: return 'За данный месяц не было покупок'
    return str(salary[year][month])


if __name__ == '__main__':
    app.run(debug=True)