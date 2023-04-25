import datetime
import sqlite3

hobbies = {"Monday": "футбол",
        "Tuesday": "хоккей",
        "Wednesday": "шахматы",
        "Thursday": "SUP сёрфинг",
        "Friday": "бокс",
        "Saturday": "Dota2",
        "Sunday": "шах-бокс"}

def update_work_schedule(cursor: sqlite3.Cursor) -> None:
    cursor.execute("DELETE FROM 'table_friendship_schedule'")
    today = datetime.datetime(year=2020, month=1, day=1)
    employee_worker = {}
    for day in range(366):
        count_worker_in_one_day = 0
        for person in range(1, cursor.execute("SELECT COUNT (*) FROM 'table_friendship_employees'").fetchall()[0][0] + 1):
            if (person not in employee_worker.keys() or employee_worker[person] < 11) and hobbies[today.strftime('%A')] != cursor.execute(f"SELECT * FROM 'table_friendship_employees' WHERE id = ?", (person,)).fetchall()[0][2]:
                cursor.execute("INSERT INTO 'table_friendship_schedule' (employee_id, date) VALUES (?, ?) ", (person, today.date(),))
                if person in employee_worker.keys():
                    employee_worker[person] += 1
                else:
                    employee_worker[person] = 1
                count_worker_in_one_day += 1
            if count_worker_in_one_day == 10:
                break
        today += datetime.timedelta(days=1)

if __name__ == "__main__":
    with sqlite3.connect("../hw.db") as conn:
        cursor = conn.cursor()
        update_work_schedule(cursor)