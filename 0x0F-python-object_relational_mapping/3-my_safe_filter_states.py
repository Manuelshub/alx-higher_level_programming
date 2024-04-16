#!/usr/bin/python3
"""
This Script displays all values in the table of a database that
matches an argument. And it's safe from SQL injection.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = """SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"""
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
