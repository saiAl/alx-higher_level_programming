#!/usr/bin/python3

""" 0. Get all states """
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC;")
    for r in cur.fetchall():
        print(r)
