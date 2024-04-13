#!/usr/bin/python3

""" 0. Get all states """
import MySQLdb
import sys


def records():
    """
        script that lists all states from the database hbtn_0e_0_usa

    """

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states")

    for r in cur.fetchall():
        print(r)


if '__name__' == '__main__':
    records()
