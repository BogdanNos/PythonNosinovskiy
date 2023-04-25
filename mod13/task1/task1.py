import sqlite3

get_sql = """
SELECT COUNT(*)
    FROM 'table_truck_with_vaccine'
    WHERE truck_number = ? AND (temperature_in_celsius NOT BETWEEN 16 AND 20) """


def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, truck_number: str) -> bool:
    cursor.execute(get_sql, (truck_number,))
    result = cursor.fetchone()
    if result[0] >= 3:
        return True
    return False

if __name__ == '__main__':
    with sqlite3.connect('../hw.db') as conn:
        cursor = conn.cursor()
        print(check_if_vaccine_has_spoiled(cursor, 'а496ар77'))
