import multiprocessing
import requests
import time
import sqlite3
import threading
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool

peoples = []
URL = 'https://swapi.dev/api/people/'
sql_req = """INSERT INTO characters (name, birth_year, gender) VALUES (?,?,?)"""

def get_peoples(i: int):
    global peoples
    response = requests.get(URL+str(i))
    if response.status_code == 200:
        people_dict = dict(response.json())
        peoples.append((people_dict["name"], people_dict["birth_year"], people_dict["gender"]))
        return (people_dict["name"], people_dict["birth_year"], people_dict["gender"])

def load_peoples_pool():
    start = time.time()
    with Pool(processes=cpu_count()) as pool:
        result = list(pool.map(get_peoples, range(22)))
        for x in result:
            if x == None:
                result.pop(result.index(None))
        cursor.executemany(sql_req, result)
        print("Time is {:4}".format(time.time() - start))

def load_peoples_threadpool():
    start = time.time()
    with ThreadPool(processes=cpu_count()) as pool:
        pool.map(get_peoples, range(22))
        cursor.executemany(sql_req, peoples)
        print("Time is {:4}".format(time.time() - start))

if __name__ == "__main__":
    with sqlite3.connect('star_wars.db') as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE characters")
        cursor.execute("CREATE TABLE characters (name text, birth_year text, gender text)")
        load_peoples_pool()
        #load_peoples_threadpool()