#!/usr/bin/python3
""" 4. Cities by states """
import sys
import MySQLdb


def list_cities():
    """ script that lists all cities """
    try:
        with MySQLdb.connect(
                "localhost", sys.argv[1], sys.argv[2], sys.argv[3]
                ) as db:
            with db.cursor() as cur:
                cur.execute(
                        """
                        SELECT cities.id, cities.name, states.name
                        FROM cities INNER JOIN states
                        ON cities.state_id = states.id ORDER BY id;
                        """
                        )
                for r in cur.fetchall():
                    print(r)
    except Exception as err:
        print(err)
        exit(1)


if __name__ == '__main__':
    list_cities()
