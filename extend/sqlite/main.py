import sqlite3

DB_NAME = 'test.db'
with sqlite3.connect(DB_NAME) as conn:
    print(conn)
    # cursor = conn.cursor()
    # cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)""")
    # cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ('John', 'john@example.com'))
    # conn.commit()
    sql_request = """SELECT * FROM users"""
    cursor = conn.cursor()
    cursor.execute(sql_request)
    print(cursor.fetchall())