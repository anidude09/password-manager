import sqlite3

conn=sqlite3.connect("pwdatabase.db")

print(conn)

c = conn.cursor()


c.execute(""" CREATE TABLE passwords
   (id INTEGER PRIMARY KEY AUTOINCREMENT,
   website TEXT,
   username TEXT,
   password TEXT)""" )


conn.commit()


