#!/usr/bin/python3
""" 2. Filter states by user input """
import sys
import MySQLdb


def filter_by_usr_input():
    """ script that takes in an argument and displays all values """
    usr_input = sys.argv[4]
    with MySQLdb.connect(
            "localhost", sys.argv[1], sys.argv[2],
            sys.argv[3], port=3306
            ) as db:
        with db.cursor() as cur:
            cur.execute("""SELECT id, name FROM states
            WHERE name = BINARY '{:s}' ORDER BY id ASC;""".format(usr_input))
            for r in cur.fetchall():
                print(r)


if '__name__' == '__main__':
    filter_by_usr_input()
