import sqlite3
import bcrypt

def hash_password(password):
    secret = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), secret)
    return hashed

def add_user(email, plain_password):
    hashed_password = hash_password(plain_password)
    cursor.execute("INSERT INTO user (email, password) VALUES (?, ?)", (email, hashed_password))
    conn.commit()

def main():
    global conn, cursor
    conn = sqlite3.connect('''./Documents/noogas/sqlite/logindb.db''')
    cursor = conn.cursor()

    email = 'Paul@xmail.com' 
    password = 'password'
    add_user(email, password)

    conn.close()

if __name__ == "__main__":
    main()    