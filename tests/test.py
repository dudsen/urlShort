import sys,os
print os.getcwd()
sys.path.append(os.getcwd())
print sys.path
from urlShortCore import interfaceout
import sqlite3 as db
dbname = '../data/urls.db'
number = 3
conn = db.connect(dbname)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM urls WHERE ref=?", (number,))
data = cur.fetchone()
print data
