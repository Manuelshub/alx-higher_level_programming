#!/usr/bin/python3
"""This Script lists all states from a database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    curr = conn.cursor()
    curr.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = curr.fetchall()
    for row in query_rows:
        print(row)

    curr.close()
    conn.close()
