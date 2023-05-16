import requests
import time
import sqlite3
import threading

peoples = []
URL = 'https://swapi.dev/api/people/'
sql_req = """INSERT INTO characters (name, birth_year, gender) VALUES (?,?,?)"""

def get_peoples(url: str, i: int):
    global peoples
    response = requests.get(url+str(i))
    if response.status_code == 200:
        people_dict = dict(response.json())
        peoples.append((people_dict["name"], people_dict["birth_year"], people_dict["gender"]))

def load_peoples():
    global peoples
    start = time.time()
    for i in range(21):
        get_peoples(URL, i + 1)
    cursor.executemany(sql_req, peoples)
    print("Time is {:4}".format(time.time() - start))

def load_peoples_threads():
    global peoples
    start = time.time()
    threads = []
    for i in range(21):
        thread = threading.Thread(target=get_peoples, args=(URL, i + 1))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    cursor.executemany(sql_req, peoples)
    print("Time is {:4}".format(time.time() - start))

if __name__ == "__main__":
    with sqlite3.connect('star_wars.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE characters")
        cursor.execute("CREATE TABLE characters (name text, birth_year text, gender text)")
        load_peoples()
        #load_peoples_threads()