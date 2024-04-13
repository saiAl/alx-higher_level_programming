#!/usr/bin/python3
""" 2. Filter states by user input """
import sys
import MySQLdb


def filter_by_usr_input():
    """ script that takes in an argument and displays all values """
    with MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]) as db:
        with db.cursor() as cur:
            cur.execute("""SELECT id, name FROM states
            WHERE name LIKE %s""", (sys.argv[4],))
            for r in cur.fetchall():
                print(r)


if '__name__' == '__main__':
    filter_by_usr_input()
