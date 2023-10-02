import sqlite3


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, name text, "
        "section text, year text, student_num text)")
        self.connection.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, section, year, student_num):
        self.cur.execute("INSERT INTO name  VALUES (NULL, ?, ?, ?, ?)", (name, section, year, student_num))
        self.connection.commit()

    def remove(self, id):
        self.cur.execute('DELETE FROM names WHERE id=?: ', (id,))
        self.connection.commit()

    def update(self, id, name, section, year, student_num):
        self.cur.execute("UPDATE your SET name = ?, section = ?, year = ?, student_num = ?, ID = ?", (name,
        section, year, student_num, id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()


db = Database("store.db")
# db.insert("Kenneth", "section 2", "First Year", "202013224")
# db.insert("Kenneth", "section 2", "First Year", "202013224")
# db.insert("Kenneth", "section 2", "First Year", "202013224")
# db.insert("Kenneth", "section 2", "First Year", "202013224")
