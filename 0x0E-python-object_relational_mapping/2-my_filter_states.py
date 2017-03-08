#!/usr/bin/python3
'''
This is the '2-filter_states' module

2-filter_states connects to the hbtn_0e_0_usa database and
retrieves the name when specified by the argument passed through
'''

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM states\
        WHERE name = '{:s}' ORDER BY states.id ASC".format(sys.argv[4]))

for info in cur.fetchall():
    print(info)

cur.close()
db.close()