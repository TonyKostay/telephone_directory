import sqlite3
import math
def connect_db():
    conn = sqlite3.connect('telestatDB.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_bd():
    db = connect_db()
    db.cursor().execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    number INTEGER NOT NULL,
    email TEXT NOT NULL,
    department TEXT NOT NULL);''')
    db.commit()
    db.close()

class TelestatDB():
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def search_users(self, search):
        self.__cur.execute(f'''SELECT * from users WHERE name LIKE '%{search.lower()}%' OR position LIKE '%{search.lower()}%' OR email LIKE '%{search.lower()}%' or department LIKE '%{search.lower()}' OR number LIKE '%{search}%' ''')
        return self.__cur.fetchall()


