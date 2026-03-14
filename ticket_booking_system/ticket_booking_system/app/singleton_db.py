import sqlite3

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect("tickets.db", check_same_thread=False)
        return cls._instance

    def get_connection(self):
        return self.conn