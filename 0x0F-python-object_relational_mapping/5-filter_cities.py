#!/usr/bin/python3
""" 5. All cities by state """
import sys
import MySQLdb


def all_cities():
    """
        script that takes in the name of a state
            as an argument and lists all cities of that state
    """
    state_list = []
    s = ''
    try:
        state_name = sys.argv[4]
        with MySQLdb.connect(
                "localhost", sys.argv[1], sys.argv[2], sys.argv[3]
                ) as db:
            with db.cursor() as cur:
                cur.execute("""
                        SELECT cities.id, cities.name, states.name
                        FROM cities INNER JOIN states
                        ON cities.state_id = states.id ORDER BY id;
                        """)
                for r in cur.fetchall():
                    if (r[2] == state_name):
                        state_list.append(r[1])

                if (len(state_list) == 0):
                    print()
                else:
                    for idx, value in enumerate(state_list):
                        if idx < (len(state_list) - 1):
                            print(value, end=', ')
                        else:
                            print(value)
    except Exception as err:
        print(err)
        exit(1)


if '__name__' == '__main__':
    all_cities()
