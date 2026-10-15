import sqlite3

DB_PATH = "api/game.db"

def get_connection():
    print("get_connection")
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            score FLOAT NOT NULL,
            level INTEGER NOT NULL
        )""")
    return conn