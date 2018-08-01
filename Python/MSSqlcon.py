#! /usr/bin/env python3
import pymssql
conn = pymssql.connect("gz33b2j2ku.database.windows.net",
                       "OmniTable@gz33b2j2ku", "Oep12345", "Omni_Test")
cursor = conn.cursor()
cursor.execute('SELECT * FROM DIM_BRAND')

for row in cursor:
    print('row = %r' % (row,))

conn.close()
