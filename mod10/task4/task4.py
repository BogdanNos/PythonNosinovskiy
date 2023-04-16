import sqlite3

with sqlite3.connect('hw_4_database.db') as conn:
    cursor = conn.cursor()

    # Задание 1
    cursor.execute(f'SELECT COUNT(*) FROM salaries WHERE (salary < 5000)')
    print(f'За чертой бедности находятся {cursor.fetchall()[0][0]} людей')

    # Задание 2
    cursor.execute(f'SELECT AVG(salary) FROM salaries')
    print(f'Средняя зарплата по острову: {cursor.fetchall()[0][0]}')

    # Задание 3
    cursor.execute(f'SELECT salary FROM salaries ORDER BY salary')
    array = cursor.fetchall()
    print(f'Медианная зарплата: {array[(len(array)) // 2][0]}')

    # Задание 4
    cursor.execute(f'SELECT COUNT(*) FROM salaries')
    total = cursor.fetchall()[0][0]
    cursor.execute(f'SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1 * {total})')
    T = cursor.fetchall()[0][0]
    cursor.execute(f'SELECT SUM(salary) - {T} FROM salaries')
    K = cursor.fetchall()[0][0]
    print(f'F = {round(T / K * 100, 2)}%')
