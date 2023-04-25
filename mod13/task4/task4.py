import sqlite3
get_sql = """
SELECT *
    FROM 'table_effective_manager'
    WHERE name = ?"""

update_sql = """
UPDATE table_effective_manager
SET salary = ?
WHERE name = ?
"""

delete_sql = """
DELETE
    FROM 'table_effective_manager'
    WHERE name = ?
   """

def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str,):
    cursor.execute(get_sql, (name,))
    people = cursor.fetchone()
    if (name != 'Иван Совин'):
        if people[2] * 1.1 <= sovin:
            cursor.execute(update_sql, (people[2] * 1.1, people[1],))
        elif people[2] * 1.1 > sovin:
            cursor.execute(delete_sql, (people[1],))
        return (people[2] * 1.1)
    else:
        return 'Я и есть Иван Совин'



if __name__ == '__main__':
    with sqlite3.connect('../hw.db') as conn:
        Sovin_salary = """SELECT salary FROM 'table_effective_manager' WHERE name = 'Иван Совин'"""
        cursor = conn.cursor()
        cursor.execute(Sovin_salary)
        sovin = cursor.fetchone()[0]
        print(ivan_sovin_the_most_effective(cursor, 'Иван Совин'))
