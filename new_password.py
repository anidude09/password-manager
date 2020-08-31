import sqlite3

conn=sqlite3.connect("pwdatabase.db")

c= conn.cursor()

def new_password():
    conn=sqlite3.connect("pwdatabase.db")
    c= conn.cursor()
    
    website = input("Enter website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    c.execute(""" INSERT INTO passwords(website, username, password) 
        VALUES(?, ?, ?)
        """,( website, username, password))
        
    conn.commit()

    c.execute("SELECT * FROM passwords ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    for row in result:
        print(row)

    conn.close()
    input("Press ENTER to exit. ")
    return
