#!/usr/bin/python3
"""
 script that takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument,
 this time, write one that is safe from MySQL injections
"""
import MySQLdb
import sys


if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    name_searched = sys.argv[4]
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s\
                 ORDER BY states.id ASC", (name_searched, ))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
