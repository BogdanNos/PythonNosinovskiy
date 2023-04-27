import sqlite3

ENABLE_FOREIGN_KEY = "PRAGMA foreign_keys = ON;"

CREATE_actors_TABLE = """
DROP TABLE IF EXISTS 'actors';
CREATE TABLE 'actors' (
    act_id INTEGER PRIMARY KEY AUTOINCREMENT,
    act_first_name VARCHAR(50) NOT NULL,
    act_last_name VARCHAR(50) NOT NULL,
    act_gender VARCHAR(1) NOT NULL
)
"""

CREATE_movie_TABLE = """
DROP TABLE IF EXISTS 'movie';
CREATE TABLE 'movie' (
    mov_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_title VARCHAR(50) NOT NULL
);
"""

CREATE_director_TABLE = """
DROP TABLE IF EXISTS 'director';
CREATE TABLE 'director' (
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dir_first_name VARCHAR(50) NOT NULL,
    dir_last_name VARCHAR(50) NOT NULL
);
"""

"""act_id -> actors (act_id) многие к одному
mov_id -> movie (mov_id) многие к одному"""

CREATE_TABLE_movie_cast = """
DROP TABLE IF EXISTS 'movie_cast';
CREATE TABLE 'movie_cast' (
    act_id REFERENCES actors(act_id) ON DELETE CASCADE,
    mov_id REFERENCES movie(mov_id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL
)
"""

"""mov_id -> movie (mov_id) многие к одному"""

CREATE_TABLE_oscar_awarded = """
DROP TABLE IF EXISTS 'oscar_awarded';
CREATE TABLE 'oscar_awarded' (
    award_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mov_id REFERENCES movie(mov_id) ON DELETE CASCADE
)
"""

"""mov_id -> movie (mov_id) один к одному
dir_id -> director (dir_id) многие к одному"""

CREATE_TABLE_movie_direction = """
DROP TABLE IF EXISTS 'movie_direction';
CREATE TABLE 'movie_direction' (
    dir_id REFERENCES director(dir_id) ON DELETE CASCADE,
    mov_id REFERENCES movie(mov_id) ON DELETE CASCADE
)
"""

def create_tables() :
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.executescript(CREATE_actors_TABLE)
        cursor.executescript(CREATE_movie_TABLE)
        cursor.executescript(CREATE_director_TABLE)
        cursor.executescript(CREATE_TABLE_movie_cast)
        cursor.executescript(CREATE_TABLE_oscar_awarded)
        cursor.executescript(CREATE_TABLE_movie_direction)
        cursor.executescript(ENABLE_FOREIGN_KEY)

if __name__ == "__main__":
    create_tables()