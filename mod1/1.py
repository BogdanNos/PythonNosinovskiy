from flask import Flask
import random
import datetime
import os
import re

app = Flask(__name__)
cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt') 

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def cars_function():
    return ', '.join(cars)

@app.route('/cats')
def cats_function():
    return random.choice(cats)

@app.route('/get_time/now')
def now_function():
    return 'Точное время: %s' % datetime.datetime.now()

@app.route('/get_time/future')
def future_function():
    return 'Точное время через час будет %s' % (datetime.datetime.now() + datetime.timedelta(hours=1))

@app.route('/get_random_word')
def get_random_word():
    return random.choice(word)

def get_word():
    with open(BOOK_FILE) as book:
        withoutTags = re.sub(r'[^\w\s]','', book.read()) 
        return withoutTags.split()

word = get_word()

counter_visits = 0
@app.route('/counter')
def counter():
    global counter_visits
    counter_visits += 1 
    return str(counter_visits)

if __name__ == '__main__':
    app.run(debug=True)