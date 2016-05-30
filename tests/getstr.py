import sqlite3 as lite
from random import randrange
from os import getcwd

prefix = getcwd() + '/tests/data'
print prefix
def getstring():
    conn = lite.connect(prefix +'/words.db')
    cur = conn.cursor()
    words = ""
    for row in cur.execute('SELECT Word FROM words ORDER BY random() LIMIT 5;'):
        words = words + row[0]
    return words

def getdom():
    conn = lite.connect(prefix + '/names.db')
    cur = conn.cursor()
    cur.execute('SELECT FName FROM names ORDER BY random() LIMIT 1;')
    d1 = cur.fetchone()
    cur.execute('SELECT MName FROM names ORDER BY random() LIMIT 1;')
    d2 = cur.fetchone()
    domains = ['com', 'io', 'eu','xyz']
    proto = ['http','https']
    string = getstring()
    return proto[randrange(len(proto))] + '://' + d1[0] + d2[0] + '.' + domains[randrange(len(domains))] + '/' + string

if __name__ == '__main__':
    for i in range(2):
        print getdom()
