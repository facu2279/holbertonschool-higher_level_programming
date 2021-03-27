#!/usr/bin/python3
"""Lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS,
                         db=MY_DB, port=3306, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' \
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    db.close()
    cur.close()