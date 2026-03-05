import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS master (password TEXT, salt BLOB)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS passwords (name TEXT, username TEXT, password TEXT)")

    def masterSetup(self, password, salt):
        self.cursor.execute("INSERT INTO master (password, salt) VALUES (?, ?)", (password, salt))
        self.connection.commit()

    def insert(self, name, username, password):
        self.cursor.execute("INSERT INTO passwords (name, username, password) VALUES (?, ?, ?)", (name, username, password))
        self.connection.commit()

    def select(self):
        self.cursor.execute("SELECT * FROM passwords")
        return self.cursor.fetchall()

    def update(self, name, username, password):
        self.cursor.execute("UPDATE passwords SET password = ? WHERE name = ?", (password, name))
        self.connection.commit()

    def delete(self, name):
        self.cursor.execute("DELETE FROM passwords WHERE name = ?", (name, ))
        self.connection.commit()
