#!/usr/bin/python3
"""
This Script takes in a state as argument and lists all cities of
that state.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    query = """
        SELECT cities.name FROM cities LEFT JOIN states ON
        states.id = cities.state_id WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))

    cur.close()
    conn.close()
