from random import randrange
import sqlite3 as db

def getref():
    def genrandom():
        return(randrange(2147483647))
    num = genrandom()
    if testfordb(num):
        return num
    else: 
        dupes = []
        count = 0
        while not testfordb(num) and count < 10:
            dupes.append(num)
            num = genrandom()
            count += 1
        if count < 10:
            return num
        else:
            print num, len(dupes)
            return False

def insert(ref, text):
    if ref:
        pushtodb(ref, text)
        return ref
    else: 
        print ref, text, "failure"
        return False

def testfordb(number):
    conn = db.connect('data/urls.db')
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM test WHERE ref=?", (number,))
    data = cur.fetchone()
    if data[0] == 0:
        return True
    else:
        return False

def pushtodb(ref, text):
    conn = db.connect('data/urls.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO test (ref, value) VALUES (?, ?)", (ref, text))
    conn.commit()

def getbyref(ref):
    conn = db.connect('data/urls.db')
    cur = conn.cursor()
    cur.execute("SELECT value FROM test WHERE ref=?", (ref,))
    data = cur.fetchone()
    if  data != None:
        return data[0]
    else:
        return False
def interfacein(url):
    return hex(insert(getref(),url)).lstrip('0x')

def interfaceout(hexa):
    ref = '0x' + hexa
    return getbyref(int(ref,16))

if __name__ == "__main__":
    print "test"          
