import sqlite3
import random

def generate_test_data(cursor, number_of_groups):
    cursor.execute("DELETE FROM 'uefa_commands'")
    cursor.execute("DELETE FROM 'uefa_draw'")
    team = ['Челси', 'Сити', 'Юнайтед', 'Атлетико', 'Атлетик', 'ЦСКА', 'Спартак', 'Бавария']
    city = ['Ливерпуль', 'Лондон', 'Барселона', 'Мадрид', 'Мюнхен', 'Манчестер', 'Москва', 'Краснодар']
    countries = ['Russia', 'Germany', 'Spain', 'France', 'Italy', 'Portugal', 'Netherlands', 'England']
    level_names = ['слабая команда', 'средняя команда', 'сильная команда']
    name_teams = []

    while len(name_teams) < number_of_groups * 4:
        generate_name = random.choice(team) + " " + random.choice(city)
        if generate_name not in name_teams:
            name_teams.append(generate_name)
    number = 0
    for group in range(number_of_groups):
        for level_team in range(4):
            number += 1
            level = level_team
            if level_team % 4 == 3:
                level = 1
            cursor.execute("INSERT INTO 'uefa_commands' (command_number, command_name, command_country, command_level) VALUES (?, ?, ?, ?) ", (number, name_teams[number - 1], random.choice(countries), level_names[level],))
            cursor.execute("INSERT INTO 'uefa_draw' (id, command_number, group_number) VALUES (?, ?, ?) ", (number, number, group + 1,))


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        generate_test_data(cursor, 5)
