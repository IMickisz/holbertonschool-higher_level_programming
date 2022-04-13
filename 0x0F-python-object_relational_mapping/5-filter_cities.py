#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC", (argv[4],))
    rows = cursor.fetchall()
    array = []
    for row in rows:
        array.append(row[0])
    print(", ".join(array))
    cursor.close()
    db.close()