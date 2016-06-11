import sqlite3 as db

def createdb():
    conn = db.connect('data/urls.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE urls ( ref INT, value TEXT);")
    conn.commit()
createdb()