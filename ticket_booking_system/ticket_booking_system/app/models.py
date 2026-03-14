from .singleton_db import Database

class TicketModel:

    def __init__(self):
        db = Database()
        self.conn = db.get_connection()
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            movie TEXT,
            seats INTEGER
        )
        """)
        self.conn.commit()

    def book_ticket(self, name, movie, seats):
        self.conn.execute(
            "INSERT INTO bookings(name,movie,seats) VALUES(?,?,?)",
            (name, movie, seats)
        )
        self.conn.commit()

    def get_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM bookings")
        return cur.fetchall()