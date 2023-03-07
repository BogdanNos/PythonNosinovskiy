from flask import Flask
from datetime import datetime

day = ['Хорошего понедельник!', 'Хорошего вторника!', 'Хорошей среды!', 'Хорошего четверга!', 'Хорошей пятницы!', 'Хорошей субботы!', 'Хорошего воскреcенья!']
app = Flask(__name__)

@app.route('/hello-world/<name>')
def hello(name):
    weekday = datetime.today().weekday()
    return f'Привет, {name}. {day[weekday]}'

if __name__ == '__main__':
    app.run(debug=True)