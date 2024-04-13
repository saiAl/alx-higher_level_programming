#!/usr/bin/python3
""" 1. Filter states """
import sys
import MySQLdb


def filter():
    """ script that lists all states with a name starting with N """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name Like 'N%';")
    for r in cur.fetchall():
        print(r)


if '__name__' == '__main__':
    filter()
