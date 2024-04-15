#!/usr/bin/python3

""" 0. Get all states """
import MySQLdb
import sys


if '__name__' == '__main__':
    try:
        with MySQLdb.connect(
                host="localhost", user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], port=3306
        ) as db:
            with db.cursor() as cur:
                cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
                for r in cur.fetchall():
                    print(r)
    except Exception as err:
        print(err)
        exit(1)
