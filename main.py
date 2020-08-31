import sqlite3
import os
import new_password
import searchall
import delete


ADMIN_PASSWORD = "mafiarex"

connect = input("Enter your password:  ")

while connect != ADMIN_PASSWORD:
    connect = input("INCORRECT! Enter your password: ")
    if connect == 'q': break
    os.system('cls')

conn = sqlite3.connect("pwdatabase.db")

c = conn.cursor()

print(conn)


while True:
    os.system('cls')
    print("\n Welcome to the password manager\n")
    print("Commands: ")
    print(" s = See all passwords")
    print(" n = New Password")
    print(" d = Delete Password")
    print(" q = Quit\n")

    userInput = input("Enter command: ")
    os.system("cls")
    if userInput == "s":
        searchall.search_all()
    elif userInput == "n":
        new_password.new_password()
    elif userInput == "d":
        delete.delete_password()
    elif userInput == "q":
        break


