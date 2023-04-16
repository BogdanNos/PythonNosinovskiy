import sqlite3

with sqlite3.connect('hw_2_database.db') as conn:
    cursor = conn.cursor()

    #Задание 1
    cursor.execute('SELECT * FROM table_checkout ORDER BY sold_count DESC')
    res = cursor.fetchall()
    print(f'Телефоны {res[0][0]} цвета чаще всего покупают')

    #Задание 2
    cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Red'")
    red = cursor.fetchall()[0]

    cursor.execute("SELECT * FROM table_checkout WHERE phone_color = 'Blue'")
    blue = cursor.fetchall()[0]

    if red[1] > blue[1]:
        print('Чаще покупают красные телефоны')
    elif blue[1] > red[1]:
        print('Чаще покупают синие телефоны')
    else: print('телефоны продаются одинаково')

    #Задание 3
    cursor.execute('SELECT * FROM table_checkout ORDER BY sold_count')
    res = cursor.fetchall()
    print(f'Телефоны {res[0][0]} цвета самый непопулрный')