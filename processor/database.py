import sqlite3

conn = sqlite3.connect("events.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    order_time TEXT,
    payment_time TEXT,
    status TEXT
)
""")

conn.commit()