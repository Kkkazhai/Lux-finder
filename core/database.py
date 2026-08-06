import sqlite3


class Database:

    def __init__(self, db_name="luxfinder.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY,
            shop TEXT,
            brand TEXT,
            article TEXT,
            title TEXT,
            price INTEGER,
            old_price INTEGER,
            url TEXT,
            image TEXT,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.connection.commit()
