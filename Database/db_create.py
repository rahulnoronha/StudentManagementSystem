# Create a db and connection to the student database
import sqlite3


conn = sqlite3.connect('student.db')
cur = conn.cursor()
cur.execute("create table if not exists student (id int primary key, name varchar, age int, class int)")
cur.execute("PRAGMA table_info(student)")
print(cur.fetchall())
conn.commit()
conn.close()