# TO RUN PROGRAM type following in terminal and click return:
# FIRST: python load_pets.py
# SECOND: python query_pets.py

import sqlite3

connection = sqlite3.connect("pets.db")
crsr = connection.cursor()

def get_person_data(person_id):
    get_person = crsr.execute("""
        SELECT person.first_name, person.last_name, person.age
        FROM person
        WHERE person.id=?
        """,
        str(person_id))

    get_person_results = get_person.fetchone()

    return get_person_results

def get_pet_data(pet_id):
    get_pet = crsr.execute("""
        SELECT pet.name, pet.breed, pet.age
        FROM pet
        WHERE pet.id=?
        """,
        str(pet_id))

    get_pet_results = get_pet.fetchone()
    return get_pet_results

def get_owner_data(person_id):
    results = []
    get_person_pet = crsr.execute("""
        SELECT *
        FROM person_pet
        WHERE person_pet.person_id=?
        """,
        str(person_id))

    get_person_pet_results = get_person_pet.fetchall()
    get_person_pet_length = len(get_person_pet_results)

    if get_person_pet_length > 1:
        for person in get_person_pet_results:
            get_person_results = get_person_data(person_id)
            get_pet_results = get_pet_data(person[1])
            person_statment = '%s %s, %s years old'%(get_person_results[0], get_person_results[1], get_person_results[2])
            person_pet_statement = '%s %s owned %s, a %s, that was %s years old'%(
                get_person_results[0],
                get_person_results[1],
                get_pet_results[0],
                get_pet_results[1],
                get_pet_results[2]
                )
            if len(results) == 0:
                results.append(person_statment)

            results.append(person_pet_statement)
    elif get_person_pet_length == 0:
        return None
    else:
        get_person_results = get_person_data(person_id)
        get_pet_results = get_pet_data(person_id)

        person_statment = '%s %s, %s years old'%(get_person_results[0], get_person_results[1], get_person_results[2])
        person_pet_statement = '%s %s owned %s, a %s, that was %s years old'%(
            get_person_results[0],
            get_person_results[1],
            get_pet_results[0],
            get_pet_results[1],
            get_pet_results[2]
            )
        results.append(person_statment)
        results.append(person_pet_statement)

    return results

if __name__ == '__main__':
    person_id = 0
    while person_id != -1:
        person_id = int(raw_input("Enter a person's ID number: "))
        if person_id < 0:
            print('You have decided to quit this program, Till Next Time.')
            break
        returned_data = get_owner_data(person_id)
        if returned_data:
            for item in returned_data:
                print(item)
        else:
            print('ERROR: Sorry, there is no user with that ID at this time.')

        print('NOTE: To Quit Program type -1 and click return')
