#!/usr/bin/python3
""" 5. All cities by state """
import sys
import MySQLdb


def all_cities():
    """
        script that takes in the name of a state
            as an argument and lists all cities of that state
    """
    try:
        state_name = sys.argv[4]
        with MySQLdb.connect(
                "localhost", sys.argv[1], sys.argv[2], sys.argv[3]
                ) as db:
            with db.cursor() as cur:
                cur.execute("""
                        SELECT cities.name
                        FROM cities INNER JOIN states
                        ON cities.state_id = states.id
                        WHERE states.name = %s ORDER BY cities.id ASC;
                        """, (state_name,))

                print(", ".join([s[0] for s in cur.fetchall()]))
    except Exception as err:
        print(err)
        exit(1)


if __name__ == '__main__':
    all_cities()
