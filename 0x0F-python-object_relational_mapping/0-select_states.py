#!/usr/bin/python3

""" 0. Get all states """
import MySQLdb
import sys


def records():
    """
        script that lists all states from the database hbtn_0e_0_usa

    """
    try:
        with MySQLdb.connect(
                "localhost", sys.argv[1], sys.argv[2], sys.argv[3], port=3306
                ) as db:
            with db.cursor() as cur:
                cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
                for r in cur.fetchall():
                    print(r)
    except Exception as e:
        print(e)
        exit(0)


if '__name__' == '__main__':
    records()
