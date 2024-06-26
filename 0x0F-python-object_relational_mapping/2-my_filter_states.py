#!/usr/bin/python3
"""This Script displays all values in a table of a database
where the name matches an Argument."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY "{}"\
                ORDER BY states.id ASC""".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
