#!/usr/bin/python3
""" SQL Injection... """
import sys
import MySQLdb


def filter_by_usr_input_safe():
    """ script that takes in an argument and displays all values
        safe from MySQL injections """
    try:
        usr_input = sys.argv[4]
        with MySQLdb.connect(
            "localhost", sys.argv[1], sys.argv[2], sys.argv[3], port=3306
                ) as db:
            with db.cursor() as cur:
                cur.execute("SELECT *FROM states ORDER BY id ASC;")
                for r in cur.fetchall():
                    if (r[1] == usr_input):
                        print(r)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    filter_by_usr_input_safe()
