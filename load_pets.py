# TO RUN PROGRAM type following in terminal and click return:
# python load_pets.py

import sqlite3
import os
import time


os.remove("pets.db")
# connecting to the database
print('Creating database....')
time.sleep(2)
print('Connecting to database...')
time.sleep(2)
print('Connected!')
connection = sqlite3.connect("pets.db")


crsr = connection.cursor()

sql_table = ("""
        CREATE TABLE person(
          id INTEGER PRIMARY KEY,
          first_name TEXT,
          last_name TEXT,
          age INTEGER
        );

        CREATE TABLE pet(
          id INTEGER PRIMARY KEY,
          name TEXT,
          breed TEXT,
          age INTEGER,
          dead INTEGER
        );

        CREATE TABLE person_pet(
          person_id INTEGER,
          pet_id INTEGER
        );
    """);


crsr.executescript(sql_table)


sql_add_person_command = "INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?)"
person_val = [
  (1,'James', 'Smith', 41),
  (2,'Diana', 'Greene', 23),
  (3, 'Sara', 'White', 27),
  (4, 'William', 'Gibson',23)
]

crsr.executemany(sql_add_person_command, person_val)

sql_add_pet_command = "INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?)"
pet_val = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'AlaskanMalamute', 3, 0),
    (3, 'Max', 'CockerSpaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'CockerSpaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

crsr.executemany(sql_add_pet_command, pet_val)

sql_add_person_to_pet = "INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?)"

person_pet_val = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

crsr.executemany(sql_add_person_to_pet, person_pet_val)

connection.commit()

connection.close()
