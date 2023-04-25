import sqlite3
import csv

get_sql = """
DELETE
    FROM 'table_fees'
    WHERE truck_number = ? AND timestamp = ?
   """


def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(f'../{wrong_fees_file}') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for line in spamreader:
            cursor.execute(get_sql, (line[0], line[1],))

if __name__ == '__main__':
    with sqlite3.connect('../hw.db') as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, 'wrong_fees.csv')