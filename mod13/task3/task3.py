import sqlite3

def log_bird(cursor: sqlite3.Cursor, bird_name: str, date_time: str,) -> None:
    cursor.execute(f"INSERT INTO 'birds' (bird_name, date_time) VALUES ('{bird_name}', '{date_time}');")


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    cursor.execute(f"SELECT COUNT(*) FROM 'birds' WHERE bird_name = '{bird_name}'")
    result = cursor.fetchone()
    if result[0] >= 1:
        return True
    return False


if __name__ == '__main__':
    with sqlite3.connect('bird.db') as conn:
        cursor = conn.cursor()
        log_bird(cursor, 'Воробей', '28.03.2022')
        print(check_if_such_bird_already_seen(cursor, 'голубь'))