import sqlite3


conn = sqlite3.connect('test_sqlite.db')
curs = conn.cursor()
"""
curs.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit
curs.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()
"""

curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike"')
conn.commit()

print(curs.fetchall())
curs.close()
conn.close()