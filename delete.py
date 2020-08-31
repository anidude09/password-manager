import sqlite3
import os

def delete_password():
    conn=sqlite3.connect("pwdatabase.db")
    c = conn.cursor()
    print(conn)

    print("\n Deleting by website..")
    user_input= input("Enter the website: ")

    c.execute ("""DELETE FROM passwords
        WHERE website = ?
        """, (user_input,) )
    

    conn.commit()
    conn.close()

    print("\n Your password has been deleted! ")
    input("Press ENTER to exit")
    return