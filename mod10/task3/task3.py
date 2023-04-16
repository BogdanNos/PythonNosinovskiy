import sqlite3

with sqlite3.connect('hw_3_database.db') as conn:
    cursor = conn.cursor()

    # Задание 1
    for number in range(1, 4):
        cursor.execute(f'SELECT COUNT (id) FROM table_{number}')
        print(f'Записей в {number} таблице = {cursor.fetchall()[0][0]}')

    # Задание 2
    cursor.execute(f'SELECT COUNT(*) FROM (SELECT DISTINCT * FROM table_1)')
    print(f'В таблице 1 {cursor.fetchall()[0][0]} уникальных записей')

    # Задание 3
    cursor.execute(f'SELECT COUNT(*) FROM (SELECT * FROM table_1 INTERSECT SELECT * FROM table_2)')
    print(f'Из таблицы table_1 встречается {cursor.fetchall()[0][0]} записей в table_2')

    # Задание 4
    cursor.execute(f'SELECT COUNT(*) FROM (SELECT * FROM table_1 INTERSECT SELECT * FROM table_2 INTERSECT SELECT * FROM table_3)')
    print(f'Из таблицы table_1 встречается {cursor.fetchall()[0][0]} записей и в table_2 и в table_3')
